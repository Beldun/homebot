from bs4 import BeautifulSoup as BS
import requests

URL_romance = "https://hdrezka.co/films/romance/"
URL_samurai = "https://hdrezka.co/films/samurai/"
URL_shounenai = "https://hdrezka.co/films/shounenai/"
URL_everyday = "https://hdrezka.co/films/everyday/"

HEADERS = {
    'Acept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"
}


def get_html(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req


def get_romance(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='b-content__inline_item')
    romance = []
    for item in items:
        title = item.find('div', class_="b-content__inline_item-link").find('a').getText()
        link = item.find('div', class_="b-content__inline_item-link").find('a').get('href')
        more = item.find('div', class_="b-content__inline_item-link").find('div').getText()
        romance.append([title, link, more])
    return romance


def parser_romance():
    html = get_html(URL_romance)
    if html.status_code == 200:
        romance = []
        for i in range(1, 2):
            html = get_html(f"{URL_romance}page/{i}/")
            current_page = get_romance(html.text)
            romance.extend(current_page)
        return romance
    else:
        raise Exception("Error in parser!!!")


def parser_samurai():
    html = get_html(URL_samurai)
    if html.status_code == 200:
        samurai = []
        for i in range(1, 2):
            html = get_html(f"{URL_samurai}page/{i}/")
            current_page = get_romance(html.text)
            samurai.extend(current_page)
        return samurai
    else:
        raise Exception("Error in parser!!!")


def parser_shounenai():
    html = get_html(URL_shounenai)
    if html.status_code == 200:
        shounenai = []
        for i in range(1, 2):
            html = get_html(f"{URL_shounenai}page/{i}/")
            current_page = get_romance(html.text)
            shounenai.extend(current_page)
        return shounenai
    else:
        raise Exception("Error in parser!!!")


def parser_everyday():
    html = get_html(URL_everyday)
    if html.status_code == 200:
        everyday = []
        for i in range(1, 2):
            html = get_html(f"{URL_everyday}page/{i}/")
            current_page = get_romance(html.text)
            everyday.extend(current_page)
        return everyday
    else:
        raise Exception("Error in parser!!!")

