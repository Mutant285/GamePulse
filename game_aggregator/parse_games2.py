from game_aggregator.games.models import Game
import requests
from bs4 import BeautifulSoup

URL = 'https://topgamez.online/'


def parse(URL):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36" }
    res = requests.get(URL, headers=headers)
    # with open('site.html', 'w') as file:
    #     file.write(response.text)


    soup = BeautifulSoup(res.text, 'lxml')
    links = soup.find_all('article', class_='ast-article-post')
    game_urls = []
    for link in links:
        game_url = link.find('div', class_='entry-title').find('a').get('href')
        game_urls.append(game_url)

    for game_url in game_urls:
        req = requests.get(game_url, headers=headers)
        game_name = game_url.split('/')[-2]

        # with open(f'data/{game_name}.html', 'w') as file:
        #     file.write(res.text)

        # with open(f'data/{game_name}.html') as file:
        #     scr = file.read()
        soup1 = BeautifulSoup(req.text, 'lxml')

        data = soup1.find('div', class_="site-content")



        title = data.find('div', class_='ast-post-format- single-layout-1').find('h1').text
        game = Game.objects.create(title=title)
        game.save()





    # downloads = game.find('span', class_='game-downloads').text.strip()
    # genre = game.find('span', class_='game-genre').text.strip()
    # rating = game.find('span', class_='game-rating').text.strip()
    # creation_date = game.find('span', class_='game-date').text.strip()
    # platform = game.find('span', class_='game-platform').text.strip()
    # publisher = game.find('span', class_='game-publisher').text.strip()





        # games.append({
        #     'title': title,
            # 'downloads': downloads,
            #  'rating': rating,
            # 'creation_date': creation_date,
            # 'platform': platform,
            # 'publisher': publisher,
        # })




    #
    #


    #
    # for game in games:
    #     print(game)

parse('https://torgamez.com/')

