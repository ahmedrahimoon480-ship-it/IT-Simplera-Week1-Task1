
# Personal Expense & Budget CLI Analyzer

## About

A Python command-line application for managing daily expenses,
monthly category budgets, and spending analytics.

## Features

- Add expenses
- View all expenses
- Filter expenses by category
- Filter expenses by date range
- Set monthly category budgets
- Budget alerts (Safe, Warning, Exceeded)
- Expense analytics
- Input validation
- Automated unit tests

## Technologies

- Python 3.11+
- Lists
- Dictionaries
- Sets
- Tuples
- Functions
- datetime
- unittest

## Project Structure

```text
Week1_Task1_AhmedRahimoon/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── analytics.py
│   └── validators.py
├── tests/
│   └── test_analytics.py
├── screenshots/
├── .gitignore
├── requirements.txt
└── README.md
```

## How to Run

Open the terminal in the project root directory.

Run:

```bash
python src/main.py
```

## How to Run Tests

Run:

```bash
python -m unittest discover -s tests -v
```

## Budget Status

- Safe: Below 80%
- Warning: 80% to 100%
- Exceeded: Above 100%

## Internship

IT Simplera

Python Development Internship

Week 1 - Task 1

## Author

Ahmed Rahimoon
