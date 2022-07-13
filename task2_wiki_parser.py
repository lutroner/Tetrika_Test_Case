# Решение задачи 2

import requests
from bs4 import BeautifulSoup
from collections import defaultdict

WIKI_ENDPOINT = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'


def get_next_page_url(page: list):
    next_page_name = page[-1].get_text('title')
    name = '+'.join(next_page_name.split())
    return f'https://ru.wikipedia.org/w/index.php?title=Категория:' \
           f'Животные_по_алфавиту&pagefrom={name}#mw-pages'


def get_html(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def get_data(html: str) -> list:
    bs = BeautifulSoup(html, 'html.parser')
    li_list = bs.find('div', id='mw-pages').find_all('li')
    return li_list


def main() -> defaultdict:
    result = defaultdict(int)
    current_page = get_data(get_html(WIKI_ENDPOINT))
    while True:
        next_page_url = get_next_page_url(current_page)
        current_page = get_data(get_html(next_page_url))
        for element in current_page:
            element_title = element.get_text('title')
            result[element_title[0]] += 1
            if element_title == 'Ящурки':
                return result


if __name__ == '__main__':
    for letter, count in sorted(main().items()):
        print(f'{letter}: {count}')
