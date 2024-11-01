import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movie_site = response.text

soup = BeautifulSoup(movie_site,"html.parser")

movie_title_tags = soup.find_all(name='h3', class_='title')

movie_list = [tag.get_text() for tag in movie_title_tags]

movie_list.reverse()


with open("movies.txt",mode="w",encoding="utf-8") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")