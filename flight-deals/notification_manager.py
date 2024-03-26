import smtplib


my_email = "erengokyildiz31@gmail.com"
password = "drokuoeariatymbf"
victim = "gokyildizsemieren@gmail.com"


class NotificationManager:
    def send_email(self, text):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=victim,
                                msg=f"Subject:{text} Degisim\n\n Haberlere bak")