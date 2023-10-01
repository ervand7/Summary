# 3.10
class UserInput:
    # задаем эту переменную, чтобы в case можно было прописывать их не как именованные,
    # а как позиционные аргументы
    __match_args__ = ('action', 'value')

    def __init__(self, action: str, value: int):
        print('__init__ called')
        self.action = action
        self.value = value


def run(user_input: UserInput | dict):
    match user_input:
        # фишка pattern matching в данном примере в том, что для проверки
        # этого условия не будет создаваться отдельный экземпляр класса UserInput
        # а будет проверяться только паттерн. Это мы можем вычислить благодаря print('__init__ called').
        # Также, то, что тут идет не вызов конструктора, мы можем понять, если передадим
        # в case не все требуемые обязательные аргументы класса, например:
        # case UserInput(action='left' | 'right'):
        # И никакой ошибки не будет, паттерн отработает.
        case UserInput(action='left' | 'right', value=value):
            print(f'Moving horizontally on {value} px')
        case {'action': 'left' | 'right', 'value': value}:
            print(f'Moving horizontally on {value} px')
        # благодаря __match_args__ приписываем аргументы как позиционные
        case UserInput('влево' | 'вправо', value):
            print(f'Перемещение по горизонтали на {value} px')
        case _:
            print('Error')


run(UserInput('left', 150))  # Moving horizontally on 150 px
run({'action': 'right', 'value': 300})  # Moving horizontally on 300 px
run(UserInput('top', 20))  # Error
run(UserInput('вправо', 151))  # Перемещение по горизонтали на 151 px
