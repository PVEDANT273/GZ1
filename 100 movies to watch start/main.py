import requests
from bs4 import BeautifulSoup
import os

URL = os.environ["URL"]

# Write your code below this line 👇
response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

top_movies = soup.findAll(name="h3", class_="title")

movie_titles = [movie.getText() for movie in top_movies]
# list[::-1] reverses the list
movies = movie_titles[::-1]
# '100)dfgdfsd took a string from the movies and returned its integer value
# an error is in the website at title no 12, its written as 12:xxxxxx
# rankings variable is of no use in this project, just for understanding purpose
rankings = [nos[:3] if nos[3] == ')'else nos[:2] if nos[2] == ')' or nos[2] == ':' else nos[:1] for nos in movies]
# error in the website, 80 is numbered as 15
rankings[79] = '80'
print(rankings)

# By using UTF-8 encoding, you can ensure that any Unicode characters in the movie titles are properly handled
# and written to the file without causing encoding errors.
with open("top_movies.txt", 'w', encoding='utf-8') as file:
    for movie in movies:
        file.write(f"{movie}\n")

