FILE = "tasks.txt"

def add_task(task):
    with open(FILE, "a") as f:
        f.write(task + "\n")

def show_tasks():
    with open(FILE, "r") as f:
        tasks = f.readlines()
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")

def delete_task(index):
    with open(FILE, "r") as f:
        tasks = f.readlines()

    if 0 < index <= len(tasks):
        tasks.pop(index - 1)

        with open(FILE, "w") as f:
            f.writelines(tasks)
    else:
        print("Falsche Nummer")
