import requests

url = 'https://api.igdb.com/v4/games'
headers = {
    'Client-ID': 'lttfqcr1kuf8gsyiy4dnzr3wmq7rry',
    'Authorization': 'Bearer psh8gk6hyxozhyerftazlqw6vu3l1l',
    'Accept': 'application/json',
}
data = 'fields name, rating; limit 10;'

response = requests.post(url, headers=headers, data=data)
games_list = response.json()

for game in games_list:  # измените это на то, как у вас называется ваш список
    # if isinstance(game, dict):  # Проверьте, что game — это словарь
        print(f"Название: {game.get('name')}, Рейтинг: {game.get('rating', 'Нет рейтинга')}")
    # else:
    #     print("Ошибка: элемент не является словарем", game)


