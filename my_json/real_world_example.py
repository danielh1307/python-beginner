import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

print(todos)
print(todos[:1])

user_to_completed_tasks = {}

for todo in todos:
    if not todo["completed"]:
        continue
    curr_user = todo["userId"]
    if curr_user in user_to_completed_tasks.keys():
        curr_number = user_to_completed_tasks[curr_user]
        user_to_completed_tasks[curr_user] = curr_number + 1
    else:
        user_to_completed_tasks[curr_user] = 1

max_completed = 0
winner = []
print(user_to_completed_tasks)
for user in user_to_completed_tasks.items():
    if user[1] >= max_completed:
        max_completed = user[1]

for user in user_to_completed_tasks.items():
    if user[1] == max_completed:
        winner.append(user[0])

print(f"The user(s) with the most completed tasks ({max_completed}) is {winner}")

only_completed = []
for todo in todos:
    if not todo["userId"] in winner or not todo["completed"]:
        continue
    only_completed.append(todo)

with open("only_completed.json", "w") as data:
    json.dump(only_completed, data, indent=2)