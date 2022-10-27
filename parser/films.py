from bs4 import BeautifulSoup as BS
import requests

URL_fantasy = "https://hdrezka.co/films/fiction/"
URL_horror = "https://hdrezka.co/films/horror/"
URL_action = "https://hdrezka.co/films/action/"
URL_drama = "https://hdrezka.co/films/drama/"

HEADERS = {
    'Acept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"
}


def get_html(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req


def get_fantasy(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='b-content__inline_item')
    fantasy = []
    for item in items:
        title = item.find('div', class_="b-content__inline_item-link").find('a').getText()
        link = item.find('div', class_="b-content__inline_item-link").find('a').get('href')
        more = item.find('div', class_="b-content__inline_item-link").find('div').getText()
        fantasy.append([title, link, more])
    return fantasy


def parser_fantasy():
    html = get_html(URL_fantasy)
    if html.status_code == 200:
        fantasy = []
        for i in range(1, 2):
            html = get_html(f"{URL_fantasy}page/{i}/")
            current_page = get_fantasy(html.text)
            fantasy.extend(current_page)
        return fantasy
    else:
        raise Exception("Error in parser!!!")


def get_horror(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='b-content__inline_item')
    horror = []
    for item in items:
        title = item.find('div', class_="b-content__inline_item-link").find('a').getText()
        link = item.find('div', class_="b-content__inline_item-link").find('a').get('href')
        more = item.find('div', class_="b-content__inline_item-link").find('div').getText()
        horror.append([title, link, more])
    return horror


def parser_horror():
    html = get_html(URL_horror)
    if html.status_code == 200:
        horror = []
        for i in range(1, 2):
            html = get_html(f"{URL_horror}page/{i}/")
            current_page = get_horror(html.text)
            horror.extend(current_page)
        return horror
    else:
        raise Exception("Error in parser!!!")


def get_action(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='b-content__inline_item')
    action = []
    for item in items:
        title = item.find('div', class_="b-content__inline_item-link").find('a').getText()
        link = item.find('div', class_="b-content__inline_item-link").find('a').get('href')
        more = item.find('div', class_="b-content__inline_item-link").find('div').getText()
        action.append([title, link, more])
    return action


def parser_action():
    html = get_html(URL_action)
    if html.status_code == 200:
        action = []
        for i in range(1, 2):
            html = get_html(f"{URL_action}page/{i}/")
            current_page = get_action(html.text)
            action.extend(current_page)
        return action
    else:
        raise Exception("Error in parser!!!")


def get_drama(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='b-content__inline_item')
    drama = []
    for item in items:
        title = item.find('div', class_="b-content__inline_item-link").find('a').getText()
        link = item.find('div', class_="b-content__inline_item-link").find('a').get('href')
        more = item.find('div', class_="b-content__inline_item-link").find('div').getText()
        drama.append([title, link, more])
    return drama


def parser_drama():
    html = get_html(URL_drama)
    if html.status_code == 200:
        drama = []
        for i in range(1, 2):
            html = get_html(f"{URL_drama}page/{i}/")
            current_page = get_drama(html.text)
            drama.extend(current_page)
        return drama
    else:
        raise Exception("Error in parser!!!")

