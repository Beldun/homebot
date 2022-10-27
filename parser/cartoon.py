from bs4 import BeautifulSoup as BS
import requests

URL_tale = 'https://hdrezka.co/series/fairytale/'
URL_kids = 'https://hdrezka.co/series/kids/'
URL_cognitive = 'https://hdrezka.co/series/cognitive/'
URL_adult = 'https://hdrezka.co/series/adult/'

HEADERS = {
    'Acept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"
}


def get_html(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req


def get_genre_cartoon(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='b-content__inline_item')
    tale = []
    for item in items:
        title = item.find('div', class_="b-content__inline_item-link").find('a').getText()
        link = item.find('div', class_="b-content__inline_item-link").find('a').get('href')
        more = item.find('div', class_="b-content__inline_item-link").find('div').getText()
        tale.append([title, link, more])
    return tale


def parser_tale():
    html = get_html(URL_tale)
    if html.status_code == 200:
        tale = []
        for i in range(1, 2):
            html = get_html(f"{URL_tale}page/{i}/")
            current_page = get_genre_cartoon(html.text)
            tale.extend(current_page)
        return tale
    else:
        raise Exception("Error in parser!!!")


def parser_kids():
    html = get_html(URL_kids)
    if html.status_code == 200:
        kids = []
        for i in range(1, 2):
            html = get_html(f"{URL_kids}page/{i}/")
            current_page = get_genre_cartoon(html.text)
            kids.extend(current_page)
        return kids
    else:
        raise Exception("Error in parser!!!")


def parser_cognitive():
    html = get_html(URL_cognitive)
    if html.status_code == 200:
        cognitive = []
        for i in range(1, 2):
            html = get_html(f"{URL_cognitive}page/{i}/")
            current_page = get_genre_cartoon(html.text)
            cognitive.extend(current_page)
        return cognitive
    else:
        raise Exception("Error in parser!!!")


def parser_adult():
    html = get_html(URL_adult)
    if html.status_code == 200:
        adult = []
        for i in range(1, 2):
            html = get_html(f"{URL_adult}page/{i}/")
            current_page = get_genre_cartoon(html.text)
            adult.extend(current_page)
        return adult
    else:
        raise Exception("Error in parser!!!")

