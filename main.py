import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"
DATE = "1992-06-13"

CLIENT_ID = "27a0c1f8e6ab434aa1a2871dd0b14bbd"
CLIENT_SECRET = "f8f261dcacc84497bcdeac854da07a8a"

# date = input("Which date do you want to travel to? Type the date in this format YYYY-MM-DD:")

# get html code of page.
response = requests.get(URL+DATE)
website_html = response.text

# pass html code to beautiful soup to parser the code.
soup = BeautifulSoup(markup=website_html, features="html.parser")

# get the text in h3 to get the top 100 songs.
song_tags = soup.find_all(name='h3', class_='a-no-trucate', id="title-of-a-story")
song_names = [song.getText() for song in song_tags]
# song_names = [song.strip("\n") for song in song_names]