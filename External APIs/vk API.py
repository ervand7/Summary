# https://vk.com/dev - документация вк
# Implicit flow - самый легкий способ получения ключа доступа по OAuth 2.0:
# Его мы и будем использовать в лекции
# ПОШАГОВАЯ ИНСТРУКЦИЯ ПО ЛЕКЦИИ ||||||||||||||||||||||||||||||||||||
# 1) Входим в VK
# 2) Создаем приложение (тип standalone)
# 3) Переходим в Настройки и запоминаем «ID приложения» (app_id). В данном случае прописываем как APP_ID = 7649081
# 4) Формируем ссылку для запроса прав
# 5) Переходим по этой ссылке и разрешаем нашему приложению доступ к нашей информации

#  На всех сайтах процесс примерно такой:
# 1. Аутентификация
# 2. Получение токена
# 3. Авторизация с токеном

# ------------------------ ПИШЕМ КОД ------------------------
import requests
from urllib.parse import urlencode, urljoin
# Вот ссылка на то, что делает urlencode:
# https://www.urlencoder.io/python/#:~:text=urlencode()%20function.,%3E%3E%3E%20import%20urllib.


# Здесь мы заполняем параметры для запроса токена ||||||||||||||||||||||
# Список этих параметров указан здесь https://vk.com/dev/oauth_dialog
# Вот такой вот пример запроса показывает нам вк:
# https://oauth.vk.com/authorize?
# client_id=1&redirect_uri=http://example.com/callback&scope=12&display=mobile
# Это у нас и должно получиться в итоге. Все, что мы сейчас будем делать, мы делаем
# для получение url, внутри которого будет содержаться токен

# ● Для того, чтобы авторизовать пользователя, необходимо перенаправить его браузер
# по адресу https://oauth.vk.com/authorize, передав следующие параметры:
oauth_api_base_url = 'https://oauth.vk.com/authorize'

# ● идентификатор Вашего приложения
APP_ID = 7649081

# ● redirect_uri - это адрес, на который будет переадресован пользователь после прохождения
# авторизации (домен указанного адреса должен соответствовать основному домену в настройках приложения).
# Если Вы разрабатываете Standalone-приложение и параметр response_type = "token",
# то в качестве параметра redirect_uri необходимо указывать
# адрес https://oauth.vk.com/blank.html, на который будут переданы данные авторизации.
# Обратите внимание, что только в данном случае у Вас будет возможность
# использовать расширенные методы работы с API.
redirect_uri = 'https://oauth.vk.com/blank.html'

# ● scope - это Битовая маска настроек доступа приложения, которые необходимо проверить при
# авторизации пользователя и запросить, в случае отсутствия необходимых.
# В данном случае в качестве параметра scope нас интересует статус в вк
scope = 'status'

# ТЕПЕРЬ ОБЪЕДИНЯЕМ ЭТО ВСЕ В СЛОВАРЬ
oauth_params = {
    'redirect_uri': redirect_uri,
    'scope': scope,
    'response_type': 'token', # пишем, что в качестве ответа нам нужен токен. См стр. 40
    'client_id': APP_ID
}
# теперь соединяем oauth_api_base_url с нашим словарем oauth_params,
# и пишем, что их нужно соединить знаком '?', и при этом используем к словарю urlencode,
# чтобы закодировать его в стиле URL-кода
print('?'.join([oauth_api_base_url, urlencode(oauth_params)]))
# Теперь, чтобы получить нужный нам токен, мы открываем новую вкладку в браузереБ
# вставляем URL, который нам вышенаписанный код выдал, нажимаем enter, и из полученного нового URL
# вынимаем токен. В данном случае
# token=fd283f82f029b490ebfa7f016884c76793521866d854022b72fa710cf0b7f5aa784b32e79b90944aaced1
#/////////////////////////////////////////////////////////




#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# # Теперь идем смотреть, какие методы у нас ксть в API вк. Вот ссылка https://vk.com/dev/methods
# # Сейчас мы с нашим токеном хотим посмотреть, какой у моей стр в вк текущий статус.
# # Для этого мы импортируем api_requests и идем смотреть документацию вк к запросам https://vk.com/dev/api_requests
# # В общем, вк от нас требует формирования с таким
# # смыслом https://api.vk.com/method/METHOD_NAME?PARAMETERS&access_token=ACCESS_TOKEN&v=V
#
# import requests
# from urllib.parse import urlencode, urljoin
#
#
# TOKEN = 'fd283f82f029b490ebfa7f016884c76793521866d854022b72fa710cf0b7f5aa784b32e79b90944aaced1'
# API_BASE_URL = 'https://api.vk.com/method/'
# V = '5.21'
#
# status_get_url = urljoin(API_BASE_URL, 'status.get') # 'status.get' - название метода (из документации вк)
# print(status_get_url)
# response = requests.get(status_get_url, params={
#     'access_token': TOKEN,
#     'v': V
# })
# print(response.json())
#/////////////////////////////////////////////////////////





#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# # Теперь мы хотим применить метод set и изменить статус в вк
#
# import requests
# from urllib.parse import urlencode, urljoin
#
#
# TOKEN = 'c2a7617a75513e32d539eda42fd1843d561b5d2bc23a2530860c5da9b7646e6e1a250077b30d552311f3c'
# API_BASE_URL = 'https://api.vk.com/method/'
# V = '5.21'
# status_get_url = urljoin(API_BASE_URL, 'status.set')
# # print(status_get_url)
# response = requests.get(status_get_url, params={
#     'access_token': TOKEN,
#     'v': V,
#     'text': 'ибо где сокровище ваше, там будет и сердце ваше.'
# })
# print(response.json())
#/////////////////////////////////////////////////////////





#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# # Теперь поработаем с классами. Обернем все вышенаписанное в класс
# # Попытаемся получить мой статус в вк
# import requests
# from urllib.parse import urlencode, urljoin
#
#
# TOKEN = 'c2a7617a75513e32d539eda42fd1843d561b5d2bc23a2530860c5da9b7646e6e1a250077b30d552311f3c'
# API_BASE_URL = 'https://api.vk.com/method/'
# V = '5.21'
#
# class VKApiClient:
#
#     def __init__(self, token=TOKEN, version=V):
#         self.token = token
#         self.version = version
#
#     def get_user_status(self):
#         status_get_url = urljoin(API_BASE_URL, 'status.get')
#         res = requests.get(status_get_url, params={
#             'access_token': self.token,
#             'v': self.version
#         })
#         return res.json()['response']['text']
#
# if __name__ == '__main__':
#     a = VKApiClient()
#     print(a.get_user_status())
#/////////////////////////////////////////////////////////





#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# # Теперь попробуем внеси изменения в статус в вк
# import requests
# from urllib.parse import urlencode, urljoin


# TOKEN = 'c2a7617a75513e32d539eda42fd1843d561b5d2bc23a2530860c5da9b7646e6e1a250077b30d552311f3c'
# API_BASE_URL = 'https://api.vk.com/method/'
# V = '5.21'

# class VKApiClient:
#     BASE_URL = API_BASE_URL

#     # мы создаем такую дополнительную функцию, чтобы в дальнейшем избежать написания этой
#     # строки: status_get_url = urljoin(API_BASE_URL, 'status.get')
#     def __create_method_url(self, method):
#         return urljoin(self.BASE_URL, method)

#     def __init__(self, token=TOKEN, version=V):
#         self.token = token
#         self.version = version

#     def get_user_status(self):
#         res = requests.get(self.__create_method_url('status.get'), params={
#             'access_token': self.token,
#             'v': self.version
#         })
#         return res.json()['response']['text']

#     def set_user_status(self, text):
#         requests.get(self.__create_method_url('status.set'), params={
#             'access_token': self.token,
#             'v': self.version,
#             'text': text
#         })

# if __name__ == '__main__':
#     a = VKApiClient()
#     my_status = a.get_user_status()
#     if 'ибо' in my_status:
#         a.set_user_status(my_status + '.')