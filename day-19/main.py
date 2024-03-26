#Örnek
# def add(a, b):
#     return a+b
# def subtract(a, b):
#     return a-b
# def multiply(a, b):
#     return a*b
# def divide(a, b):
#     return a/b
# def calculator(a, b, func):
#     return func(a,b)
#
# print(calculator(4,5, add))

from turtle import Turtle, Screen

tim = Turtle()
myScreen = Screen()

def move(): #Space e basınca 1 adım ilerleme yaptık!
    tim.forward(1)

myScreen.listen() #Kullanıcıdan herhangi bir tuş yazmasını bekler.
myScreen.onkey(key="space", fun=move) #Girilen tuşa göre fonksiyona gider.
myScreen.exitonclick()

