# pypi: https://pypi.org/project/urlextract/
from urlextract import URLExtract

extractor = URLExtract()
urls = extractor.find_urls("Text with URLs. Let's have URL janlipovsky.cz as an example.")
print(urls)  # ['janlipovsky.cz']


example_text = "Text with URLs. Let's have URL janlipovsky.cz as an example."
for url in extractor.gen_urls(example_text):
    print(url)  # 'janlipovsky.cz'

if extractor.has_urls(example_text):
    print("Given text contains some URL")