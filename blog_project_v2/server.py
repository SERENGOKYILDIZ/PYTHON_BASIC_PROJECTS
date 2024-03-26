from flask import Flask, render_template
from post import Post

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


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:num>")
def getPost(num):
    return render_template("post.html", post=postes[num])


if __name__ == "__main__":
    app.run(debug=True)
