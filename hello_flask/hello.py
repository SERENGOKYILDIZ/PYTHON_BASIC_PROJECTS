from flask import Flask

app = Flask(__name__)


@app.route("/")  # Kullanıcıyı ana rotaya yönlendirir. Bu bir "Python Decorators" dur.
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/bye")
def say_bye():
    return "Bye"


if __name__ == "__main__":  # Bu kod sayesinde RUN butonu ile serveri kontrol edebileceğiz
    app.run()  # Serveri başlatır. "flask --app hello run" kodu yazmış gibi olur.

# Bu kod ile random'un dışarıdan dahil edildiğini isminin çıkış verilmesiyle anlayabiliriz.
# import random
#
# print(random.__name__)


# print(__name__)  # __name__ = "__main__" çıktısı geliyor.
# # Burada __name__ "Special Attributes" tur.


# class anan:
#     pass
#
# print(anan.__name__)  # Görüldüğü gibi sınıfın adını çıktı olarak bize veriyor
