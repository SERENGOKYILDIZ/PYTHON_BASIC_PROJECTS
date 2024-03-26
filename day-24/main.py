#Read
# file = open(file="my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

#Read 2
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

#Write
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")

#Append
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

#Path
with open("C:\\Users\Eren\Desktop\my_file.txt") as path_file:
    contents = path_file.read()
    print(contents)