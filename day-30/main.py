#FileNotFound
# with open("Myfile.txt", mode="r") as file:
#     file.read()

#KeyError
# my_dict = {"Key": "Value"}
# value = my_dict["non_key"]

#IndexError
# my_list = [0, 1, 2]
# value = my_list[9]

#TypeError
# text = "abc"
# print(text + 5)


try:
    file = open("myFile.txt")
    text = "abc"
    # print(text + 5)
except FileNotFoundError:
    print("Dosya hatası oluştu")
    file = open("myFile.txt", mode="w")
    file.write("Something")
    print("Dosya olusturuldu")
except TypeError as message:
    print(f"Tip hatası oluştu: {message}")
else:
    letter = file.read()
    print(letter)
finally:
    if type(4) != type(int):
        raise TypeError("Tip hatasi")
    file.close()
    print("Devam edelim ....")