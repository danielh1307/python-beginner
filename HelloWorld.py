message = "Hello Python world"
print(message)

names = ["Bob", "Alice", "Zen"] # declare a list
for name in names: # loop through the list
    print(name)

print(names[-1]) # access last element of the list

names.append("Paddington") # appending an element to the end of a list
names.insert(1, "Monster") # adding an element to the list at a specific position
for name in names:
    print(name)

del names[0] # removing an element from a sepcific position
popped_name_end = names.pop() # removing an element and store it to a variable
popped_name_beginning = names.pop(0) # removing from a specific position
print("Popped name from the end: " + popped_name_end)
print("Popped name from the beginning: " + popped_name_beginning)
names.remove("Alice") # removing an element by name --> the element mus exist

names.insert(1, "Paddington");
names.append("Alice")
names.append("Monster")


print("\nSorted list temporarily:")
for name in sorted(names):
    print(name)
print ("\nPrinting list in reversed order:")
names.reverse() # does not sort in reverse order alphabetically, just print the list in reversed order
for name in names:
    print(name)

print("\nSorted list permanently:")
names.sort() # sorts the list permanently
for name in names:
    print(name)
print("\nSorted in reverse order:")
names.sort(reverse=True) # sort in reverse order
for name in names:
    print(name)

print("Length of a list: " + str(len(names)) + "\n") # getting length of a list

for value in range(1,5):
    print(value)

numbers_to_hundred = list(range(1,101)) # creating a list from a range
even_numbers = list(range(2, 11, 2)) # start with 2, add 2 until 11
print("Smallest number to 100: " + str(min(numbers_to_hundred)))
print("Largest number to 100: " + str(max(numbers_to_hundred)))
print("all numbers to 100 added: " + str(sum(numbers_to_hundred)))

squares = [value**2 for value in range(1,11)] # all squared numbers to 10 in a list
for square in squares:
    print(square)

print(squares[1:4]) # print elements 1, 2, 3 of a list
print(squares[:4]) # print all elements to 3 of a list
print(squares[2:]) #print all elements from third to the end

squares_copied = squares[:] # copy a list

dimensions = (200, 50) # definint a tuple, an immutable list

even_numbers_to_hundred = list(range(2, 100, 2))
if (7 in even_numbers_to_hundred):
    print("7 is even")
elif (11 in even_numbers_to_hundred):
    print("11 is even")
elif(50 in even_numbers_to_hundred):
    print("50 is even")
