import sqlite3

##### VERİTABANI OLUŞTURMA
db = sqlite3.connect("books-collection.db")
cursor = db.cursor()

##### TABLO OLUŞTURMA
# # Zaten tablo varsa "sqlite3.OperationalError: table books already exists" HATASI ALIRSIN
# cursor.execute("CREATE TABLE books "  # "CREATE TABLE" = Tablo oluşturma komutu, "books" = tablo ismi
#                "(id INTEGER PRIMARY KEY, "  # "id" = Sütun adımız, "INTEGER" = veri türü,
#                # "PRIMARY KEY" = benzersiz olsun demek
#                "title varchar(250) NOT NULL UNIQUE, "  # "varchar(250)" = 250 karakter alabilir,
#                # "NOT NULL" = boş olamaz, "UNIQUE" = diğer title lar ile farklı olmalı
#                "author varchar(250) NOT NULL, "
#                "rating FLOAT NOT NULL)")
#

##### VERİ EKLEME
# Tekrar aynı veriyi eklersen "sqlite3.IntegrityError: UNIQUE constraint failed: books.id" HATASI ALIRSIN
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
