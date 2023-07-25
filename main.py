from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

# Email
mail_label = Label(text="Email/Username:")
mail_label.grid(column=0, row=2)
mail_entry = Entry(width=35)
mail_entry.grid(column=1, row=2, columnspan=2)

# password
password_label = Label(text="Password:", width=21)
password_label.grid(column=0, row=3)
password_entry = Entry()
password_entry.grid(column=1, row=3)

# generate password
btn = Button(text="Generate password")
btn.grid(column=2, row=3)

# add btn
add_btn = Button(text="Add", width=36)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()