age: int
name: str
height: float
is_human: bool

# age = "SDASD" # Pycharm uayrı veriyor "BU INT MK" diye

age = 12
name = "Eren"
height = 1.76
is_human = True


def is_legal(its_age: int) -> bool: #Girişi int, Çıkışı bool
    if its_age > 18:
        return True
    else:
        return False


if is_legal(9):
    print("it is legal")
else:
    print("is it not legal")
