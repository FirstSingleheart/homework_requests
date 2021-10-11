import requests
import pprint

TOKEN = "2619421814940190"


def name_intelligence(name):
    url = f"https://superheroapi.com/api/{TOKEN}/search/{name}"
    params = {"name": name}
    response = requests.get(url=url, params=params, timeout=5)
    resp = response.json()
    return resp['results'][0]['powerstats']['intelligence']


if __name__ == '__main__':

    my_dict = {"Hulk": name_intelligence("Hulk"),
               "Captain America": name_intelligence("Captain America"),
               "Thanos": name_intelligence("Thanos")}

    the_smartest_character = max(my_dict)

    print(the_smartest_character)
