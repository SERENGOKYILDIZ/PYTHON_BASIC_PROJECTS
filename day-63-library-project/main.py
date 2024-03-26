from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
# uzantıyı oluştur
db = SQLAlchemy()
# uygulamayı oluştur
app = Flask(__name__)
# uygulama örneği klasörüne göre SQLite veritabanını yapılandırın
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# uygulamayı uzantı ile başlatın
db.init_app(app)

all_books = []


## Tablo sınıfı oluşturma
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # İsteğe bağlı: Bu, yazdırıldığında her kitap nesnesinin başlığına göre tanımlanmasına izin verecektir.
    def __repr__(self):
        return f'<Book {self.title}>'


## Veri tabanının sütunlarını oluşturur. (Yoksa)
with app.app_context():
    db.create_all()


## Veri ekleme
def Create(title, author, rating):
    with app.app_context():
        new_book = Book(title=title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()


## Tüm verileri okuma
def Read_all():
    global all_books
    with app.app_context():
        all_books = db.session.query(Book).all()


# all_books = [
#      {
#         "title": "Harry Potter",
#         "author": "J. K. Rowling",
#         "rating": 9,
#     }
# ]
@app.route('/')
def home():
    Read_all()
    return render_template("index.html", books=all_books)


@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":  # gelen isteğin "POST" olup olmadığı kontrol edilir
        data = request.form
        Create(data["title"], data["author"], data["rating"])
        Read_all()
        return render_template("index.html", books=all_books)
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
