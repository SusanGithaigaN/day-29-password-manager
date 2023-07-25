from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # password_list = []
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# save files into data.txt on command of add button
def save():
    # get entries
    saved_password = password_entry.get()
    saved_mail = mail_entry.get()
    saved_web = website_entry.get()

    #     validation for user entries
    if len(saved_web) == 0 or len(saved_password) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure you haven't left any fields empty")
    else:
        # messagebox.showinfo(title="", message="")
        is_ok = messagebox.askokcancel(title="Website", message=f"These are the details entered: "
                                                                f"\nEmail: {saved_mail}\nWebsite: {saved_web}\n"
                                                                f"Password:{saved_password}\nIs it okay to save?")
        if is_ok:
            with open("data.txt", "a") as new_file:
                new_file.write(f"{saved_web} | {saved_mail} | {saved_password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)
window.minsize(width=200, height=200)

# canvas
canvas = Canvas(width=189, height=200)
# add image
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# labels
website = Label(text="Website:")
website.grid(column=0, row=1)
# entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# Email
mail_label = Label(text="Email/Username:")
mail_label.grid(column=0, row=2)
mail_entry = Entry(width=35)
mail_entry.insert(0, "susangithaiga@gmail.com")
mail_entry.grid(column=1, row=2, columnspan=2)

# password
password_label = Label(text="Password:", width=21)
password_label.grid(column=0, row=3)
password_entry = Entry()
password_entry.grid(column=1, row=3)

# generate password
btn = Button(text="Generate password", command=generate_password)
btn.grid(column=2, row=3)

# add btn
add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(column=1, row=4, columnspan=2)



window.mainloop()