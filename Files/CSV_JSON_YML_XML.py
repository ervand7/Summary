# Формат CSV
# CSV - единственный формат из всех, который поддерживат флаг append


# КОМАНДЫ ДЛЯ РАБОТЫ С CSV ||||||||||||||||||
# Десериализация в список:
# reader = csv.reader(file) # reader - это объект
# data = list(reader) # это для маленьких данных. Минус в том, что нужно знать, на какой конкретной позиции находится каждый элемент
# Десериализация в словарь: # Этот вариант проще и лучше
# reader = csv.DictReader(file)
# Сериализация:
# writer = csv.writer(file)
# writer.writerows(data) # Сюда сразу список помещать нужно. Точнее, список списков
# writer.writerow(data) # Сюда добавляем построчно


# Настройки форматирования ||||||||||||||||||
# csv.register_dialect()
# Настройки форматирования через csv.register_dialect()
# delimiter=“,”
# quoting=csv.QUOTE_MINIMAL (QUOTE_ALL, QUOTE_NONNUMERIC, QUOTE_NONE)
# quotechar='“’
# escapechar='\\'


# # Формат CSV: Десериализация и сериализация ||||||||||||||||||
# ПРИМЕР КОДА:
# import csv
# csv.register_dialect("customcsv", delimiter=",", quoting=csv.QUOTE_NONE, quotechar="`", escapechar="\\")
# with open("files/sample.csv", 'w', encoding='utf-8') as f:
# 	writer = csv.writer(f, 'custom.csv')
#   writer.writerows(data2)


# with open("files/sample.csv", newline='') as f:
#   reader = csv.reader(f)
#   print(list(reader))


# with open("files/sample.csv", newline='') as f:
#   reader = csv.DictReader(f)
#   for row in reader:
#     print(row['title'])


# ДОПОЛНИТЕЛЬНО, ПРИМЕР КОДА с https://www.youtube.com/watch?v=3lpqHCvHOAk&t=232s
# import csv
# with open("fio_salary_kpi.csv", newline = '') as csvfile:
#     reader = csv.DictReader(csvfile,delimiter=";")
#     for row in reader:
#         print(row['full_name'],'|',row['salary'],row['kpi'])
# with open("new_file.csv", 'w', newline = '') as csvfile:
#     writer = csv.writer(csvfile, delimiter=";")
#     writer.writerow(["row 1 el 1","row 1 el 2","row 1 el 3"])
#     writer.writerow(["row 2 el 1","row 2 el 2","row 2 el 3"])
#     writer.writerow(["row 3 el 1","row 3 el 2","row 3 el 3"])
#/////////////////////////////////////////////////////////////////////



# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Формат JSON 

# КОМАНДЫ ДЛЯ РАБОТЫ С JSON ||||||||||||||||||
# Десериализация:
# Из файла: json.load(file) # - даем файл в качестве параметра
# Из строки: json.loads(str) # - даем строку в качестве параметра
# Сериализация:
# В файл: json.dump() # - сохраняем в файл
# В строку: json.dumps() # - сохраняем в строку
# Печать не-ascii символов, отступы:
# ensure_ascii=False, indent=2 
# - обязательно, если работаем с кириллицей, задаем параметр ensure_ascii=False, иначе все буквы превратятся в цифры. А indent=2 - это красивые отступы, если их не использовать, то будет одна бесконечная строка


# # ПРИМЕР КОДА ||||||||||||||||||
# import json
# from pprint import pprint
# data = {'channel': {'title': 'Дайджест новостей о python',
#               'link': 'https://pythonigest.ru/'}}
# with open('files/sample.json', 'w') as f: # ТОЛЬКО ФЛАГ 'w'!!!!!
#   json.dump(data, f, ensure_ascii=False, indent=2)

# with open('files/sample.json', encoding='utf-8') as f:
#   data = json.load(f)
#   pprint(data)
#/////////////////////////////////////////////////////////////////////



# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Формат YAML - встречается редко, в основном в API. В обращении аналогичен формату JSON


# КОМАНДЫ ДЛЯ РАБОТЫ С YAML ||||||||||||||||||
# Десериализация:
# Из файла: yaml.load(file)
# Из строки: yaml.loads(str) 
# Сериализация:
# В файл: yaml.dump
# В строку: yaml.dumps
#  Печать не-ascii символов, отступы:
# allow_unicode=True, default_flow_style=False 
# чтобы с кириллицей все было хорошо, нужно прописать allow_unicode=True. Чтобы получить отступы, нужно использовать флаг default_flow_style=False. Размер отступа назначить нельзя. Тут отступ можно только включить либо выключить


# # ПРИМЕР КОДА:
# import yaml
# from pprint import pprint
# data = {'channel': {'title': 'Дайджест новостей о python',
#               'linf': 'https://pythonigest.ru/'}}
# with open('files/sample.json', 'w') as f: # ТОЛЬКО ФЛАГ 'w'!!!!!
#   yaml.dump(data, f, allow_unicode=True, default_flow_style=False)

# with open('files/sample.json', encoding='utf-8') as f:
#   data = yaml.load(f, Loader=yaml.FullLoader) # это требование обновленной библиотеки
#   pprint(data)
#/////////////////////////////////////////////////////////////////////



# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Формат XML

# 1) КАК ВЫГЛЯДИТ В ФАЙЛЕ. ПРИМЕР №1 (это не код!!!!) ||||||||||||||||||
# <rss xmlns:ns0='http://www.w3.org/2005/Atom', version='2.0'>
# <channel>
#   <title>Дайджест новостей о python</title>
#   <link>https://pythondigest.ru/</link>
#   <description>Русскоязычные анонсы свежх новостей о python и близлежащих технологиях.</description>
# </channel></rss>
# В ВЫШЕНАПИСАННОМ ФАЙЛЕ:
# Элемент - это: <title>Дайджест новостей о python</title>
# Тег - это: title
# Текст - это: Дайджест новостей о python
# Атрибут - это: version=“2.0”
# Внимание!! Если есть тег, в нем атрибут, а текста внутри тега нет, то можно не писать отдельно закрывающий тег, а все уместить в одном теге. Пример: <t a='2'/>


# 2) КАК ВЫГЛЯДИТ В ФАЙЛЕ. ПРИМЕР №2 (это не код!!!!)
# # Как что называется в XML |||||||||||||||||| 
# <?xml version='1.0' ?> # Это не корень. Это объявление xml. По этому тегу парсер орентируется, что перед ним XML
# <rss xmlns:ns0='http://www.w3.org/2005/Atom', version='2.0'> # Это корень (root)
# <channel>
#   <title>Дайджест новостей о python</title>
#   <link>https://pythondigest.ru/</link>
#   <description>Русскоязычные анонсы свежх новостей о python и близлежащих технологиях.</description>
#   <ns0:link href='https://pythondigest.ru/rss' rel='self'


#   КОМАНДЫ ДЛЯ РАБОТЫ С XML  ||||||||||||||||||
# импортируем xml.etree.ElementTree.parse()
# tree.getroot() # получить корень дерева. В итоге получаем:
# <rss xmlns:ns0="http://www.w3.org/2005/Atom" version="2.0">
# root.tag # узнаем имя тега
# root.text # узнаем текст внутри тега
# root.attrib # узнаем атрибуты тега
# tree.write() # сохраняем
# |||||XPath - это язык запросов, для нахождения конкретного запроса||||| 
# root.find(query) # - поиск первого элемента вхождения того, что мы запрашиваем. (query) - это имя тега, которого мы хотим получить
# root.findall(query) # - поиск нескольких элементов. Находит все

# Работа с элементами 
# root = tree.getroot() # получить корневой элемент дерева
# print(root.tag) # название тега (на примере корневого элемента)
# print(root.attrib) # получение атрибутов тега
# print(root.text) # текст внутри тега
# xml_title = root.find('channel/title') # поиск элемента с помощью xpath
# print(xml_title.text) # текст внутри тега
# xml_items = root.findall('channel/item') # поиск всех эл. с помощью xpath. Так мы можем писать составные запросы. Всю цепочку через /. findall будет относиться к самому последнему звену цепочку. Если мы уж используем findall, то все, что впереди последнего звена, должно быть в единственном экземпляре
# print(len(xml_items))
# for xmli in xml_items:
#   print(xmli.find('title').text)

# Сохранение ||||||||||||||||||
# 1) простое сохранение:
# tree.write('files/result.xml', encoding='utf-8')
# 2) сохранение с отступами:
# from xml.dom import minidom
# xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent='    ')
# with open('files/result_index.xml', 'w', encoding='utf-8') as f:
#   f.write(xmlstr)


#   Загрузка из файла и словаря ||||||||||||||||||
# 1) из файла:
# import xml.etree.ElementTree as ET
# parser = ET.XMLParser(encoding='utf-8') # создать объект парсера и указать верную кодировку
# tree = ET.parse('files/sample.xml', parser) # прочитать DOM-дерево документа
# root = tree.getroot() # получить корневой элемент дерева

# 2) из словаря:
# import dicttoxml # эту библиотеку придется устанавливать отдельно
# data = {'channel': {'title': 'Дайджест новостей о python', 
#               'limk': 'https://pythondigest.ru'}}
# xml = dicttoxml.dicttoxml(data)


