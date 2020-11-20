# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

from user_info import EMAIL
from generate_password import create_new_password

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def get_new_password():
    password = create_new_password()
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_inputs():
    """Returns a string with the data to save.
    Each field is separated with a '|' character.
    """
    return [website_input.get(), user_input.get(), password_input.get()]

def data_is_ok():
    data = get_inputs()
    CONFIRMATION_MESSAGE = f'This is the data you entered:\n Website: {data[0]}\n Email/user: {data[1]}\n Password: {data[2]}'
    return messagebox.askokcancel(title='Confirmation', message=CONFIRMATION_MESSAGE)

def field_is_empty():
    data = get_inputs()
    if len(data[0]) == 0 or len(data[1]) == 0 or len(data[2]) == 0:
        messagebox.showinfo(title='Oops', message='Please make sure all fields are filled in.')
        return True
    else:
        return False 

def clean_entry_fields():
    website_input.delete(0, END)
    # user_input.delete(0, END)
    password_input.delete(0, END)

def save():
    website, user, password = get_inputs()
    new_data = {
        website:{
            'user': user,
            'password': password
        }
    }
    if not field_is_empty():
        if data_is_ok():
            try:
                with open('passwords.json', 'r') as f:
                    data = json.load(f) # Read previous data     
            except FileNotFoundError:
                data = new_data
            else:
                data.update(new_data) # Update data
            finally:
                with open('passwords.json', 'w') as f:
                    json.dump(data, f, indent=4) # Write data to file
                clean_entry_fields()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title('Password manager')
window.config(padx=30, pady=30)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(window, text='Website')
website_label.grid(row=1, column=0)

user_label = Label(window, text='Email/username')
user_label.grid(row=2, column=0)

password_label = Label(window, text='Password')
password_label.grid(row=3, column=0)

# Inputs
website_input = Entry(width=44)
website_input.grid(row=1, column=1, columnspan=2)

user_input = Entry(width=44)
user_input.insert(0, EMAIL)
user_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=24)
password_input.grid(row=3, column=1)

# Buttons
gen_pw_button = Button(text='Generate password', command=get_new_password)
gen_pw_button.grid(row=3, column=2)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


#Window loop
window.mainloop()