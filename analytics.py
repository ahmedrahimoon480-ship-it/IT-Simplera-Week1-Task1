
from datetime import datetime


def add_expense(expenses, date, category, amount, description):
    """Create and return a new expense record."""
    expense = {
        "id": len(expenses) + 1,
        "date": date,
        "category": category,
        "amount": float(amount),
        "description": description
    }

    return expense


def filter_by_category(expenses, category):
    """Return expenses matching a category."""
    return [
        expense for expense in expenses
        if expense["category"].lower() == category.lower()
    ]


def filter_by_date_range(expenses, start_date, end_date):
    """Return expenses within a date range."""
    return [
        expense for expense in expenses
        if start_date <= expense["date"] <= end_date
    ]


def get_category_totals(expenses):
    """Calculate total spending for each category."""
    totals = {}

    for expense in expenses:
        category = expense["category"]
        totals[category] = (
            totals.get(category, 0) + expense["amount"]
        )

    return totals


def check_budget_status(expenses, budgets, month):
    """Check monthly budget status for every budget category."""
    results = {}

    for category, limit in budgets.items():
        spent = sum(
            expense["amount"]
            for expense in expenses
            if expense["category"] == category
            and expense["date"].startswith(month)
        )

        percentage = (spent / limit) * 100 if limit > 0 else 0

        if percentage > 100:
            status = "Exceeded"
        elif percentage >= 80:
            status = "Warning"
        else:
            status = "Safe"

        results[category] = {
            "spent": spent,
            "limit": limit,
            "percentage": percentage,
            "status": status
        }

    return results


def compute_summary_tuple(expenses):
    """Return total, average, highest and lowest expenses."""
    if not expenses:
        return (0, 0, 0, 0)

    amounts = [expense["amount"] for expense in expenses]

    total = sum(amounts)
    average = total / len(amounts)
    highest = max(amounts)
    lowest = min(amounts)

    return (total, average, highest, lowest)
