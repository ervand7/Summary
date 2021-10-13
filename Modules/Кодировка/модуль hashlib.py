import hashlib

h = hashlib.sha1(b"password")
h.update(b"password_continuation")
print(h.digest())
print(h.hexdigest())

# еще в питоне есть такое встроенное хеширование
print("password".__hash__())

# Использование md5, encode() и b
md5 = hashlib.md5("password".encode()).digest()
# или
md5_2 = hashlib.md5(b"password").digest()
print(md5)
print(md5_2)
