import collections  # From Python standard library.
import bson
from bson.codec_options import CodecOptions


# про ObjectId
def what_bson_type(input_):
    return bson._ELEMENT_GETTER[bson.BSON.encode({"t": input_})[4]].__name__[5:]


print(what_bson_type(9.8))  # float
print(bson.ObjectId(b'foo-bar-quux'))  # 666f6f2d6261722d71757578

print('________________________________________________________')
# про кодировки-раскодировки
# 1й вариант

data = bson.BSON.encode({'a': 1})
print(data)

decoded = bson.BSON(data).decode()  # <type 'dict'>
print(decoded)

options = CodecOptions(document_class=collections.OrderedDict)
decoded_2 = bson.BSON(data).decode(codec_options=options)
print(decoded_2)

print(type(decoded_2))  # <class 'collections.OrderedDict'>

print('________________________________________________________')
# 2й вариант

d = bson.encode({'a': 1})
print(d)
decoded_ = bson.decode(d)
print(decoded_)
options = CodecOptions(document_class=collections.OrderedDict)
decoded_doc = bson.decode(d, codec_options=options)
print(decoded_doc)
