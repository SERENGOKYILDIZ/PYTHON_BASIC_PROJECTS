#TODO1: Create a letter using starting_letter.txt
#TODO2:for each name in invited_names.txt
#TODO3: Replace the [name] placeholder with the actual name.
#TODO4: Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
letter = ""
with open("./Input/Names/invited_names.txt", mode="r") as name:
    names = name.readlines()
    for i in range(len(names)):
        names[i] = names[i].replace("\n","")

with open("./Input/Letters/starting_letter.txt", mode="r") as start_letter:
    letter = start_letter.read()

for a in range(len(names)):
    with open(f"./Output/ReadyToSend/letter_for_{names[a]}.txt", mode="w") as finish_letter:
        new_letter = letter.replace("[name]", names[a])
        finish_letter.write(new_letter)
print(letter)

print(names)