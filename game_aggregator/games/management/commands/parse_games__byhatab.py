import re

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from games.models import Game


class Command(BaseCommand):
    help = "Parse games from the given URL and save them to the database."

    def handle(self, *args, **options):
        url = 'https://byxatab.com/?ysclid=mbi0fgrmmn514311045'
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
        res = requests.get(url, headers=headers)

        soup = BeautifulSoup(res.text, 'lxml')
        links = soup.find_all('div', class_='entry')
        game_urls = []
        for link in links:
            game_url = link.find('div', class_='entry__title h2').find('a').get('href')
            game_urls.append(game_url)

        for game_url in game_urls:
            req = requests.get(game_url, headers=headers)

            soup1 = BeautifulSoup(req.text, 'lxml')
            data = soup1.find('div', id="dle-content")
            detail = data.find('div', class_='inner-entry__details').text.strip()
            more_detail = re.split(r'[:\n]+', detail)

            title = data.find(class_='inner-entry__allinfo').find('h1').text
            title = title.replace('[Архив]', '').replace('[Папка игры]', '').replace('Repak от xatab', '').strip()
            genre = more_detail[3]
            date = more_detail[1]
            developer = more_detail[5]
            publisher = more_detail[7]
            description = data.find('div', class_='inner-entry__content-text').find_next().find_next().text.strip()

            game = Game.objects.create(title=title, genre=genre, date=date, developer=developer, publisher=publisher,
                                        description=description)
            game.save()
