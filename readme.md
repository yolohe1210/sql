# Overview
As a software engineer, my primary goal for this project was to deepen my practical understanding of backend data persistence by integrating a Python application with a robust relational database. I wanted to move beyond in-memory data structures and learn how to design tables, manage database connections, and execute structured queries for full CRUD (Create, Read, Update, Delete) operations.

This software is a command-line Expense Tracker application designed to help users efficiently manage and analyze their personal finances. It interfaces seamlessly with an SQLite relational database (expenses.db), automatically initializing the required schema upon launch. Users can interact with the system through an intuitive menu-driven interface to add new expenses, view all recorded items, update existing details, remove erroneous entries, and generate comprehensive spending summaries backed by SQL aggregate functions.

My purpose for writing this software was to build a complete, end-to-end data-driven utility from scratch—handling everything from schema design and parameterized SQL queries to user input handling and data presentation.

[Software Demo Video](https://youtu.be/l8m_Pq6_eE4)

# Relational Database

For this project, I used SQLite, a lightweight, serverless, and self-contained relational database management system. SQLite is exceptionally well-suited for standalone applications and Python development because it requires no separate server setup and stores the entire database in a single file on disk.

The database consists of a single primary table named expenses with the following structure:
- id: INTEGER PRIMARY KEY AUTOINCREMENT — A unique numerical identifier for each expense record.
- expense_date: TEXT NOT NULL — The date when the expense occurred, formatted as YYYY-MM-DD.
- category: TEXT NOT NULL — The classification of the expense (e.g., Food, Transport, Utilities).
- description: TEXT — Optional notes or details regarding the specific transaction.
- amount: REAL NOT NULL — The monetary value of the expense.

# Development Environment

To develop this software, I utilized the following tools and environment:
- Code Editor / IDE: Visual Studio Code for writing, debugging, and organizing the Python source code.
- Version Control: Git for tracking code changes and maintaining project history.
- Terminal / Command Prompt: For running the Python script and interacting with the SQLite database CLI if needed.

The software was developed using Python 3, leveraging its built-in sqlite3 library, which provides a native, clean API for executing SQL statements and managing database transactions without requiring any third-party package installations.

# Useful Websites

Here is a list of websites that I found particularly helpful during the development of this project:

- [Python sqlite3 Official Documentation](https://docs.python.org/3/library/sqlite3.html)
- [SQLite Tutorial Website](https://www.sqlitetutorial.net/)
- [TutorialsPoint SQLite Python Guide](https://www.tutorialspoint.com/sqlite/sqlite_python.htm)

# Future Work

While the current version of the Expense Tracker fully satisfies the core requirements and incorporates aggregate summaries, there are several enhancements and features I plan to implement in the future:

- Item 1: Implement robust input error handling (using `try-except` blocks) to prevent application crashes when users input invalid data types for amounts or IDs.
- Item 2: Add a date-range filtering feature to allow users to query and summarize expenses between specific start and end dates.
- Item 3: Introduce a graphical user interface (GUI) or a lightweight web interface (using Flask) to make the application more visually appealing and accessible.