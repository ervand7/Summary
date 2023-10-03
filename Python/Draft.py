import requests
from bs4 import BeautifulSoup
import json


class HabrParser:
    def __init__(self):
        self.url = 'https://habr.com/ru/all/'
        self.params = {
            'q': 'python',
            'order': 'relevance'
        }

    def get_response(self):
        response = requests.get(self.url, params=self.params)
        return response

    def get_content(self):
        response = self.get_response()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def get_articles(self):
        soup = self.get_content()
        articles = soup.find_all('article', class_='post')
        return articles

    def get_article_data(self, article):
        title = article.find('a', class_='post__title_link').text
        date = article.find('span', class_='post__time').text
        link = article.find('a', class_='post__title_link').get('href')
        return title, date, link

    def get_articles_data(self):
        articles = self.get_articles()
        articles_data = []
        for article in articles:
            articles_data.append(self.get_article_data(article))
        return articles_data

    def get_articles_data_to_json(self):
        articles_data = self.get_articles_data()
        articles_data_json = json.dumps(articles_data, ensure_ascii=False)
        return articles_data_json


parser = HabrParser()
print(parser.get_articles_data_to_json())


class TestHabrParser:
    def setup(self):
        self.parser = HabrParser()

    def test_get_response(self):
        response = self.parser.get_response()
        assert response.status_code == 200

    def test_get_content(self):
        soup = self.parser.get_content()
        assert soup is not None

    def test_get_articles(self):
        articles = self.parser.get_articles()
        assert len(articles) > 0

    def test_get_article_data(self):
        article = self.parser.get_articles()[0]
        article_data = self.parser.get_article_data(article)
        assert len(article_data) == 3

    def test_get_articles_data(self):
        articles_data = self.parser.get_articles_data()
        assert len(articles_data) > 0

    def test_get_articles_data_to_json(self):
        articles_data_json = self.parser.get_articles_data_to_json()
        assert len(articles_data_json) > 0
