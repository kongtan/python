import requests

url = 'https://movie.douban.com/j/search_subjects'
params = {
    'type': 'movie',
    'tag': '热门',
    'sore': 'recommend',
    'page_limit': '20',
    'page_start': '20'
}


def getDouBanReMen():
    response = requests.get(url=url, params=params)
    resource = response.text
    return resource

getDouBanReMen()

def typeof(variate):
    type = None
    if isinstance(variate, int):
        type = "int"
    elif isinstance(variate, str):
        type = "str"
    elif isinstance(variate, float):
        type = "float"
    elif isinstance(variate, list):
        type = "list"
    elif isinstance(variate, tuple):
        type = "tuple"
    elif isinstance(variate, dict):
        type = "dict"
    elif isinstance(variate, set):
        type = "set"
    return type



