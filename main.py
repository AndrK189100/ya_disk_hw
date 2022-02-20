import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': 'disk:/test.txt', 'overwrite': 'true'}
        headers = {'Authorization': self.token}
        resp = requests.get(url = url, params = params, headers = headers, timeout = 5).json()

        upload_url = resp['href']

        with open(file_path, 'rb') as f:
            resp = requests.put(url = upload_url, data = f, timeout = 5)
        pass
        if resp.status_code == 201:
            return True
        return False


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = os.path.join(os.getcwd(), 'test.txt')
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)



