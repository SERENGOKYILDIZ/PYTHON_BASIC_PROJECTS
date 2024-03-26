from tkinter import *
window = Tk() #Pencere oluşturur #Window Start
window.title("Day 27 Code")
window.minsize(width=400, height=600)

#Label
label1 = Label(text="Hello World", font=("Arial", 24, "normal")) #Etiket oluşturur
label1.pack() #Etiketi pencereye birleştirir

# label1["text"] = "Yeni yazı"  #İkiside text değiştirir
label1.config(text="Yeni yazı") #İkiside text değiştirir

#Button
def button1_clicked():
    label1["text"] = input.get() #Yazıyı Labela yazdı

button1 = Button(text="Bana Tıkla", command=button1_clicked)
button1.pack()

#Entry # Yazı girme elemanı

input = Entry(width=10)
input.insert(END, "Az yazı")
input.pack()

#Text
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Çok yazı")
print(text.get("1.0", END))
text.pack()

#SpinBox
def spinbox1_used():
    print(spinbox1.get())
spinbox1 = Spinbox(from_=0, to=10, width=5, command=spinbox1_used)
spinbox1.pack()

#Scale
def scale1_used(value):
    print(value)
scale1 = Scale(from_=0, to=100, command=scale1_used)
scale1.pack()

#CheckButton
def checkbutton1_used():
    print(checked_state.get())
checked_state = IntVar()
checkbutton1 = Checkbutton(text="Açık mı?", variable=checked_state, command=checkbutton1_used)
checked_state.get()
checkbutton1.pack()

#RadioButton
def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Seçenek 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Seçenek 2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#ListBox
def listbox1_used(event):
    print(listbox1.get(listbox1.curselection()))
listbox1 = Listbox()
fruits = ["Apple", "Orange", "Pear", "Banana"]
for item in fruits:
    listbox1.insert(fruits.index(item), item)
listbox1.bind("<<ListboxSelect>>", listbox1_used)
listbox1.pack()

window.mainloop() #Pencerenin durmasını sağlar #Window End