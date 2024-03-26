from tkinter import *

window = Tk()
window.title("M->K Çevirme")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

input1 = Entry(width=10)
input1.grid(column=1, row=0)

def button1_clicked():
    mill = float(input1.get())
    km = mill * 1.6
    label3["text"] = int(km)
button1 = Button(text="Hesapla", command=button1_clicked)
button1.grid(column=1, row=2)

label1 = Label(text="Mill")
label1.grid(column=2, row=0)

label2 = Label(text="eşittir")
label2.grid(column=0, row=1)

label3 = Label(text="0")
label3.grid(column=1, row=1)

label4 = Label(text="Km")
label4.grid(column=2, row=1)






window.mainloop()