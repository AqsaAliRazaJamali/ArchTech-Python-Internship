#  Task 2: To-Do List Application

> A menu-driven, console-based To-Do List Manager developed in Python that enables users to organize daily tasks, track completion status, and monitor overall progress through a dynamic command-line progress bar.

Developed as **Task 2** during the **Python Development Internship** at **Arch Technologies**.

---

## 📖 Project Overview

The **To-Do List Application** is a simple yet practical command-line task management system built using Python. It allows users to create, manage, and organize their daily tasks through an interactive menu-driven interface.

Each task can be added, viewed, marked as completed, or removed when no longer needed. The application also calculates and displays task completion progress using a visual progress bar, providing users with a quick overview of their productivity.

This project demonstrates fundamental Python programming concepts including data structures, loops, functions, conditional logic, user input validation, and modular program design.

---

##  Features

-  Add new tasks
-  View all current tasks
-  Mark tasks as completed
-  Remove tasks from the list
-  Dynamic command-line progress bar
-  Displays completion percentage
-  Input validation and error handling
-  Clean menu-driven user interface
-  Continuous interaction until user exits

---

## 🎯 Learning Objectives

This project was developed to strengthen understanding of:

- Python Functions
- Lists and Dictionaries
- While Loops
- Conditional Statements
- User Input Handling
- Exception Handling (`try` / `except`)
- Data Manipulation
- Modular Programming
- Console Application Development

---

##  Technologies Used

- Python 3
- Standard Python Library
- Visual Studio Code

---

##  Project Structure

```text
Task2_ToDoListApp/
│
├── todo_app.py
└── README.md
```

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/AqsaAliRazaJamali/ArchTech-Python-Internship.git
```

Navigate to the project directory:

```bash
cd ArchTech-Python-Internship/Task2_ToDoListApp
```

Run the application:

```bash
python todo_list.py
```

---

##  How It Works

The application follows a simple interactive workflow:

1. Launch the program.
2. Select an option from the main menu.
3. Add tasks to your to-do list.
4. View all current tasks and their status.
5. Mark tasks as completed.
6. Remove tasks when they are no longer needed.
7. Monitor completion progress through the built-in progress bar.
8. Exit the application whenever desired.

---

## 📊 Progress Bar

The application automatically calculates the percentage of completed tasks and displays it using a visual progress bar.

Example:

```text
Progress: [████████████░░░░░░░░] 60% (3/5 tasks completed)
```

The progress updates immediately whenever a task is marked as completed.

---

##  Sample Output

```text
════════════════════════════════════════
        TO-DO LIST MANAGER UI
════════════════════════════════════════
1. View Tasks & Progress
2. Add New Task
3. Mark Task as Completed
4. Remove Task
5. Exit Application
════════════════════════════════════════

Select an option (1-5): 2

Enter the task description:
Complete Internship Task

Success: 'Complete Internship Task' added to your list.
```

---

##  Implementation Highlights

- Uses a **list of dictionaries** to manage task data.
- Each task stores:
  - Task title
  - Completion status
- Implements modular programming through reusable functions.
- Includes exception handling for invalid user input.
- Calculates completion percentage dynamically based on completed tasks.
- Renders a visual command-line progress bar using Unicode characters.

---

##  Python Concepts Demonstrated

- Variables
- Lists
- Dictionaries
- Functions
- Loops
- Conditional Statements
- Exception Handling
- String Formatting
- User Input Validation
- Modular Programming

---

## 📌 Internship Task

**Task 2 – To-Do List Application**

**Python Development Internship**

**Arch Technologies**

---

## 👩‍💻 Author

**Aqsa Jamali**

Python Development Intern

GitHub: https://github.com/AqsaAliRazaJamali
