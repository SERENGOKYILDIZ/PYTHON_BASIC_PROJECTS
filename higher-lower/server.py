from flask import Flask
import random

GIF = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
HIGH_GIF = "https://media0.giphy.com/media/MBaeLRcqYNyk5p1zu0/giphy.gif?cid=ecf05e47fom5myl8isbk3mmya3yi931jm60qb603hc83ixdu&ep=v1_gifs_search&rid=giphy.gif&ct=g"
LOW_GIF = "https://media4.giphy.com/media/NXgyr1jxOKMDA0ilWO/giphy.gif?cid=ecf05e47ulm2fdy7d90j1pdlw9e9dn1y2jii9eqjtg9kidb6&ep=v1_gifs_search&rid=giphy.gif&ct=g"
TRUE_GIF = "https://media1.giphy.com/media/puFgQGYANZRUhFU0eE/giphy.gif?cid=ecf05e47ymtirzw5jvwlqshvdcpz1x4zv4nxk1y1uck7a252&ep=v1_gifs_search&ct=g"

app = Flask(__name__)

choicen_number = random.randint(0, 9)


@app.route("/")
def hello_world():
    return f"{header('Guess a number between 0 and 9', 'black')}{gif(GIF)}"


@app.route("/<int:num>")
def estimate(num):
    if num < choicen_number:
        return f"{header('Too low, try again!', 'red')}{gif(LOW_GIF)}"
    elif num > choicen_number:
        return f"{header('Too high, try again!', 'purple')}{gif(HIGH_GIF)}"
    else:
        return f"{header('You found me!', 'green')}{gif(TRUE_GIF)}"


def make_header(function):
    def wrapper(*args):
        return f"<h1 style='color:{args[1]}'>{args[0]}</h1>"

    return wrapper


def make_img(function):
    def wrapper(*args):
        return f"<img src='{args[0]}'>"

    return wrapper


@make_header
def header(text, color):
    return text


@make_img
def gif(Mygif):
    return Mygif


if __name__ == "__main__":
    # Sunucuyu Debug modu ile çalıştırdık
    app.run(debug=True)
