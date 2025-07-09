from .file_handler import read_tasks, write_tasks


def get_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1


def add_task(title, description):
    tasks = read_tasks()

    new_task = {
        'id': get_id(tasks),
        'title': title,
        'description': description,
        'status': 'not done'
    }

    tasks.append(new_task)
    write_tasks(tasks)
    print(f"\n✅ '{title}' task added successfully!")

def update_task(task_id, status):
    tasks = read_tasks()
    task_found = False

    for task in tasks:
        if int(task['id']) == int(task_id):
            task['status'] = status
            task_found = True
            break
    if task_found:
        write_tasks(tasks)
        print(f"Your {task_id} task status {status} changed successfully!")
    else:
        print(f"Your {task_id} task id not found!")

def delete_task(task_id):
    tasks = read_tasks()
    deleted_task = [task for task in tasks if int(task['id']) != int(task_id)]

    if len(tasks) == len(deleted_task):
        print(f"Your {task_id} task id not found!")
    else:
        write_tasks(deleted_task)
        print(f"Your task successfully deleted!")

def get_status(status_filter = None):
    tasks = read_tasks()

    if status_filter:
        return [task for task in tasks if task[status_filter] == tasks]
    return tasks
            