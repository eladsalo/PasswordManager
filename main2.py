from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)  # for adding the password to the entry
    pyperclip.copy(password)
    # this will make that the new generated password will be on the clipboard,
    # therefore now we can press ctrl+v tp pasted it

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(website, user_name, password):
    if len(website) == 0 or len(user_name) == 0 or len(password) ==0 :
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title="Conformation", message=f"These are the details entered:\n"
                                                      f"\nEmail: {user_name} \nPassword: {password} \n Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website}  |  {user_name}  |  {password}\n")
                website_input.delete(0, END)
                email_input.delete(0, END)
                password_input.delete(0, END)
                email_input.insert(0, "@gmail.com")
                website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


# --- Labels --- #
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

website_label = Label(text="Password:")
website_label.grid(row=3, column=0)


# --- Buttons --- #
add_button = Button(text="Add", width=36, command=lambda: save(website_input.get(), email_input.get(), password_input.get()))
add_button.grid(row=4, column=1, columnspan=2)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)


# --- Entries --- #
website_input = Entry(width=39)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=39)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "elad2salomon@gmail.com")

password_input = Entry(width=25)
password_input.grid(column=1, row=3)

window.mainloop()