# 3.10
class UserInput:
    # задаем эту переменную, чтобы в case можно было прописывать их не как именованные,
    # а как позиционные аргументы
    __match_args__ = ('action', 'value')

    def __init__(self, action: str, value: int):
        print('__init__ called')
        self.action = action
        self.value = value


def run_horizontally(user_input: UserInput | dict):
    match user_input:
        # фишка pattern matching в данном примере в том, что для проверки
        # этого условия не будет создаваться отдельный экземпляр класса UserInput
        # а будет проверяться только паттерн. Это мы можем вычислить благодаря print('__init__ called').
        # Также, что тут идет не вызов конструктора, мы можем понять, если передадим в case
        # не все требуемые обязательные атрументы класса, например:
        # case UserInput(action='left' | 'right'):
        # И никакой ошибки не будет6 паттерн отработает.
        case UserInput(action='left' | 'right', value=value):
            print(f'Moving horizontally on {value} px')
        case {'action': 'left' | 'right', 'value': value}:
            print(f'Moving horizontally on {value} px')
        # благодаря __match_args__ приписываем аргументы как позиционные
        case UserInput('влево' | 'вправо', value):
            print(f'Перемещение по горизонтали на {value} px')
        case _:
            print('Error')


input1 = UserInput('left', 150)
input2 = {'action': 'right', 'value': 300}
input3 = UserInput('top', 20)
input4 = UserInput('вправо', 151)

run_horizontally(input1)  # Moving horizontally on 150 px
run_horizontally(input2)  # Moving horizontally on 300 px
run_horizontally(input3)  # Error
run_horizontally(input4)  # Перемещение по горизонтали на 151 px
