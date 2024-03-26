from flask import Flask, render_template, request
from post import Post
import smtplib
# request == POST isteklerinde kullanılır (requests ile karıştırma!!!)

OWN_EMAIL = "erengokyildiz31@gmail.com"
OWN_PASSWORD = "drokuoeariatymbf"

app = Flask(__name__)

post = Post()
postes = []


@app.route('/')
def home():
    global postes
    post.request_posts()
    postes = post.get_posts()
    return render_template("index.html", postes=postes)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST": #gelen isteğin "POST" olup olmadığı kontrol edilir
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:num>")
def getPost(num):
    return render_template("post.html", post=postes[num])


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True)
