from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# uzantıyı oluştur
db = SQLAlchemy()
# uygulamayı oluştur
app = Flask(__name__)
# uygulama örneği klasörüne göre SQLite veritabanını yapılandırın
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# uygulamayı uzantı ile başlatın
db.init_app(app)

all_books = []
book = 0


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


########## CRUD İşlemleri ##########

## Veri ekleme
def Create():
    with app.app_context():
        new_book = Book(id=1, title="Harry Potter 1", author="J. K. Rowling", rating=9.3)
        db.session.add(new_book)
        db.session.commit()


## Tüm verileri okuma
def Read_all():
    global all_books
    with app.app_context():
        all_books = db.session.query(Book).all()


## Belirli bir veri okuma
def Read_one():
    global book
    with app.app_context():
        book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter 1")).scalar()


## Belirli bir veri okuma
def Read_id(id: int):
    global book
    with app.app_context():
        book = db.session.execute(db.select(Book).where(Book.id == id)).scalar()


## Belirli bir özelliğe göre veri güncelleme
def Update_title():
    with app.app_context():
        book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter 1")).scalar()
        book_to_update.title = "Harry Potter and the Chamber of Secrets"
        db.session.commit()


## Belirli idye göre veri güncelleme
def Update_id():
    book_id = 1
    with app.app_context():
        book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        book_to_update.title = "Harry Potter and the Goblet of Fire"
        db.session.commit()


## Belirli idye göre veri silme
def Delete_id():
    book_id = 1
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        # or book_to_delete = db.get_or_404(Book, book_id)
        db.session.delete(book_to_delete)
        db.session.commit()


# Create()

# Read_all()
# print(all_books[0].title)

# Read_one()
# print(book)

# Update_id()
# Read_id(1)
# print(book)

Delete_id()
