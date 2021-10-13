# официальная документация: https://github.com/fate0/pychrome
import pychrome

# Устанавливаем соединение:
# sudo /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222


browser = pychrome.Browser(url="http://127.0.0.1:9222")
tab = browser.new_tab()


def request_will_be_sent(**kwargs):
    print("loading: %s" % kwargs.get('request').get('url'))


tab.set_listener("Network.requestWillBeSent", request_will_be_sent)
tab.start()
tab.call_method("Network.enable")
tab.call_method("Page.navigate", url="https://github.com/fate0/pychrome", _timeout=5)

tab.wait(50)
# в это время можем нажимать на кнопки, наводить мышкой на что-то кликабельное и смотреть, что происходит в консоли
# питона. Своего рода дебаг

tab.stop()
browser.close_tab(tab)




