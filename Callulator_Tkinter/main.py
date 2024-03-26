from tkinter import *

window = Tk()
window.title("Hesap Makinesi")
window.minsize(width=400, height=400)
window.config(padx=20, pady=20)

def write_1():
    result_Lb["text"] += "1"
def write_2():
    result_Lb["text"] += "2"
def write_3():
    result_Lb["text"] += "3"
def write_4():
    result_Lb["text"] += "4"
def write_5():
    result_Lb["text"] += "5"
def write_6():
    result_Lb["text"] += "6"
def write_7():
    result_Lb["text"] += "7"
def write_8():
    result_Lb["text"] += "8"
def write_9():
    result_Lb["text"] += "9"
def write_0():
    result_Lb["text"] += "0"

def write_pl():
    result_Lb["text"] += "+"
def write_ng():
    result_Lb["text"] += "-"
def write_ml():
    result_Lb["text"] += "*"
def write_es():
    result_Lb["text"] += "/"

def hesapla():
    sum = eval(result_Lb.cget("text"))
    result_Lb["text"] = str(sum)

result_Lb = Label(text="", font=("Arial", 36, "bold"), padx=10, pady=10)
result_Lb.grid(column=1, row=0)

button_1 = Button(text="1", font=("Arial", 24, "normal"), command=write_1)
button_1.config(width=3, height=1)
button_1.grid(column=0, row=1)
button_2 = Button(text="2", font=("Arial", 24, "normal"), command=write_2)
button_2.config(width=3, height=1)
button_2.grid(column=1, row=1)
button_3 = Button(text="3", font=("Arial", 24, "normal"), command=write_3)
button_3.config(width=3, height=1)
button_3.grid(column=2, row=1)

button_4 = Button(text="4", font=("Arial", 24, "normal"), command=write_4)
button_4.config(width=3, height=1)
button_4.grid(column=0, row=2)
button_5 = Button(text="5", font=("Arial", 24, "normal"), command=write_5)
button_5.config(width=3, height=1)
button_5.grid(column=1, row=2)
button_6 = Button(text="6", font=("Arial", 24, "normal"), command=write_6)
button_6.config(width=3, height=1)
button_6.grid(column=2, row=2)

button_7 = Button(text="7", font=("Arial", 24, "normal"), command=write_7)
button_7.config(width=3, height=1)
button_7.grid(column=0, row=3)
button_8 = Button(text="8", font=("Arial", 24, "normal"), command=write_8)
button_8.config(width=3, height=1)
button_8.grid(column=1, row=3)
button_9 = Button(text="9", font=("Arial", 24, "normal"), command=write_9)
button_9.config(width=3, height=1)
button_9.grid(column=2, row=3)

button_0 = Button(text="0", font=("Arial", 24, "normal"), command=write_0)
button_0.config(width=5, height=1)
button_0.grid(column=1, row=4)

button_plus = Button(text="+", font=("Arial", 24, "normal"), command=write_pl)
button_plus.config(width=3, height=1)
button_plus.grid(column=3, row=1)

button_nega = Button(text="-", font=("Arial", 24, "normal"), command=write_ng)
button_nega.config(width=3, height=1)
button_nega.grid(column=3, row=2)

button_multi = Button(text="x", font=("Arial", 24, "normal"), command=write_ml)
button_multi.config(width=3, height=1)
button_multi.grid(column=3, row=3)

button_episode = Button(text="/", font=("Arial", 24, "normal"), command=write_es)
button_episode.config(width=3, height=1)
button_episode.grid(column=3, row=4)

button_calculator = Button(text="Hesapla", font=("Arial", 24, "bold"), command=hesapla)
button_calculator.config(width=5, height=1)
button_calculator.grid(column=1, row=5)


# input1 = Entry(width=10)
# input1.grid(column=1, row=0)
#
# def button1_clicked():
#     mill = float(input1.get())
#     km = mill * 1.6
#     label3["text"] = int(km)
# button1 = Button(text="Hesapla", command=button1_clicked)
# button1.grid(column=1, row=2)
#
# label1 = Label(text="Mill")
# label1.grid(column=2, row=0)
#
# label2 = Label(text="eşittir")
# label2.grid(column=0, row=1)
#
# label3 = Label(text="0")
# label3.grid(column=1, row=1)
#
# label4 = Label(text="Km")
# label4.grid(column=2, row=1)






window.mainloop()

# print(eval("2+4"))