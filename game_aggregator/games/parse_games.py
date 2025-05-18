import requests, random
from bs4 import BeautifulSoup

URL = "https://itorrents-igruha.net/"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"




headers = {"User-Agent": user_agent}
def parse(URL):
    response = requests.get(URL, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        games = []

        for game in soup.find_all('div', class_='article-film'):
            title = game.find('div', class_='article-film-image').text.strip()
          #  downloads = game.find('span', class_='game-downloads').text.strip()
           # genre = game.find('span', class_='game-genre').text.strip()
           # rating = game.find('span', class_='game-rating').text.strip()
           # creation_date = game.find('span', class_='game-date').text.strip()
            #platform = game.find('span', class_='game-platform').text.strip()
           # publisher = game.find('span', class_='game-publisher').text.strip()

            games.append({

                'title': title,
               # 'downloads': downloads,
                #'rating': rating,
            #    'creation_date': creation_date,
               # 'platform': platform,
              #  'publisher': publisher,
            })

        for game in games:
            print(game)
    else:
        print('Error')
parse(URL)
