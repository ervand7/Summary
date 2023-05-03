# https://pythonworld.ru/moduli/modul-pickle.html
import pickle

initial_data = {
    'a': [1, 2.0, 3, 4],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

# dump/load ___________________________________
with open(file='pickle_data', mode='wb') as f:
    pickle.dump(initial_data, f)

with open(file='pickle_data', mode='rb') as f:
    data_new = pickle.load(f)
    print(data_new)
    print(type(data_new))

# dumps/loads ___________________________________
byte_data = pickle.dumps(initial_data)  # b'\x80\x04\x95N\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x01a\x94]\x94(K\x01G@\x00\x00\x00\x00\x00\x00\x00K\x03K\x04e\x8c\x01b\x94\x8c\x10character string\x94C\x0bbyte string\x94\x86\x94\x8c\x01c\x94\x8f\x94(\x89N\x88\x90u.'
restored = pickle.loads(byte_data)
assert restored.__eq__(initial_data)

