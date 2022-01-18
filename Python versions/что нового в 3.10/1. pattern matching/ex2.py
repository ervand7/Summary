# 3.9
def run_action_old(user_input: list) -> None:
    if isinstance(user_input, list) and len(user_input) == 2:
        action, value = user_input
        print(f'{action=}, {value=}')
    else:
        print('wrong command')


run_action_old('go_left 100'.split())  # action='go_left', value='100'


# 3.10
def run_action(user_input: list) -> None:
    match user_input:
        case action, value:
            print(f'{action=}, {value=}')
        case 'shoot', *coords:
            print(f'Shoot by coords: {coords}')
        case _:
            print('wrong command')


run_action('shoot 100 200 500 1000'.split())  # Shoot by coords: ['100', '200', '500', '1000']
run_action('qwerty 100 200 500 1000'.split())  # wrong command
