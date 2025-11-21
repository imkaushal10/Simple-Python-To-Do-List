# Simple Python To-Do List (Enhanced Version)

A simple and beginner-friendly command-line To-Do List application built in Python. This enhanced version includes features developed by our team as part of an open-source course project.

## Features

- **Add Tasks** — Create a new task and optionally assign a priority level (High, Medium, Low)
- **Remove Tasks** — Delete any task by selecting its index
- **Mark Tasks as Completed** — Update the completion status of any task
- **View All Tasks** — Displays index, task name, completion status, and priority level
- **Persistent Storage** *(New)* — Tasks automatically load on program start and save to a JSON file on exit
- **Priority System** *(New)* — Each task includes a priority label: High / Medium / Low

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses standard library only)

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/imkaushal10/Simple-Python-To-Do-List.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Simple-Python-To-Do-List
   ```

3. Run the `todo.py` script:

   ```bash
   python todo.py
   ```

## Usage

When you run `python todo.py`, a menu will appear with the following options:

1. **Add Task** — Enter task name and priority (High/Medium/Low)
2. **Remove Task** — View current tasks and remove by index
3. **Mark Task as Completed** — View tasks and mark by index
4. **View Tasks** — Display all tasks with index, priority, and status
5. **Exit** — Saves tasks to `tasks.json` and quits

### Example Workflow

```
--- To-Do List Menu ---
1. Add Task
2. Remove Task
3. Mark Task as Completed
4. View Tasks
5. Exit
Enter your choice: 1

Enter the task: Buy groceries
Enter priority (High/Medium/Low): High
Task 'Buy groceries' with priority 'High' added!
```

## File Structure

```
.
├── todo.py          # Main application
├── tasks.json       # Auto-generated on exit (ignored in repo)
├── README.md        # This file
└── .gitignore       # Prevents tasks.json from being tracked
```

## Team Contribution Summary

- **Kaushal** — Implemented JSON save/load persistence, added the priority feature, updated README and documentation, performed manual testing
- **Wasey** — Performed manual testing, improved output formatting, assisted with documentation

## Future Improvements

- Search functionality for tasks
- Create a simple GUI (Tkinter) or web front-end (Flask/Django)

## License

This project follows the license of the original repository. See the repository root for license details.

---

*This project was created as part of an open-source software development course to demonstrate collaborative development practices.*
