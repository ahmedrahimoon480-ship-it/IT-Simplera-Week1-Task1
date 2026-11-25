
import unittest

from src.analytics import (
    add_expense,
    filter_by_category,
    filter_by_date_range,
    get_category_totals,
    check_budget_status,
    compute_summary_tuple
)

from src.validators import (
    validate_amount,
    validate_date,
    validate_category
)


class TestExpenseAnalyzer(unittest.TestCase):

    def setUp(self):
        self.expenses = [
            {
                "id": 1,
                "date": "2026-11-10",
                "category": "Food",
                "amount": 1000.0,
                "description": "Lunch"
            },
            {
                "id": 2,
                "date": "2026-11-12",
                "category": "Transport",
                "amount": 500.0,
                "description": "Bus"
            },
            {
                "id": 3,
                "date": "2026-11-15",
                "category": "Food",
                "amount": 1500.0,
                "description": "Dinner"
            }
        ]

    def test_add_expense(self):
        expense = add_expense(
            self.expenses,
            "2026-11-20",
            "Food",
            200,
            "Snacks"
        )
        assert expense["amount"] == 200.0
        assert expense["category"] == "Food"

    def test_category_filter(self):
        result = filter_by_category(self.expenses, "Food")
        assert len(result) == 2

    def test_date_filter(self):
        result = filter_by_date_range(
            self.expenses,
            "2026-11-11",
            "2026-11-20"
        )
        assert len(result) == 2

    def test_category_totals(self):
        totals = get_category_totals(self.expenses)
        assert totals["Food"] == 2500.0

    def test_budget_warning(self):
        budgets = {"Food": 3000}
        result = check_budget_status(
            self.expenses, budgets, "2026-11"
        )
        assert result["Food"]["status"] == "Warning"

    def test_budget_exceeded(self):
        budgets = {"Food": 2000}
        result = check_budget_status(
            self.expenses, budgets, "2026-11"
        )
        assert result["Food"]["status"] == "Exceeded"

    def test_empty_summary(self):
        result = compute_summary_tuple([])
        assert result == (0, 0, 0, 0)

    def test_summary_values(self):
        result = compute_summary_tuple(self.expenses)
        assert result == (3000.0, 1000.0, 1500.0, 500.0)

    def test_invalid_amount(self):
        assert validate_amount("-100") is False
        assert validate_amount("abc") is False

    def test_valid_amount(self):
        assert validate_amount("500") is True

    def test_date_validation(self):
        assert validate_date("2026-11-25") is True
        assert validate_date("25-11-2026") is False

    def test_category_validation(self):
        assert validate_category("Food") is True
        assert validate_category("Shopping") is False


if __name__ == "__main__":
    unittest.main()
