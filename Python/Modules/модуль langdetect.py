# https://pypi.org/project/langdetect/
# pip install langdetect

from langdetect import detect

print(detect("War doesn't show who's right, just who's left."))  # 'en'
print(detect("Ein, zwei, drei, vier"))  # 'de'

