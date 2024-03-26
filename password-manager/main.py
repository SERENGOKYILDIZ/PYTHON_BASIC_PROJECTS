from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    password_input.delete(0, END)
    password_input.insert(END, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if website != "" and password != "":
        try:
            with open("data.json", mode="r") as file:
                #Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new_data
            data.update(new_data)
            with open("data.json", mode="w") as file:
                #Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
    else:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left ant fields empty.")

def search():
    website = website_input.get()
    try:
        with open("data.json", mode="r") as file:
            # Reading old data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.askokcancel(title="Oops", message="Dosya yok")

    try:
        messagebox.askokcancel(title=website, message=f"email: {data[website]['email']} \npassword: {data[website]['password']}")
    except KeyError:
        messagebox.askokcancel(title="Oops", message="Boyle bir veri yok")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass Program")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

label1 = Label(text="Website:")
label1.grid(column=0, row=1)

label2 = Label(text="Email/Username:")
label2.grid(column=0, row=2)

label3 = Label(text="Password:")
label3.grid(column=0, row=3)

website_input = Entry(width=21)
website_input.grid(column=1, row=1, sticky="EW")
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_input.insert(END, "eren@email.com") # END ile üstüne gelince hepsine seçer ve işimizi kolaylaştırır

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="EW")

Generate_Pass_Btn = Button(text="Generate Password", command=generate_password)
Generate_Pass_Btn.grid(column=2, row=3, sticky="EW")

Add_Btn = Button(text="Add", width=36, command=save_password)
Add_Btn.grid(column=1, row=4, columnspan=2, sticky="EW")

Search_Btn = Button(text="Search", command=search)
Search_Btn.grid(column=2, row=1, sticky="EW")







window.mainloop()