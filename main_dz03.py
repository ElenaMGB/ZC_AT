import requests


def get_catapi_url():
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:  # Проверяем, что список не пустой
            return data[0].get('url')  # Возвращаем сам URL изображения
    return None
