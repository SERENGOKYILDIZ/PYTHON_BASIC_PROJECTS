from bs4 import BeautifulSoup


# import lxml
#
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup)
# print("====== HTML ======")
# print(soup.prettify())
# print(soup.a)
#
# print(soup.find_all(name="a"))
# print(soup.find_all(name="p"))

# all_tags = soup.find_all("a")
# for text in all_tags:
#     # print(text.getText())
#     print(text.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
# print(section_heading.name)

# company_url = soup.select_one(selector="p a") #CSS selector kodu ile arama
# print(company_url)

# heading = soup.select_one(selector="#name") #CSS selector kodu ile arama
# print(heading)

# heading = soup.select(selector=".heading")
# print(heading)


#CANLI KOD KAZMA
import requests

response = requests.get("https://news.ycombinator.com/news")
html_data = response.text

soup = BeautifulSoup(html_data, "html.parser")
articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.a.getText()
    article_texts.append(text)
    link = article_tag.a.get("href")
    article_links.append(link)
article_upvotes = [int(score.text.split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

max_point = max(article_upvotes)
max_index = article_upvotes.index(max_point)
print()
print(max_index)
print(article_texts[max_index])
print(article_links[max_index])
print(max_point)









