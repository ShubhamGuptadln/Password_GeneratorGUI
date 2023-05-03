from tkinter import *
from tkinter import messagebox
import random
import pyperclip

#-------- password generator------->
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password=[]
    for i in range(2):
        a=random.choice(letters)
        password.append(a)
    for i in range(2):
        a=random.choice(numbers)
        password.append(a)
    for i in range(2):
        a=random.choice(symbols)
        password.append(a)
    random.shuffle(password)
    passw=""
    for i in password:
        passw+=i
    input_Password.insert(0,passw)
    pyperclip.copy(passw)

# ------------ Add button Function -------->
def add():
    # is_ok=messagebox.askokcancel(title='website',message=f"your website is {input_website}\nyour email is {input_email}\
    # \nyour password is {input_Password}\nAre you sure and want to continue")
    if len(input_Password.get()) == 0 or len(input_email.get()) == 0 or len(input_website.get()) == 0:
        messagebox.showerror(title='oops', message="Some fields are missing")

    else:
        messagebox.askokcancel(title='website',
                               message=f"your website is {input_website.get()}\nyour email is {input_email.get()}\
            \nyour password is {input_Password.get()}\nAre you sure and want to continue")
        with open('file.txt', 'a') as file:
            file.write(f"{input_website.get()} | {input_email.get()} | {input_Password.get()} \n")
        input_website.delete(0, END)
        input_Password.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
photo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

# --------Labels------------>
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# -------Entry------------>
input_website = Entry(width=35)
input_website.grid(row=1, column=1, columnspan=2)
input_email = Entry(width=35)
input_email.insert(0, "shubh@gmail.com")
input_email.grid(row=2, column=1, columnspan=2)
input_Password = Entry(width=21)
input_Password.grid(row=3, column=1)
# ---------- Buttons-------------->
generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=add)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
