a = bytes()
print(a)  # ''

a = bytes("hello", "utf-8")
print(a)  # b'hello'
print(type(a))  # <class 'bytes'>

a = "hello".encode()
print(a)  # b'hello'
print(type(a))  # <class 'bytes'>

a = b"hello".decode()
print(a)  # hello
print(type(a))  # <class 'str'>
