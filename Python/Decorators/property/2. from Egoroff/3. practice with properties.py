from string import digits


class NewUser:
    def __init__(self, login, password):
        self._login = login
        self._password = password

    @property
    def password(self):
        print('getter called')
        return print(self._password)

    @password.setter
    def password(self, value):
        print('setter called')
        if not isinstance(value, str):
            raise TypeError('The password must be string')
        if len(value) < 4:
            raise ValueError("Minimum length is 4")
        if len(value) > 12:
            raise ValueError("Maximum length is 12")
        if not NewUser.is_include_number(value):
            raise ValueError("The password must contain minimum one number")
        self._password = value

    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False
