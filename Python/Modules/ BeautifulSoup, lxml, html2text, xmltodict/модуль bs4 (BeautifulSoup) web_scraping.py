# Парсим https://2ip.ru
# вариант с requests и без BeautifulSoup
import requests
from bs4 import BeautifulSoup
from pprint import pprint

response = requests.get('https://2ip.ru')
# мы можем вычленить конкретные данные благодаря знанию, что у каждого тега может быть свой неповторимый id
# в данном случае здесть у тега div индивидуальный id="d_clip_button"
index_id = response.text.index('id="d_clip_button"')  # <div class="ip" id="d_clip_button" style="cursor: pointer;">
# <span>93.157.169.19</span><i class="ip-icon-shape btn-copy"></i></div>
# 1) ищем открывающий тег span с помощью методов text и index. Мы говорим программе найти бижайший тег
# <span>, начиная с index_id, который мы нашли на прошлой строке кода. То есть
# тут мы прописываем что искать ('<span>') и начиная с какой позиции (index_id).
index_span = response.text.index('<span>', index_id)  # index(self, sub, start=None, end=None) -

# 2) ищем закрывающий тег span:
index_span_end = response.text.index('</span>', index_id)
# print(response.text[index_span + 6:index_span_end])  # поскольку индекс будет возвращаться с самого начала
# строки '</span>', то мы должны пропустить эти символы именования тега
# ____________________________________________________


# ____________________________________________________
# Парсим https://2ip.ru
# вариант с requests + BeautifulSoup
response2 = requests.get('https://2ip.ru')
# формируем наше дерево с детьми
soup = BeautifulSoup(response2.text, 'html.parser')  # здесь response2.text - это HTML разметка
# по умолчанию в BeautifulSoup стоит html.parser, но мы все равно каждый раз должны его указывать
element = soup.find(id="d_clip_button")

# print(element.text.strip())  # а здесь element.text - это визуальный текст для каждого элемента
# ____________________________________________________


# ____________________________________________________
# Парсим https://habr.com/ru/ и ищем все статьи, в которых есть один из след хабов:
# 'devops', 'фото', 'laravel', 'криптография'.
# Нам нужно название, ссылка и дата выпуска
DESIRED_HUBS = ['devops', 'машинное обучение', 'laravel', 'криптография']
resp = requests.get('https://habr.com/ru/all')
soup2 = BeautifulSoup(resp.text, 'html.parser')

# извлекаем посты
# здесь будем использовать find_all, а не find, так как find возвращает нам только первое вхождение,
# а find_all будет нам возвращать все вхождения
# первым параметром мы указываем тег. Если не укажем, то он будет пытаться найти среди всех тегов
# Внимание! очень важно писать class_ - это требование библиотеки.
posts = soup2.find_all('article', class_='post')  # Вообще изначально тут class_='post post_preview', но
# мы можем прописать всего на всего первое слово (class_='post') и все будет работать
# pprint(posts)
for post in posts:
    # print(post)
    # теперь в рамках каждого поста нам нужно найти все хабы которые есть у этого поста
    # это у нас будут ссылки, которые находятся внутри тега <li> у которого class_='inline-list__item_hub'
    # опять же, полное название class_'inline-list__item inline-list__item_hub', но мы можем сократить
    # название до 'inline-list__item_hub'
    hubs = post.find_all('li', class_='inline-list__item_hub')
    # print(hubs)  # hubs в данном случае - это списки с хабами

    # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    # сейчас попробуем вывести только текстовые названия хабов (все с маленькой буквы),
    # это будут также списки с хабами.
    # Функция map делает преобразование для каждого элемента.
    # В данном случае функция берет элемент (x) и делает с ним x.text.strip().lower(), то есть извлекает
    # такст-название, избавляется от лишних пробелов и все переводит в нижний регистр. И все это происходит в hubs.
    # Мы все переводим в нижний регистр чтобы не париться с написанием хабов в DESIRED_HUBS, чтобы избежать
    # ошибок, связвнных с регистрами.
    hubs_text = list(map(lambda x: x.text.strip().lower(), hubs))
    # print(hubs_text)
    # # # с помощью map мы заменяем эти 4 строки кода:
    # hubs_text = []
    # for hub in hubs:
    #     hubs_text.append(hub.text.strip())
    # print(hubs_text)
    # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    for hub_text in hubs_text:
        # print(hub_text)
        # нам нужно, чтобы хотя бы один из этих хабов ('devops', 'фото', 'laravel', 'криптография')
        # присутствовал внутри списка hub_text
        # функция any проверяет, чтобы хотя бы один из элементов был истинным
        if any(one_hub in hubs_text for one_hub in DESIRED_HUBS):
            date = post.find('span', class_='post__time').text.strip()  # если мы раньше
            # использовали post.find_all(), то сейчас, поскольку нам нужно только первое вхождение,
            # мы уже будем использовать просто find()
            our_link = post.find('a', class_='post__title_link')
            our_link_link = our_link.attrs.get('href')
            our_link_text = our_link.text.strip()

            print(date, our_link_link, our_link_text)
            break  # если мы тут не поставим break, то, если у одной статьи будет несколько хабов, которые будут
            # присутствовать в DESIRED_HUBS, эта статья будет нам выводиться более одного раза. А именно
            # столько раз, сколько она имеет хабов, входящих в DESIRED_HUBS. А нам этого не надо. Нам нужно,
            # чтобы каждая статья выводилась всего по одному разу. То есть мы заканчиваем цикл, если мы нашли
            # хоть одно вхождение элементов из DESIRED_HUBS.
        # else:
        #     print('Таких хабов не обнаружено')
# ____________________________________________________


# ____________________________________________________
# Код с презентации
# # определяем список хабов, которые нам интересны
# DESIRED_HUBS = ['дизайн', 'фото', 'web', 'python']
# # получаем страницу с самыми свежими постами
# ret = requests.get('https://habr.com/ru/all/')
# soup = BeautifulSoup(ret.text, 'html.parser')
#
# # извлекаем посты
# posts = soup.find_all('article', class_='post')
# for post in posts:
#     post_id = post.parent.attrs.get('id')
#     # если идентификатор не найден, это что-то странное, пропускаем
#     if not post_id:
#         continue
#     post_id = int(post_id.split('_')[-1])
#     print('post', post_id)
#
#     # извлекаем хабы поста
#     hubs = post.find_all('a', class_='hub-link')
#     for hub in hubs:
#         hub_lower = hub.text.lower()
#         # ищем вхождение хотя бы одного желаемого хаба
#         if any([hub_lower in desired for desired in DESIRED_HUBS]):
#             title_element = post.find('a', class_='post__title_link')
#             print(title_element.text, title_element.attrs.get('href'))
#             break
