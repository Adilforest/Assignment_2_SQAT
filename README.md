# Software QA & Testing — Assignment 2 (AITU)

![Python](https://img.shields.io/badge/python-3.x-blue)
![Selenium](https://img.shields.io/badge/tool-Selenium-43B02A)
![Course](https://img.shields.io/badge/course-SQAT-lightgrey)

## Overview

Assignment 2 for the **Software Quality Assurance and Testing** course at Astana IT University.
Covers introductory Selenium WebDriver automation: browser-driven end-to-end tests for a
demo flight-booking web application.

## What it covers

- Selenium WebDriver setup and browser control
- Locating elements by name, CSS selector, and XPath
- Filling forms, clicking buttons, and submitting searches
- Explicit waits with `WebDriverWait` and `expected_conditions`
- Screenshot capture at key test steps as evidence
- Basic assertions on page state after navigation

## Project structure

```
Assignment_2_SQAT/
├── test_sqat.py          # Selenium test script
└── screenshots/          # Step-by-step screenshots
    ├── login_success.png
    ├── flight_search.png
    ├── search_test.png
    ├── flight_booking_success.png
    └── logout_success.png
```

## Getting started

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install selenium webdriver-manager
```

Run the test:

```bash
python test_sqat.py
# or via pytest
pytest test_sqat.py -v
```

> Requires Chrome (or Chromium) and a matching ChromeDriver on `PATH`.

---

Adil Ormanov — [GitHub](https://github.com/Adilforest)
