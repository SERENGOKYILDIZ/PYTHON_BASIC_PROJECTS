##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv*

# 2. Check if today matches a birthday in the birthdays.csv*

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import smtplib
import datetime as dt
import random

my_email = "erengokyildiz31@gmail.com"
password = "drokuoeariatymbf"

now = dt.datetime.now()
letters = []

with open("./letter_templates/letter_1.txt") as letter:
    metin = letter.read()
    letters.append(metin)
with open("./letter_templates/letter_2.txt") as letter:
    metin = letter.read()
    letters.append(metin)
with open("./letter_templates/letter_3.txt") as letter:
    metin = letter.read()
    letters.append(metin)

data = pandas.read_csv("./birthdays.csv")
persons = data.to_dict(orient="records")

for person in persons:
    if person["day"] == now.day and person["month"] == now.month:
        msg = random.choice(letters)
        msg = msg.replace("[NAME]", person["name"])
        msg = msg.replace("Angela", "Eren")
        Hedef = person["mail"]
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=Hedef,
                msg=f"Subject:BirthDay\n\n{msg}")
