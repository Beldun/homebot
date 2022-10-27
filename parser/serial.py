from bs4 import BeautifulSoup as BS
import requests

URL_fanta = 'https://hdrezka.co/series/fantasy/'
URL_comedy = 'https://hdrezka.co/series/comedy/'
URL_adventure = 'https://hdrezka.co/series/advenures/'
URL_melodramas = 'https://hdrezka.co/series/melodrama/'

HEADERS = {
    'Acept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"
}


def get_html(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req


def get_genre_serial(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='b-content__inline_item')
    fanta = []
    for item in items:
        title = item.find('div', class_="b-content__inline_item-link").find('a').getText()
        link = item.find('div', class_="b-content__inline_item-link").find('a').get('href')
        more = item.find('div', class_="b-content__inline_item-link").find('div').getText()
        fanta.append([title, link, more])
    return fanta


def parser_fanta():
    html = get_html(URL_fanta)
    if html.status_code == 200:
        fanta = []
        for i in range(1, 2):
            html = get_html(f"{URL_fanta}page/{i}/")
            current_page = get_genre_serial(html.text)
            fanta.extend(current_page)
        return fanta
    else:
        raise Exception("Error in parser!!!")


def parser_comedy():
    html = get_html(URL_comedy)
    if html.status_code == 200:
        comedy = []
        for i in range(1, 2):
            html = get_html(f"{URL_comedy}page/{i}/")
            current_page = get_genre_serial(html.text)
            comedy.extend(current_page)
        return comedy
    else:
        raise Exception("Error in parser!!!")


def parser_adventure():
    html = get_html(URL_adventure)
    if html.status_code == 200:
        adventure = []
        for i in range(1, 2):
            html = get_html(f"{URL_adventure}page/{i}/")
            current_page = get_genre_serial(html.text)
            adventure.extend(current_page)
        return adventure
    else:
        raise Exception("Error in parser!!!")


def parser_melodramas():
    html = get_html(URL_melodramas)
    if html.status_code == 200:
        melodramas = []
        for i in range(1, 2):
            html = get_html(f"{URL_melodramas}page/{i}/")
            current_page = get_genre_serial(html.text)
            melodramas.extend(current_page)
        return melodramas
    else:
        raise Exception("Error in parser!!!")

