"""
Selenium WebDriver end-to-end tests for SQAT Assignment 2.

Covered scenario:
  1. Login  – practicetestautomation.com/practice-test-login/
  2. Logout – same site, after successful login
  3. Flight search   – blazedemo.com (Boston → London)
  4. Choose a flight – first result from the list
  5. Purchase        – fill booking form and confirm
  6. Confirm success – assert "Thank you for your purchase" headline
"""

import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ---------------------------------------------------------------------------
# Public demo credentials (published on the login page itself)
# ---------------------------------------------------------------------------
LOGIN_URL = "https://practicetestautomation.com/practice-test-login/"
LOGIN_USERNAME = "student"
LOGIN_PASSWORD = "Password123"

BLAZEDEMO_URL = "https://blazedemo.com/"

SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "screenshots")


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,900")

    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=options)
    drv.implicitly_wait(0)          # rely on explicit waits only
    yield drv
    drv.quit()


def _wait(driver, timeout=10):
    return WebDriverWait(driver, timeout)


def _screenshot(driver, name: str):
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    path = os.path.join(SCREENSHOT_DIR, f"{name}.png")
    driver.save_screenshot(path)


# ---------------------------------------------------------------------------
# Test 1 – Login
# ---------------------------------------------------------------------------

class TestLogin:
    def test_successful_login(self, driver):
        driver.get(LOGIN_URL)

        _wait(driver).until(EC.visibility_of_element_located((By.ID, "username")))

        driver.find_element(By.ID, "username").clear()
        driver.find_element(By.ID, "username").send_keys(LOGIN_USERNAME)
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys(LOGIN_PASSWORD)
        driver.find_element(By.ID, "submit").click()

        success_heading = _wait(driver).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.post-title"))
        )

        _screenshot(driver, "login_success")
        assert "Logged In Successfully" in success_heading.text

    def test_logout(self, driver):
        logout_btn = _wait(driver).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Log out"))
        )
        logout_btn.click()

        _wait(driver).until(EC.url_contains("practice-test-login"))
        _screenshot(driver, "logout_success")
        assert "practice-test-login" in driver.current_url


# ---------------------------------------------------------------------------
# Test 2 – BlazeDemo flight booking
# ---------------------------------------------------------------------------

class TestFlightBooking:
    def test_search_flights(self, driver):
        driver.get(BLAZEDEMO_URL)

        _wait(driver).until(
            EC.visibility_of_element_located((By.NAME, "fromPort"))
        )

        Select(driver.find_element(By.NAME, "fromPort")).select_by_visible_text("Boston")
        Select(driver.find_element(By.NAME, "toPort")).select_by_visible_text("London")

        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        _wait(driver).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "table.table"))
        )

        heading = driver.find_element(By.TAG_NAME, "h3")
        _screenshot(driver, "flight_search")
        assert "Flights from Boston to London" in heading.text

    def test_choose_flight(self, driver):
        first_flight_btn = _wait(driver).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "table.table tbody tr:first-child input[type='submit']")
            )
        )
        first_flight_btn.click()

        _wait(driver).until(EC.url_contains("purchase.php"))
        assert "purchase.php" in driver.current_url

    def test_fill_and_purchase(self, driver):
        _wait(driver).until(
            EC.visibility_of_element_located((By.ID, "inputName"))
        )

        driver.find_element(By.ID, "inputName").clear()
        driver.find_element(By.ID, "inputName").send_keys("John Doe")

        driver.find_element(By.ID, "address").clear()
        driver.find_element(By.ID, "address").send_keys("123 Main Street")

        driver.find_element(By.ID, "city").clear()
        driver.find_element(By.ID, "city").send_keys("Astana")

        driver.find_element(By.ID, "state").clear()
        driver.find_element(By.ID, "state").send_keys("KZ")

        driver.find_element(By.ID, "zipCode").clear()
        driver.find_element(By.ID, "zipCode").send_keys("010000")

        Select(driver.find_element(By.ID, "cardType")).select_by_visible_text("Visa")

        driver.find_element(By.ID, "creditCardNumber").clear()
        driver.find_element(By.ID, "creditCardNumber").send_keys("4111111111111111")

        driver.find_element(By.ID, "creditCardMonth").clear()
        driver.find_element(By.ID, "creditCardMonth").send_keys("12")

        driver.find_element(By.ID, "creditCardYear").clear()
        driver.find_element(By.ID, "creditCardYear").send_keys("2027")

        driver.find_element(By.ID, "nameOnCard").clear()
        driver.find_element(By.ID, "nameOnCard").send_keys("John Doe")

        driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()

        confirmation_heading = _wait(driver).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )

        _screenshot(driver, "flight_booking_success")
        assert "Thank you for your purchase" in confirmation_heading.text
