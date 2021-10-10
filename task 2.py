import requests
import os
import pprint


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_upload_link(self, disk_file_path=None):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": 'test file.txt', "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint.pprint(response.json())
        return response.json()["href"]

    def upload_file_to_disk(self, path_to_file):
        url = f"{self.get_upload_link()}"
        with open(path_to_file, "rb") as f:
            response = requests.put(url=url, data=f)
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
        return response


if __name__ == '__main__':
    path_to_file = os.path.join(os.getcwd(), 'test file.txt')
    # print(path_to_file)
    token = " "

    ya_disk = YandexDisk(token)
    ya_disk.upload_file_to_disk(path_to_file)