##################################
# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)
#
#
# result = calculate(multiply, 2, 3)
# print(result)


##################################
# def kabuk_func():
#     print("Dısarisi")
#
#     def iceri_func():
#         print("Icerisi")
#
#     iceri_func()
#
#
# kabuk_func()

##################################
# def kabuk_func():
#     print("Dısarisi")
#
#     def iceri_func():
#         print("Icerisi")
#
#     # iceri_func()
#     return iceri_func
#
#
# iceri_deger = kabuk_func()
# iceri_deger()  # Return edilen fonsiyon, bir değişken gibi aktarıldı ve çalıştırıldı.


######################################################################################################
# Python Decorator Function -> Kısacası varolna bir fonksiyona ekstra özellikler eklemek için @ operatörünü başına yazarak kullanırız
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Fonk öncesini ayarlayabiliriz buradan
        function()
        # Fonk sonrasını ayarlayabiliriz buradan

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


def say_greeting():
    print("How are you?")


say_hello()
say_bye()

decorated_function = delay_decorator(say_greeting)
decorated_function()

# Anladığım kadarıyla birden fazla fonksiyona modifiye yapmak gibi bişi. greeting ile diğerleri farklı yazılsada aynı çalışıyor
