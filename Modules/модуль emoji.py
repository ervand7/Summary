# понятная официальная документация: https://pypi.org/project/emoji/
import emoji

print(emoji.emojize('Python is :thumbs_up:'))  # 👍
print(emoji.emojize(":white_check_mark:", use_aliases=True))  # ✅
