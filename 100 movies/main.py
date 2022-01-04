import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

respuesta=requests.get(URL)
sitio=respuesta.text

soup=BeautifulSoup(sitio,"html.parser")

peliculas=soup.find_all(name="h3",class_="title")

titulos_pelis=[peli.string for peli in peliculas ]
pelis_asc=titulos_pelis[::-1]

with open("day 45/100 movies/movies.txt", mode="w") as archivo:
    for peli in pelis_asc:

        archivo.write(f"{peli}\n")

