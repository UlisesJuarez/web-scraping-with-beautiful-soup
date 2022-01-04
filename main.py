from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com/news")
web_page=response.text
soup=BeautifulSoup(web_page,"html.parser")

articles=soup.find_all(name="a",class_="titlelink")
texts=[]
links=[]
for tag in articles:
    texts.append(tag.string)
    links.append(tag.get("href"))
article_upvotes=[int(score.string.split()[0]) for score in soup.find_all(name="span", class_="score")]

mayor=max(article_upvotes)
index=article_upvotes.index(mayor)

print(texts[index])
print(links[index])
print(mayor)


# with open("day 45/website.html") as file:
#     content=file.read()

# soup=BeautifulSoup(content,'html.parser')

# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup)

# # all_anchor_tags=soup.findAll(name="a")

# # for i in all_anchor_tags:
# #     # print(i.getText())
# #     # print(i.string)
# #     print(i.get("href"))

# # heading=soup.find(name="h1",id="name")

# # print(heading.string)

# name=soup.select_one(selector="#name")
# print(name)

# headings=soup.select(".heading")
# print(headings)