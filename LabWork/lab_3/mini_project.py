'''
Mini Project:
Simple To-Do Manager Using Functional Programming
Objective: Manage a list of to-do tasks using functions, lambda, filter, and map.
Requirements:
● Allow adding tasks using a function add_task(task_list, task_name).
● Each task is a dictionary: { "name": str, "completed": bool }.
● Use lambda and filter() to list only incomplete tasks.
● Use map() to mark all tasks as completed.
● Include a search_tasks(task_list, keyword) function using filter() and lambda.
Sample Workflow:
tasks = []
tasks = add_task(tasks, "Buy groceries")
tasks = add_task(tasks, "Finish assignment")
tasks = add_task(tasks, "Call friend")
# List incomplete tasks
print("Pending Tasks:", list_pending(tasks))

# Mark all tasks as complete
tasks = complete_all(tasks)
# Search tasks with keyword "call"
print("Search Result:", search_tasks(tasks, "call"))

'''

def add_task(task_list, task_name):
    new_task = {"name": task_name, "completed": False}
    return task_list + [new_task]


def list_pending(task_list):
    return list(filter(lambda task: not task["completed"], task_list))


def complete_all(task_list):
    return list(map(lambda task: {**task, "completed": True}, task_list))


def search_tasks(task_list, keyword):
    return list(filter(lambda task: keyword.lower() in task["name"].lower(), task_list))



tasks = []
tasks = add_task(tasks, "Buy groceries")
tasks = add_task(tasks, "Finish assignment")
tasks = add_task(tasks, "Call friend")

print("Pending Tasks:", list_pending(tasks))
tasks = complete_all(tasks)
print("Search Result:", search_tasks(tasks, "call"))


 
