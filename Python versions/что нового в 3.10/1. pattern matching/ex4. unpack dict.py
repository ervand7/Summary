# 3.10
user_action = {
    'id': 123,
    'action': 'left',
    'action2': 50,
    'timestamp': 1010102121,
    'user_group': 11,
    'cache': 2_000_000
}

"""
Таким образом мы можем проверить, что: 
1) тип user_action словарь
2) что у него есть поля action, значение которого str и action2, значение которго int 
3) остальные поля мы проигнорируем

"""
match user_action:
    case {'action': str(something), 'action2': int(another_something)}:
        print(f'Все соответствует!')  # Все соответствует!
