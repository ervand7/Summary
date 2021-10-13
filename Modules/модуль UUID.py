# основная статья: https://docs.python.org/3/library/uuid.html
import uuid

# make a UUID based on the host ID and current time
print(uuid.uuid1())

# make a UUID using an MD5 hash of a namespace UUID and a name
print(uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org'))

# make a random UUID
print(uuid.uuid4())

# make a UUID using a SHA-1 hash of a namespace UUID and a name
print(uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org'))

# make a UUID from a string of hex digits (braces and hyphens ignored)
x = uuid.UUID('{00010203-0405-0607-0809-0a0b0c0d0e0f}')
# convert a UUID to a string of hex digits in standard form
print(str(x))

# get the raw 16 bytes of the UUID
print(x.bytes)

# make a UUID from a 16-byte string
print(uuid.UUID(bytes=x.bytes))
