from flask import Flask
from mydecorator import *

app = Flask(__name__)


@app.route("/")  # Kullanıcıyı ana rotaya yönlendirir. Bu bir "Python Decorators" dur.
def hello_world():
    return "<h1 style='text-align:center;color:red'>Hello, World!</h1>"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:id>")
def greet(name, id):
    return f"Hello there {name}, your id = {id}"


if __name__ == "__main__":
    # Sunucuyu Debug modu ile çalıştırdık
    app.run(debug=True)
