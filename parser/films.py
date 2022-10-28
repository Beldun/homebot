from bs4 import BeautifulSoup as BS
import requests

URL = 'https://hdrezka.co'
# Фильмы
URL_fantasy = "https://hdrezka.co/films/fiction/"
URL_horror = "https://hdrezka.co/films/horror/"
URL_action = "https://hdrezka.co/films/action/"
URL_drama = "https://hdrezka.co/films/drama/"
# Сериалы
URL_fanta = 'https://hdrezka.co/series/fantasy/'
URL_comedy = 'https://hdrezka.co/series/comedy/'
URL_adventure = 'https://hdrezka.co/series/advenures/'
URL_melodramas = 'https://hdrezka.co/series/melodrama/'
# Мультфильмы
URL_tale = 'https://hdrezka.co/series/fairytale/'
URL_kids = 'https://hdrezka.co/series/kids/'
URL_cognitive = 'https://hdrezka.co/series/cognitive/'
URL_adult = 'https://hdrezka.co/series/adult/'
# Аниме
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


def get_genre(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='b-content__inline_item')
    status = []
    for item in items:
        title = item.find('div', class_="b-content__inline_item-link").find('a').getText()
        link = item.find('div', class_="b-content__inline_item-link").find('a').get('href')
        more = item.find('div', class_="b-content__inline_item-link").find('div').getText()
        status.append([title, link, more])
    return status


html_s = get_html(URL)
if html_s.status_code == 200:
    # Фильмы
    def parser_fantasy():
        fantasy = []
        for i in range(1, 2):
            html = get_html(f"{URL_fantasy}page/{i}/")
            current_page = get_genre(html.text)
            fantasy.extend(current_page)
        return fantasy

    def parser_horror():
        horror = []
        for i in range(1, 2):
            html = get_html(f"{URL_horror}page/{i}/")
            current_page = get_genre(html.text)
            horror.extend(current_page)
        return horror

    def parser_action():
        action = []
        for i in range(1, 2):
            html = get_html(f"{URL_action}page/{i}/")
            current_page = get_genre(html.text)
            action.extend(current_page)
        return action

    def parser_drama():
        drama = []
        for i in range(1, 2):
            html = get_html(f"{URL_drama}page/{i}/")
            current_page = get_genre(html.text)
            drama.extend(current_page)
        return drama

    # Сериалы
    def parser_fanta():
        fanta = []
        for i in range(1, 2):
            html = get_html(f"{URL_fanta}page/{i}/")
            current_page = get_genre(html.text)
            fanta.extend(current_page)
        return fanta

    def parser_comedy():
        comedy = []
        for i in range(1, 2):
            html = get_html(f"{URL_comedy}page/{i}/")
            current_page = get_genre(html.text)
            comedy.extend(current_page)
        return comedy

    def parser_adventure():
        adventure = []
        for i in range(1, 2):
            html = get_html(f"{URL_adventure}page/{i}/")
            current_page = get_genre(html.text)
            adventure.extend(current_page)
        return adventure

    def parser_melodramas():
        melodramas = []
        for i in range(1, 2):
            html = get_html(f"{URL_melodramas}page/{i}/")
            current_page = get_genre(html.text)
            melodramas.extend(current_page)
        return melodramas

    # Мультфильмы
    def parser_tale():
        tale = []
        for i in range(1, 2):
            html = get_html(f"{URL_tale}page/{i}/")
            current_page = get_genre(html.text)
            tale.extend(current_page)
        return tale

    def parser_kids():
        kids = []
        for i in range(1, 2):
            html = get_html(f"{URL_kids}page/{i}/")
            current_page = get_genre(html.text)
            kids.extend(current_page)
        return kids

    def parser_cognitive():
        cognitive = []
        for i in range(1, 2):
            html = get_html(f"{URL_cognitive}page/{i}/")
            current_page = get_genre(html.text)
            cognitive.extend(current_page)
        return cognitive

    def parser_adult():
        adult = []
        for i in range(1, 2):
            html = get_html(f"{URL_adult}page/{i}/")
            current_page = get_genre(html.text)
            adult.extend(current_page)
        return adult

    # Аниме
    def parser_romance():
        romance = []
        for i in range(1, 2):
            html = get_html(f"{URL_romance}page/{i}/")
            current_page = get_genre(html.text)
            romance.extend(current_page)
        return romance

    def parser_samurai():
        samurai = []
        for i in range(1, 2):
            html = get_html(f"{URL_samurai}page/{i}/")
            current_page = get_genre(html.text)
            samurai.extend(current_page)
        return samurai

    def parser_shounenai():
        shounenai = []
        for i in range(1, 2):
            html = get_html(f"{URL_shounenai}page/{i}/")
            current_page = get_genre(html.text)
            shounenai.extend(current_page)
        return shounenai

    def parser_everyday():
        everyday = []
        for i in range(1, 2):
            html = get_html(f"{URL_everyday}page/{i}/")
            current_page = get_genre(html.text)
            everyday.extend(current_page)
        return everyday
else:
    raise Exception("Error in parser!!!")
