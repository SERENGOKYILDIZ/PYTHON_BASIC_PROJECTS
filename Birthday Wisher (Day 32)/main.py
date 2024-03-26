# import smtplib
#
# my_email = "erengokyildiz31@gmail.com"
# password = "drokuoeariatymbf"
#
# Hedef = "gokyildizsemieren@gmail.com"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     # connection = smtplib.SMTP("smtp.gmail.com", port=587) #Gmail posta servisine bağlanır
#     connection.starttls() #Şifrelemeyi başlatır
#     connection.login(user=my_email, password=password) #Kullanacağımız postaya giriş yapar
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=Hedef,
#         msg="Subject:Selam Eren\n\nSelam bu bir deneme mailidir.") #Hedefe mesaj gönderir
#     # connection.close() #İşlemi sonlandırır

# import datetime as dt #datetime'ı dt olarak kısalttık
#
# mytime = dt.datetime.now()
# year = mytime.year
# day_of_week = mytime.weekday()
#
# print(day_of_week)
# print(year)
# print(mytime)
#
# day_of_birth = dt.datetime(year=2002, month=1, day=25)
# print(day_of_birth)


import datetime as dt
import smtplib
import random

now = dt.datetime.now()
weekday = now.weekday()

with open("./quotes.txt") as file:
    quotes = file.readlines()

my_email = "erengokyildiz31@gmail.com"
password = "drokuoeariatymbf"

Hedef = "gokyildizsemieren@gmail.com"
myMsg = random.choice(quotes)

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=Hedef,
        msg=f"Subject:BirthDay\n\n{myMsg}")