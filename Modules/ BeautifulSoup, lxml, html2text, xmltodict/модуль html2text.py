# информация взята отсюда: https://pypi.org/project/html2text/
# pip install html2text
import html2text

print(html2text.html2text(
    "<p><strong>Zed's</strong> dead baby, <em>Zed's</em> dead.</p>"))  # **Zed's** dead baby, _Zed's_ dead.


h = html2text.HTML2Text()
# Ignore converting links from HTML
h.ignore_links = True
print(h.handle("<p>Hello, <a href='https://www.google.com/earth/'>world</a>!"))  # Hello, world!


# Don't Ignore links anymore, I like links
h.ignore_links = False
print(h.handle(
    "<p>Hello, <a href='https://www.google.com/earth/'>world</a>!").strip())  # Hello, [world](https://www.google.com/earth/)!
