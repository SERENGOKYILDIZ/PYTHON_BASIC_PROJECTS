import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


# Write your code below this line 👇

Html_code = requests.get(url=URL)
soup = BeautifulSoup(Html_code.text, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w", encoding="utf8") as file:
    for title in movies:
        print(title)
        file.write(title)
        file.write("\n")