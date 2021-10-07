import requests
import pprint

'''Кто самый умный супергерой? 
Есть API по информации о супер-героях. 
Нужно определить кто самый умный(intelligence) из трех супер-героев - Hulk, Captain America, Thanos. 
Для определения id нужно использовать метод /search/name
Токен, который нужно использовать для доступа к API: 2619421814940190.
Таким образом, все адреса для доступа к API должны начинаться с https://superheroapi.com/api/2619421814940190/.

https://superheroapi.com/api/2619421814940190/search/name'''

TOKEN = "2619421814940190"


def hulk_intelligence():
    url = f"https://superheroapi.com/api/{TOKEN}/search/Hulk"
    params = {"name": "Hulk"}
    response = requests.get(url=url, params=params, timeout=5)
    hulk = response.json()
    return hulk['results'][0]['powerstats']['intelligence']


def captain_america_intelligence():
    url = f"https://superheroapi.com/api/{TOKEN}/search/Captain_America"
    params = {"name": "Captain America"}
    response = requests.get(url=url, params=params, timeout=5)
    captain_america = response.json()
    return captain_america['results'][0]['powerstats']['intelligence']


def thanos_intelligence():
    url = f"https://superheroapi.com/api/{TOKEN}/search/Thanos"
    params = {"name": "Thanos"}
    response = requests.get(url=url, params=params, timeout=5)
    thanos = response.json()
    return thanos['results'][0]['powerstats']['intelligence']


if __name__ == '__main__':
    # pprint.pprint(hulk_intelligence())
    # pprint.pprint(captain_america_intelligence())
    # pprint.pprint(thanos_intelligence())

    my_dict = {"Hulk": hulk_intelligence(),
               "Captain America": captain_america_intelligence(),
               "Thanos": thanos_intelligence()}
    the_smartest_character = max(my_dict)
    print(the_smartest_character)
