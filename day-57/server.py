from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)


# Böyle html'in içine python kodu yazmamızı sağlayan modül "jinja" dır.

@app.route('/')
def home():
    rand_int = random.randint(1, 10)
    now = dt.datetime.now()
    company_name = "JUPITER"
    return render_template("index.html", num=rand_int, comp_name=company_name, comp_year=now.year)


@app.route('/guess/<name>')
def guess(name: str):
    name = name.capitalize()
    person = {
        "name": name,
        "age": 0,
        "gender": "male"
    }
    response = requests.get(url="https://api.agify.io", params={"name": name})
    person["age"] = response.json()["age"]
    response = requests.get(url="https://api.genderize.io", params={"name": name})
    person["gender"] = response.json()["gender"]
    return render_template("guess.html", person=person)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    fake_blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=fake_blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
