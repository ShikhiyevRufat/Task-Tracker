# ✅ Simple CLI Task Tracker

A lightweight, zero-dependency command-line interface (CLI) tool for managing your daily tasks. Track what you need to do, what's in progress, and what you've completed, all from the comfort of your terminal.

This project is built using only native modules, storing tasks in a simple `tasks.json` file in the project directory.

***

## ✨ Features

-   **Add, Update, & Delete Tasks**: Full CRUD functionality for your tasks.
-   **Track Progress**: Mark tasks with a status of `todo`, `in-progress`, or `done`.
-   **Flexible Listing**: View all tasks or filter them by their status.
-   **Command-Line Based**: All interactions are handled through command-line arguments.
-   **Local Storage**: Your tasks are saved in a human-readable `tasks.json` file.
-   **No Dependencies**: Runs out-of-the-box with a standard Python installation. No `pip install` needed.

***

## 🚀 Getting Started

No installation is required. Just clone the repository and ensure you have Python 3.6+ installed.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/cli-task-tracker.git](https://github.com/your-username/cli-task-tracker.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd cli-task-tracker
    ```

That's it! You're ready to start managing your tasks. The application will automatically create a `tasks.json` file in the directory when you add your first task.

***

## 💻 Usage

The application is operated using positional arguments from your terminal.

**General syntax:** `python task_manager.py <command> [arguments...]`

---

### **1. Add a new task**

Creates a new task with a status of `todo`.

-   **Command:** `add`
-   **Argument:** `"<description>"` (The task description in quotes)

**Example:**
```bash
python task_manager.py add "Buy groceries for the week"
```
> ✅ Success: Task 1 'Buy groceries for the week' added.

---

### **2. List tasks**

Displays a list of tasks. You can list all tasks or filter by status.

-   **Command:** `list`
-   **Argument (Optional):** `[status]` (Can be `todo`, `in-progress`, or `done`)

**Examples:**
```bash
# List all tasks
python task_manager.py list

# List only completed tasks
python task_manager.py list done

# List tasks that are in progress
python task_manager.py list in-progress
```

---

### **3. Update a task**

Updates a task's description or status. The `updatedAt` timestamp will be automatically refreshed.

-   **Command:** `update`
-   **Arguments:** `<id> <property> "<new_value>"`
    -   `<id>`: The ID of the task to update.
    -   `<property>`: The property to change (`desc` or `status`).
    -   `"<new_value>"`: The new value for the description or status.

**Examples:**
```bash
# Update the status of task 1 to 'in-progress'
python task_manager.py update 1 status "in-progress"

# Update the description of task 2
python task_manager.py update 2 desc "Buy ALL the groceries for the month"
```
> ✅ Success: Task 1 status updated to in-progress.

---

### **4. Delete a task**

Permanently removes a task from the list.

-   **Command:** `delete`
-   **Argument:** `<id>` (The ID of the task to delete)

**Example:**
```bash
python task_manager.py delete 3
```
> ✅ Success: Task 3 deleted.

***

## 📂 Task Data Structure

All tasks are stored in the `tasks.json` file. Each task is a JSON object with the following properties:

```json
{
  "id": 1,
  "description": "Plan the project architecture",
  "status": "done",
  "createdAt": "2025-07-09T14:45:10.123456",
  "updatedAt": "2025-07-09T14:52:30.654321"
}
```

-   **`id`**: A unique integer identifying the task.
-   **`description`**: The text content of the task.
-   **`status`**: The current state of the task (`todo`, `in-progress`, or `done`).
-   **`createdAt`**: An ISO 8601 timestamp for when the task was created.
-   **`updatedAt`**: An ISO 8601 timestamp for when the task was last modified.

***

## ⚠️ Error Handling

The application gracefully handles common errors, such as:
-   Using an invalid command.
-   Providing a non-existent task ID for `update` or `delete` operations.
-   Supplying an incorrect number of arguments for a command.
-   Using an invalid status value.

In these cases, a clear error message will be printed to the console to guide you.

***

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
