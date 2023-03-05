def get_user_input():
    while True:
        user_input = input('What is your favourite number?')
        try:
            int(user_input)
        except ValueError:
            print('No, please enter a number')
        else:
            write_favourite_number_to_file(user_input)
            return int(user_input)


def write_favourite_number_to_file(user_input):
    with open('favourite_number.txt', 'w') as f:
        f.write(user_input)


def load_favourite_number_from_file():
    try:
        with open('favourite_number.txt') as f:
            return f.read()
    except FileNotFoundError:
        return None


f_number = load_favourite_number_from_file()
if not f_number:
    f_number = get_user_input()
print(f"I know your favourite number, it is {f_number}")
