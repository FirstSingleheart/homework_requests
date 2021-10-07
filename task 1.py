import requests
import pprint

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
    my_dict = {"Hulk": hulk_intelligence(),
               "Captain America": captain_america_intelligence(),
               "Thanos": thanos_intelligence()}

    the_smartest_character = max(my_dict)

    print(the_smartest_character)
