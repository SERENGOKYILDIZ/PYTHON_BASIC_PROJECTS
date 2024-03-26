# *args Example
# def add(*args):
#     toplam = 0
#     for n in args:
#         toplam += n
#     return toplam
#
#
# print(add(2, 4, 5, 6))
# print(add(2, 4))


# **kwargs Example

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=1, multiply=3)

def deneme(**types):
    if types["add"] == 0:
        print("add adında argüman geldi!!")


deneme(add=0)