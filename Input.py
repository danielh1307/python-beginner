responses = {}
active = True

while active:
    next_question = ''
    name = input("What is your name? ")
    club = input("What is your favorite club? ")

    responses[name] = club

    while next_question != 'y' and next_question != 'n':
        next_question = input("Continue (y/n)? ")

    if (next_question == 'y'):
        continue
    else:
        break

for name, club in responses.items():
    print(f"The favourite club of {name} is {club}.")