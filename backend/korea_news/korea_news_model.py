from bs4 import BeautifulSoup
import requests


class KoreaNewsModel:
    def news_crawling(self):
        url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%BD%94%EB%A1%9C%EB%82%98'
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        a = soup.find_all('ul', {'class': 'type01'})
        result = []
        for item_a in a:
            b = item_a.find_all('li', {'id': not None})
            for item_b in b:
                link = item_b.find('dl').find('dt').find('a')['href']
                title = item_b.find('dl').find('dt').find('a')['title']
                result.append({"link": link, "title": title})
        return result
