# 1) КАК ВЫГЛЯДИТ В ФАЙЛЕ. ПРИМЕР №1
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
# Внимание!! Если есть тег, в нем атрибут, а текста внутри тега нет, то можно не писать отдельно закрывающий тег,
# а все уместить в одном теге. Пример: <t a='2'/>


# 2) КАК ВЫГЛЯДИТ В ФАЙЛЕ. ПРИМЕР №2
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
