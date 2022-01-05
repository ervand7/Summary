# Сервисы, которыми мы пользовались во время урока:
# ● httpbin - все про http-методы. http://httpbin.org/#/HTTP_Methods

# ● https://http.cat/ - все коды ответов отображены в виде котиков

# ● urlencoder - конвертер в url-формат
# https://www.urlencoder.org/

# ● Документация по установке витруального окружения https://docs.python.org/3/library/venv.html

# ● reddit.com - аналог русского Пикабу. Здесь мы брали гифки
# https://www.reddit.com/r/gifs/

# ● https://www.reddit.com/dev/api - api реддита

# ● https://pypi.org - каталог библиотек питона

# ● Документации по библиотеке requests:
# https://pypi.org/project/requests/
# https://requests.readthedocs.io/en/master/user/quickstart/
#________________________________________________________


# |||||||||||||||| HTTP методы |||||||||||||||||||||
# ● GET - используется для получения данных
# ● HEAD - делает то же самое, что и GET, но не получает тело (то есть, сервер в ответ не вкладывает тело ответа, а отправляет заголовки)

# ● POST - для отправки данных, для создания новых объектов. Если несколько раз посылать один и тот же запрос с методом POST, то можно создать дублирующиеся объекты

# ● PATCH - для изменение каких-то конкретных делатей. Можно безопасно несколько раз отправлять один и тот же запрос PATCH, и дублирующихся объектов не будет
# ● PUT - для изменения всех данных. Можно безопасно несколько раз отправлять один и тот же запрос PUT, и дублирующихся объектов не будет

# ● DELETE - для удаления
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# ///////////////////////////////////////////////////////////////////
# |||||||||||||||| HTTP коды |||||||||||||||||||||
# Первая цифра обозначает семантику кода.
# ● 1XX — Информационные
# ● 2XX — Успешный вызов (пример: 200 – ок, 201 – создано)
# ● 3XX — Перенаправление
# ● 4XX — Ошибка на стороне клиента (пример: 404 – не найдено, 403 – недостаточно прав) 
# ● 5XX — Ошибка на стороне сервера
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# ///////////////////////////////////////////////////////////////////
# ||||||||||||||||| Creation of virtual environments |||||||||||||||||
# Все это нужно делать через ТЕРМИНАЛ
# https://docs.python.org/3/library/venv.html - ссылка на документацию

# Открываем ТЕРМИНАЛ и вводим комманды
# ● mkdir netology_http_example - создаем папку
# ● cd netology_http_example/ - переходим в нее
# ● python3 -m venv .env - говорим терминалу, что с помощью модуля venv (который создает виртуальное окружение) создай новое виртуальное окружение в папке .env
# ● ls -la - так просматриваем сисок файлов. В одном из них и будет наш питон (копия)
# ● ls -l .env/bin/ - смотрим, что лежит в bin (после ввода этой комманды мы увидим путь, где лежит питон)
# ● source .env/bin/activate - активируем питон
# ● python -m venv .env^C - я не знаю зачем, но учитель эту команду потом вводит
# ● python - далее включаем python в интеррактивном режиме, проверяем, есть ли там нужный нам реквест или нет. Потом выходим с помощью exit() (ВЕСЬ ЭТОТ ШАГ ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО)
# ●  мы сейчас находимся в папке .env. Тут мы скачиваем реквест коммандой pip install requests (ну или все, что угодно с сайта https://pypi.org/)
# ●  python - заходим снова в питон
# ●  import requests - уже можем спокойно импортировать

# Далее, уже в PyCharm нужно выбрать правильный virtual environments
# Заходим в Preferences - Project: netology_http_example - python interpreter - шестеренку в правом верхнем углу - add - Existing environment и выбираем
# ///////////////////////////////////////////////////////////////////
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# ///////////////////////////////////////////////////////////////////
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# ///////////////////////////////////////////////////////////////////
# ||||||||||||||||ПЕРЕХОДИМ К ПРАКТИКЕ|||||||||||||||||||||
import requests
from pprint import pprint
import os
import tqdm # Этот модуль рисует прогресс бар

# response = requests.get("https://www.reddit.com/r/gifs.json") # Тут вконце мы приписываем .json, чтобы получать данные в формате json
# print(response) # <Response [429]> 
# # # Если мы получаем не 200 или 201 или 204, значит дело плохо и нужно разбираться
# print(response.status_code) # 429
# print(response.text) # Пусть текст нам скажет, в чем причина. {"message": "Too Many Requests", "error": 429}



# Тут можно сразу обозначить атрибуты и методы объекта Response:
# ● status_code – HTTP-статус ответа
# ● headers – заголовки ответа
# ● content – содержимое ответа в байтах
# ● text – содержимое ответа в текстовом представлении (utf8, так как все строки в Python – юникодные)
# ● json() – представление ответа в виде словаря. Работает только в том случае, если сервер вернул валидный JSON. Используется при работе с API.

# Параметры запроса и заголовки
# Чтобы передать параметры и заголовки в запросе, используйте именованные аргументы (пример кода):
# import requests
# url = "https://httpbin.org/get
# params = {"foo": "bar", "message": "hello"}
# headers = {"Authorization": "secret-token-123"}
# resp = requests.get(url, params=params, headers=headers)
# Важно: конкретные значения параметров и заголовков зависят от сервера, к которому происходит обращение. Для того чтобы узнать точные значения параметров, нужно читать документацию или проверять опытным путем.
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# ///////////////////////////////////////////////////////////////////
# # Посмотрим, вообще какие заголовки кладет библиотека реквест в запрос
# response = requests.get("https://httpbin.org/get")
# print(response.status_code)
# print(response.text) # помимо всего прочего мы видим "User-Agent": "python-requests/2.24.0". Отсюда и ошибка, так как reddit в принципе не любит программы, написанные на питоне
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# ///////////////////////////////////////////////////////////////////
# # Поэтому мы переписываем "User-Agent" с "python-requests/2.24.0" на "Netology" (или любое другое слово). Заголовки можно передавать с помощью именнованного аргумента headers. Он передает словарь
# response = requests.get("https://www.reddit.com/r/gifs.json", headers={"User-Agent": "Netology"})
# print(response.status_code)
# print(response.text) # Все ок, но это трудночитаемый текст
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# ///////////////////////////////////////////////////////////////////
# # Поэтому нам эта информация нужна в виде json. Чтобы получить json из этого ответа, нужно использовать response.json()
# response = requests.get("https://www.reddit.com/r/gifs.json", headers={"User-Agent": "Netology"})
# data = response.json()
# pprint(data)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# ///////////////////////////////////////////////////////////////////
# # Теперь из этого json нам нужно получить нужные нам данные. Пробуем добраться до "children"
# response = requests.get("https://www.reddit.com/r/gifs.json", headers={"User-Agent": "Netology"})
# data = response.json()["data"]["children"]
# pprint(data)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# ///////////////////////////////////////////////////////////////////
# # Теперь обходим этот список по постам
# # Внимание! Тут переменную data я переименовал на a, так как в json далее будет своя data. Чтоб не путаться
# response = requests.get("https://www.reddit.com/r/gifs.json", headers={"User-Agent": "Netology"})
# a = response.json()["data"]["children"]

# for post in a:
#   print(post["data"]["title"]) 

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# ///////////////////////////////////////////////////////////////////
# # Теперь мы хотим к себе на комп скачать гифки с reddit.com
# # Для начала мы ищем в словаре data адрес на какую-нибудь гифку
# # На reddit.com юзеры загружают свои посты через внешние хостинги. Мы поняли, что url этих хостов идут под ключом "url"
# response = requests.get("https://www.reddit.com/r/gifs.json", headers={"User-Agent": "Netology"})
# a = response.json()["data"]["children"]

# for post in a:
#   d = post["data"]
#   print(d["title"], d["url"]) 
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# ///////////////////////////////////////////////////////////////////
# # Видим среди многих прочих хостов хост под названием imgur
# # Мы хотим получать данные, загруженные именно с imgur.com
# # Поэтому итерируемся именно таким образом, чтобы в консоли выводились только url, содержащие "imgur.com"
# response = requests.get("https://www.reddit.com/r/gifs.json", headers={"User-Agent": "Netology"})
# a = response.json()["data"]["children"]

# for post in a:
#   data = post["data"]
#   url = data["url"] # для удобства url преобразуем в отдельную переменную

#   if "imgur.com" not in url:
#     continue # continue пропускает итерации, в которых нет "imgur.com"
#   print(data["title"], url)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# ///////////////////////////////////////////////////////////////////
# # Внимание!  Это мое личное изобретение. Чтобы из всего нам попалась только та итерация, где url заканчивается на .gif
# response = requests.get("https://www.reddit.com/r/gifs.json", headers={"User-Agent": "Netology"})
# a = response.json()["data"]["children"]

# for post in a:
#   data = post["data"]
#   url = data["url"]
#   s = str(url)

#   if "imgur.com" not in url:
#         continue
#   elif ".gifv" in url:
#         continue
#   print(data["title"], url)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# ///////////////////////////////////////////////////////////////////
# # Теперь мы хотим концовки всех url изменить с .gifv на .gif. Этот лайфхак нам рассказал учитель. .gifv - это не совсем гифка. Это обертака вокруг гифки. Это html-документ, внутри еоторого где-то вставлена гифка. И чтобы нам из нее получить гифку, в url нужно просто удалить последнюю букву v. Ну а в коде мы просто переименовываем все url из ".gifv" в ".gif" методом .replace
# response = requests.get("https://www.reddit.com/r/gifs.json", headers={"User-Agent": "Netology"})
# a = response.json()["data"]["children"]

# for post in a:
#   data = post["data"]
#   url = data["url"]

#   if "imgur.com" not in url:
#     continue 
#   url = url.replace(".gifv", ".gif")
#   print(data["title"], url)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# ///////////////////////////////////////////////////////////////////
# # Теперь все эти файлы мы хотим отправить запрос на скачивание гифок. Для этого:
# # 1) импортируем os
# # 2) создаем директорию, куда будем скачивать все файлы
# # 3) создаем константу, которая будет равна путю к нашей папке
# # 4) отправляем запрос на адрес url. Это мы делаем в самом конце кода. И это еще раз сохраняем в response. Получается: response = requests.get(url)
# # 5) печатаем url и статус ответа через response.status_code
# GIFS_FOLDER = "gifs_3"
# response = requests.get("https://www.reddit.com/r/gifs.json", headers={"User-Agent": "Netology"})
# a = response.json()["data"]["children"]
# for post in a:
#   data = post["data"]
#   url = data["url"]

#   if "imgur.com" not in url:
#     continue
#   url = url.replace(".gifv", ".gif")
#   response = requests.get(url)
#   print(url, response.status_code)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# ///////////////////////////////////////////////////////////////////
# # Теперь попробуем все эти гифки сохранить к себе в папку gifs_3
# # Внимание!!! В репле этот код работает только если так: with open('gifs_3', 'wb') as f:      !!! Нижеприведенный код работает только в PyCharm
# # 1) Открываем с таким путем и записываем только в бинарном режиме:  with open(os.path.join(GIFS_FOLDER, title + ".gif"), 'wb') as f:
# # 2) Вытаскиваем данные методом content он возвращает не текст, а байты: f.write(response.content)
# GIFS_FOLDER = "gifs_3"
# response = requests.get("https://www.reddit.com/r/gifs.json", headers={"User-Agent": "Netology"})
# a = response.json()["data"]["children"]
# for post in a:
#   data = post["data"]
#   url = data["url"]
#   title = data["title"] # Сейчас и для заголовка создаем отдельную переменную, чтобо при принте удобнее было использовать

#   if "imgur.com" not in url:
#     continue
#   url = url.replace(".gifv", ".gif")

#   response = requests.get(url)
#   # with open('gifs_3', 'wb') as f: # это только для репла
#   with open(os.path.join(GIFS_FOLDER, title + ".gif"), 'wb') as f:
#     f.write(response.content)
#   print(title, "Done!")
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# ///////////////////////////////////////////////////////////////////
# ||||||||||||||||Разберем нашу программу на части|||||||||||||||||||||
# Создаем константу, равную пути к нашей папке, в которую все потом сохраним
# GIFS_FOLDER = "gifs_3"

# # Обращаемся к API reddit и получаем посты
# response = requests.get("https://www.reddit.com/r/gifs.json", headers={"User-Agent": "Netology"})
# a = response.json()["data"]["children"]

# # Для этого в цикле мы обходим посты
# for post in a:
#   data = post["data"]
#   url = data["url"]
#   title = data["title"]

# # Выбираем только те, которые находятся на imgur.com
#   if "imgur.com" not in url:
#     continue

# # Чиним адрес    
#   url = url.replace(".gifv", ".gif")

# # Скачиваем гифку
#   response = requests.get(url)

# # Сохраняем ее в файл  
#   with open(os.path.join(GIFS_FOLDER, title + ".gif"), 'wb') as f:
#     f.write(response.content)

# # И печтаем просто, чтобы после успешного скачивания каждого файла он писал:
#   print(title, "Done!")
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# ///////////////////////////////////////////////////////////////////
# # Теперь попробуем все то же самое сделать с tqdm. Выше мы уже импортировали tqdm
# GIFS_FOLDER = "gifs_3"
# response = requests.get("https://www.reddit.com/r/gifs.json", headers={"User-Agent": "Netology"})
# a = response.json()["data"]["children"]
# for post in tqdm.tqdm(a): # для этого просто в цикле переменную a заворачиваем в tqdm.tqdm
#   data = post["data"]
#   url = data["url"]
#   title = data["title"]

#   if "imgur.com" not in url:
#     continue
#   url = url.replace(".gifv", ".gif")

#   response = requests.get(url)
# #  # with open('gifs_3', 'wb') as f: # это только для репла
#   with open(os.path.join(GIFS_FOLDER, title + ".gif"), 'wb') as f:
#     f.write(response.content)
#   print(title, "Done!")