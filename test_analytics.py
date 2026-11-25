
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
        self.assertEqual(expense["amount"], 200.0)
        self.assertEqual(expense["category"], "Food")

    def test_category_filter(self):
        result = filter_by_category(self.expenses, "Food")
        self.assertEqual(len(result), 2)

    def test_date_filter(self):
        result = filter_by_date_range(
            self.expenses,
            "2026-11-11",
            "2026-11-20"
        )
        self.assertEqual(len(result), 2)

    def test_category_totals(self):
        totals = get_category_totals(self.expenses)
        self.assertEqual(totals["Food"], 2500.0)

    def test_budget_warning(self):
        budgets = {"Food": 3000}
        result = check_budget_status(
            self.expenses, budgets, "2026-11"
        )
        self.assertEqual(result["Food"]["status"], "Warning")

    def test_budget_exceeded(self):
        budgets = {"Food": 2000}
        result = check_budget_status(
            self.expenses, budgets, "2026-11"
        )
        self.assertEqual(result["Food"]["status"], "Exceeded")

    def test_empty_summary(self):
        result = compute_summary_tuple([])
        self.assertEqual(result, (0, 0, 0, 0))

    def test_summary_values(self):
        result = compute_summary_tuple(self.expenses)
        self.assertEqual(result, (3000.0, 1000.0, 1500.0, 500.0))

    def test_invalid_amount(self):
        self.assertFalse(validate_amount("-100"))
        self.assertFalse(validate_amount("abc"))

    def test_valid_amount(self):
        self.assertTrue(validate_amount("500"))

    def test_date_validation(self):
        self.assertTrue(validate_date("2026-11-25"))
        self.assertFalse(validate_date("25-11-2026"))

    def test_category_validation(self):
        self.assertTrue(validate_category("Food"))
        self.assertFalse(validate_category("Shopping"))


if __name__ == "__main__":
    unittest.main()
