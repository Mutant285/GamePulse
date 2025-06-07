import re

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from games.models import Game


class Command(BaseCommand):
    help = "Parse games from the given URL and save them to the database."

    def handle(self, *args, **options):
        url = 'https://torgamez.com/'
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
        res = requests.get(url, headers=headers)

        soup = BeautifulSoup(res.text, 'lxml')
        links = soup.find_all('article', class_='ast-article-post')
        game_urls = []
        for link in links:
            game_url = link.find('div', class_='entry-title').find('a').get('href')
            game_urls.append(game_url)

        for game_url in game_urls:
            req = requests.get(game_url, headers=headers)

            soup1 = BeautifulSoup(req.text, 'lxml')
            data = soup1.find('div', class_="site-content")
            detail = data.find('div', id='adlink_other').find('h3').find_next_sibling().text.strip()
            more_detail = re.split(r'[:\n]+', detail)

            title = data.find('div', class_='ast-post-format- single-layout-1').find('h1').text
            title = title.replace('torrent download for PC', '').strip()
            genre = more_detail[5]
            date = more_detail[-1]
            developer = more_detail[1]
            publisher = more_detail[3]
            description = data.find('div', id='adlink_other').find('p').text

            game = Game.objects.create(title=title, genre=genre, date=date, developer=developer, publisher=publisher,
                                       description=description)
            game.save()