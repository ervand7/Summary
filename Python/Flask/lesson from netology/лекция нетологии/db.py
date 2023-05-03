import hashlib


def get_hash(password: str):
    return hashlib.md5(password.encode()).hexdigest()


def get_password(login):
    return get_hash('такой_то_пароль')  # хеш будет примерно таким: '6746fb9ebaa3e3e3b73baa0f9f856533'
