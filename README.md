# Software QA & Testing — Assignment 2 (AITU)

![Python](https://img.shields.io/badge/python-3.x-blue)
![Selenium](https://img.shields.io/badge/tool-Selenium-43B02A)
![Course](https://img.shields.io/badge/course-SQAT-lightgrey)

## Overview

Assignment 2 for the **Software Quality Assurance and Testing** course at Astana IT University.
Browser-driven end-to-end automation with Selenium WebDriver covering two demo applications:

| # | Site | Flow |
|---|------|------|
| 1 | [practicetestautomation.com](https://practicetestautomation.com/practice-test-login/) | Login → assert success page → Logout |
| 2 | [blazedemo.com](https://blazedemo.com) | Select Boston → London → choose first flight → fill purchase form → assert confirmation |

## What it covers

- Selenium WebDriver 4 setup with **Selenium Manager / webdriver-manager** (no hardcoded driver path)
- Locating elements by ID, CSS selector, name, and link text
- Filling forms, `Select` dropdowns, clicking buttons
- Explicit waits with `WebDriverWait` and `expected_conditions`
- Screenshot capture at each key step saved to `screenshots/`
- Assertions on page headings and URL state
- `pytest` fixture for browser lifecycle (setup / teardown)

## Project structure

```
Assignment_2_SQAT/
├── test_sqat.py          # Selenium test suite (pytest)
├── requirements.txt      # Python dependencies
└── screenshots/          # Evidence screenshots (committed + regenerated on each run)
    ├── login_success.png
    ├── logout_success.png
    ├── flight_search.png
    ├── search_test.png
    └── flight_booking_success.png
```

## Prerequisites

- Python 3.9+
- **Google Chrome** (or Chromium) installed — ChromeDriver is downloaded automatically

## Getting started

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running the tests

```bash
pytest test_sqat.py -v
```

Tests run headless by default (`--headless=new`). To watch Chrome open, remove
the `--headless=new` argument from the `driver` fixture in `test_sqat.py`.

### Expected output

```
test_sqat.py::TestLogin::test_successful_login  PASSED
test_sqat.py::TestLogin::test_logout            PASSED
test_sqat.py::TestFlightBooking::test_search_flights    PASSED
test_sqat.py::TestFlightBooking::test_choose_flight     PASSED
test_sqat.py::TestFlightBooking::test_fill_and_purchase PASSED
```

Screenshots are saved/overwritten in `screenshots/` after each run.

---

Adil Ormanov — [GitHub](https://github.com/Adilforest)
