from tkinter import *
window = Tk() #Pencere oluşturur #Window Start
window.title("Day 27 Code")
window.minsize(width=400, height=600)
window.config(padx=10, pady=10) #10'ar px boşluk verdik
#Label
label1 = Label(text="Hello World", font=("Arial", 24, "normal")) #Etiket oluşturur
# label1.pack() #Etiketi pencereye birleştirir

# label1["text"] = "Yeni yazı"  #İkiside text değiştirir
label1.config(text="Yeni yazı") #İkiside text değiştirir
label1.grid(column=0, row=0)
#Button
def button1_clicked():
    label1["text"] = input.get() #Yazıyı Labela yazdı

button1 = Button(text="Bana Tıkla", command=button1_clicked)
# button1.place(x=50, y=50)
button1.grid(column=1, row=1)
#Entry # Yazı girme elemanı

input = Entry(width=10)
input.insert(END, "Az yazı")
# input.place(x=300, y=200)
input.grid(column=3, row=2)


button2 = Button(text="Deneme")
button2.grid(column=2, row=0)
window.mainloop() #Pencerenin durmasını sağlar #Window End