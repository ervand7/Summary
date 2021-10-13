# основная статья: https://codecamp.ru/blog/python-the-base64-module/
import base64

# Creating a string
row = "Hello World!"

# Encoding the string into bytes
encoded_row = row.encode("UTF-8")
print(f'1 {encoded_row}')  # b'Hello World!'

# Base64 Encode the bytes
encoded_row_64 = base64.b64encode(encoded_row)
print(f'2 {encoded_row_64}')  # b'SGVsbG8gV29ybGQh'

# Decoding the Base64 bytes to string
decoded_64 = encoded_row_64.decode("UTF-8")
print(f'3 {decoded_64}')  # SGVsbG8gV29ybGQh

# Encoding the Base64 encoded string into bytes
new_encoded_row_64 = decoded_64.encode("UTF-8")
print(f'4 {new_encoded_row_64}')  # b'SGVsbG8gV29ybGQh'

# Decoding the Base64 bytes
new_decoded_64 = base64.b64decode(new_encoded_row_64)
print(f'5 {new_decoded_64}')  # b'Hello World!'

# Decoding the bytes to string
s2 = new_decoded_64.decode("UTF-8")
print(f'6 {s2}')  # Hello World!
