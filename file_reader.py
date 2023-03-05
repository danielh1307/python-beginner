import my_json

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())  # rstrip removes the empty line at the end

with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(f"This is a line: {line.rstrip()}")

with open('pi_digits.txt') as file_object:
    # Save the contents of the file in a variable to access it outside the with block
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming")

numbers = [2, 3, 5, 7, 11, 13]
d = {
    "a": "b",
    "c": "d"
}
filename = 'numbers.json'
with open(filename, 'w') as f:
    my_json.dump(numbers, f)

with open('my_json.json', 'w') as f:
    my_json.dump(d, f)

with open(filename) as f:
    n_numbers = my_json.load(f)

print(n_numbers)