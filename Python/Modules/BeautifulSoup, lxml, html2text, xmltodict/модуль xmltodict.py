from pprint import pprint

import requests
import xmltodict

url = "https://www.w3schools.com/xml/plant_catalog.xml"
response = requests.get(url)
data = xmltodict.parse(response.content)
pprint(data['CATALOG'])
