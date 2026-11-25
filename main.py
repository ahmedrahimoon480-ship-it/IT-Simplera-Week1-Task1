
from analytics import (
    add_expense,
    filter_by_category,
    filter_by_date_range,
    get_category_totals,
    check_budget_status,
    compute_summary_tuple
)

from validators import (
    validate_amount,
    validate_date,
    validate_category,
    VALID_CATEGORIES
)


expenses = []
budgets = {}


def show_expenses(records):
    """Display expense records."""
    if not records:
        print("\nNo expenses found.")
        return

    print("\nID | Date       | Category      | Amount | Description")
    print("-" * 65)

    for expense in records:
        print(
            f"{expense['id']}  | "
            f"{expense['date']} | "
            f"{expense['category']:<13} | "
            f"{expense['amount']:.2f} | "
            f"{expense['description']}"
        )


def add_new_expense():
    """Ask the user for expense information."""
    date = input("Enter date (YYYY-MM-DD): ").strip()

    if not validate_date(date):
        print("Invalid date!")
        return

    category = input(
        "Category (Food, Transport, Utilities, Entertainment, Other): "
    ).strip().title()

    if not validate_category(category):
        print("Invalid category!")
        return

    amount = input("Enter amount: ").strip()

    if not validate_amount(amount):
        print("Amount must be greater than zero!")
        return

    description = input("Enter description: ").strip()

    if not description:
        print("Description cannot be empty!")
        return

    expense = add_expense(
        expenses, date, category, amount, description
    )

    expenses.append(expense)
    print("Expense added successfully!")


def set_monthly_budget():
    """Set a monthly budget for a category."""
    category = input("Enter category: ").strip().title()

    if not validate_category(category):
        print("Invalid category!")
        return

    amount = input("Enter monthly budget: ").strip()

    if not validate_amount(amount):
        print("Invalid budget amount!")
        return

    budgets[category] = float(amount)
    print("Budget saved successfully!")


def show_budget_alerts():
    """Display budget status for a selected month."""
    month = input("Enter month (YYYY-MM): ").strip()

    try:
        datetime_check = __import__("datetime").datetime.strptime(
            month, "%Y-%m"
        )
        if datetime_check.strftime("%Y-%m") != month:
            raise ValueError
    except ValueError:
        print("Invalid month format!")
        return

    if not budgets:
        print("No budgets have been set.")
        return

    results = check_budget_status(expenses, budgets, month)

    print(f"\nBudget Report for {month}")
    print("-" * 55)

    for category, data in results.items():
        print(
            f"{category}: Spent {data['spent']:.2f} / "
            f"{data['limit']:.2f} | "
            f"{data['percentage']:.1f}% | {data['status']}"
        )


def show_analytics():
    """Display spending analytics."""
    total, average, highest, lowest = compute_summary_tuple(
        expenses
    )

    print("\n========== ANALYTICS REPORT ==========")
    print(f"Total Spending:   {total:.2f}")
    print(f"Average Expense:  {average:.2f}")
    print(f"Highest Expense:  {highest:.2f}")
    print(f"Lowest Expense:   {lowest:.2f}")

    print("\nCategory Breakdown:")

    category_totals = get_category_totals(expenses)

    if not category_totals:
        print("No expense data available.")
        return

    for category, amount in category_totals.items():
        percentage = (amount / total) * 100 if total else 0
        print(
            f"{category}: {amount:.2f} "
            f"({percentage:.1f}%)"
        )

    show_budget_alerts_for_current_month = input(
        "\nWould you like to see budget alerts? (y/n): "
    ).strip().lower()

    if show_budget_alerts_for_current_month == "y":
        show_budget_alerts()


def main():
    """Run the expense analyzer menu."""
    while True:
        print("\n====================================")
        print(" PERSONAL EXPENSE & BUDGET ANALYZER")
        print("====================================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses")
        print("4. Set Monthly Budget")
        print("5. Analytics Report")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_new_expense()

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            print("\n1. Filter by Category")
            print("2. Filter by Date Range")

            filter_choice = input("Choose filter: ").strip()

            if filter_choice == "1":
                category = input("Enter category: ").strip()
                results = filter_by_category(expenses, category)
                show_expenses(results)

            elif filter_choice == "2":
                start = input("Enter start date (YYYY-MM-DD): ").strip()
                end = input("Enter end date (YYYY-MM-DD): ").strip()

                if (
                    validate_date(start)
                    and validate_date(end)
                    and start <= end
                ):
                    results = filter_by_date_range(
                        expenses, start, end
                    )
                    show_expenses(results)
                else:
                    print("Invalid date range!")

            else:
                print("Invalid filter choice!")

        elif choice == "4":
            set_monthly_budget()

        elif choice == "5":
            show_analytics()

        elif choice == "6":
            print("Thank you for using the Expense Analyzer!")
            break

        else:
            print("Invalid choice! Please select 1 to 6.")


if __name__ == "__main__":
    main()
