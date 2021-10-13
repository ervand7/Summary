from urllib.parse import urlparse, parse_qs, urlsplit, urljoin

url = 'https://www.google.com/search?q=linkedin&oq=linkedin&aqs=chrome..69i57j0l7.3961j0j15&sourceid=chrome&ie=UTF-8'
print(urlsplit(url))
parsed_url = urlparse(url)
print(parsed_url)
print(parse_qs(parsed_url.query))
print(parse_qs(urlsplit(url).query))

print('_________________________________________________________')


def get_query_params(url: str, param_name=None):
    """
    Парсит URL и отдает параметры запроса.
    Если указано имя конкретного, то отдает только его значение.
    """
    up = urlparse(url)
    qs = parse_qs(up.query)
    if param_name:
        return qs[param_name]
    return qs


url_ = 'https://google.ru/v2/categories?category=qwerty&genre=well&year=2010'
category = get_query_params(url_, 'category')
genre = get_query_params(url_, 'genre')
print(category)  # qwerty
print(genre)  # well
print(parse_qs(url_))
print(urlparse(url_))
url_parse = urlparse(url_)
parse__qs = parse_qs(url_parse.query)
print(parse__qs)