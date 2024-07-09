from tkinter import *
from tkinter import messagebox
import random
# a class that's useful for copying text into clipboard
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_letters = [random.choice(letters) for _ in range(nr_letters)]
password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

password_list = password_numbers + password_letters + password_symbols


def generate_password():
    random.shuffle(password_list)
    g_password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, g_password)
    # copies the generated password into the clipboard without having to manually do it
    pyperclip.copy(g_password)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get().upper()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website:
        {
            "email": username,
            "password": password,
        }}

    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
            if len(website) == 0 or len(username) == 0:
                messagebox.showinfo(title="Error", message="Please fill all the fields")
            elif website in data and username == data[website]["email"]:
                messagebox.showinfo(title=website, message=f"email:{username} \npassword:{data[website]['password']}")
            else:
                messagebox.showinfo(title="OOPS", message=f"No details for {website} Found")
    except FileNotFoundError:
        messagebox.showinfo(title='OOPS', message='There is no password saved.')

# ---------------------------- SAVE PASSWORD ------------------------------- #


# or you can just use a normal password.txt

def save_data():
    website = website_entry.get().upper()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

proj_img = PhotoImage(file="logo.png")

canvas = Canvas(height=200, width=200, highlightthickness=0)
canvas.create_image(100, 100, image=proj_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
username_label = Label(text="email/Username:")
username_label.grid(row=2, column=0)
password_label = Label(text="password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=33)
website_entry.grid(row=1, column=1, columnspan=2, stick='w')
# Focuses the cursor in the entry box
website_entry.focus()
username_entry = Entry(width=33)
username_entry.grid(row=2, column=1, columnspan=2, stick='w')

# insert class is used to preoccupy the empty space with text of your choice
# the first parameter is for the position of the cursor you want it to be
# for putting the cursor at the start we use zero and for at end we use 'END'
username_entry.insert(0, "pvedant090@gmail.com")
password_entry = Entry(width=23)
password_entry.grid(row=3, column=1, stick='w')

# Buttons
generate = Button(text="Generate Password", width=14, command=generate_password)
generate.grid(row=3, column=1, columnspan=2, stick='e')

add = Button(text="Add", width=36, command=save_data)
add.grid(row=4, column=1, columnspan=2, stick='w')

search = Button(text="Search", command=search_password)
search.grid(column=2, row=1)

window.mainloop()
