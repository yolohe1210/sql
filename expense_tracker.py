import sqlite3

DATABASE = "expenses.db"


def connect_db():
    return sqlite3.connect(DATABASE)


def create_table():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expense_date TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            amount REAL NOT NULL
        )
    """)
    connection.commit()
    connection.close()


def add_expense():
    expense_date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return

    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO expenses
        (expense_date, category, description, amount)
        VALUES (?, ?, ?, ?)
    """, (expense_date, category, description, amount))
    connection.commit()
    connection.close()

    print("Expense added successfully.")


def view_expenses():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id, expense_date, category, description, amount
        FROM expenses
        ORDER BY expense_date
    """)
    expenses = cursor.fetchall()
    connection.close()

    if not expenses:
        print("No expenses found.")
        return

    for expense in expenses:
        print(
            f"ID: {expense[0]} | "
            f"Date: {expense[1]} | "
            f"Category: {expense[2]} | "
            f"Description: {expense[3]} | "
            f"Amount: ${expense[4]:.2f}"
        )


def update_expense():
    expense_id = int(input("Enter the ID to update: "))
    expense_date = input("Enter new date (YYYY-MM-DD): ")
    category = input("Enter new category: ")
    description = input("Enter new description: ")
    try:
        amount = float(input("Enter new amount: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return

    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE expenses
        SET expense_date = ?,
            category = ?,
            description = ?,
            amount = ?
        WHERE id = ?
    """, (expense_date, category, description, amount, expense_id))
    connection.commit()

    if cursor.rowcount == 0:
        print("Expense ID not found.")
    else:
        print("Expense updated successfully.")

    connection.close()


def delete_expense():
    expense_id = int(input("Enter the ID to delete: "))

    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )
    connection.commit()

    if cursor.rowcount == 0:
        print("Expense ID not found.")
    else:
        print("Expense deleted successfully.")

    connection.close()


def show_summary():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT SUM(amount), AVG(amount)
        FROM expenses
    """)
    total, average = cursor.fetchone()

    print(f"Total spending: ${total or 0:.2f}")
    print(f"Average expense: ${average or 0:.2f}")

    print("\nSpending by category:")

    cursor.execute("""
        SELECT category, SUM(amount), COUNT(*)
        FROM expenses
        GROUP BY category
        ORDER BY SUM(amount) DESC
    """)

    results = cursor.fetchall()

    for category, total_amount, count in results:
        print(
            f"{category}: ${total_amount:.2f} "
            f"from {count} expense(s)"
        )

    connection.close()


def main():
    create_table()

    while True:
        print("\nExpense Tracker")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Update expense")
        print("4. Delete expense")
        print("5. Show summary")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            update_expense()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            show_summary()
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()