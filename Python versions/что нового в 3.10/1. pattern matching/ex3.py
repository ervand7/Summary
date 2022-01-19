# 3.10
def run_action(user_input: list) -> None:
    match user_input:
        case 'left', value if int(value) > 50:
            print('something.......')
        case 'left' | 'right' | 'top' | 'bottom' as action, value:
            print(f'Go to {action} to {value}px')
        case 'shoot', *coords:
            print(f'Shoot by coords: {coords}')
        case ('quit', ):
            print('bye')
        case _:
            print('wrong command')


run_action('left 100'.split())  # Go to left to 100px
run_action('bottom 333'.split())  # Go to bottom to 333px
run_action('qwerty 333'.split())  # wrong command
run_action('quit'.split())  # bye
run_action('left 1000'.split())  # something.......
