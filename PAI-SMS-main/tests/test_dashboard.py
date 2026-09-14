import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_dashboard_module():

    # --------------------------------
    # Launch Browser
    # --------------------------------

    driver = webdriver.Chrome()

    driver.maximize_window()

    # --------------------------------
    # Open Website
    # --------------------------------

    driver.get(
        "https://aradanaqa.pineappleai.cloud/login"
    )

    # --------------------------------
    # Login
    # --------------------------------

    login = LoginPage(driver)

    login.login(
        "admin",
        "admin123"
    )

    # --------------------------------
    # Wait
    # --------------------------------

    wait = WebDriverWait(driver, 10)

    # --------------------------------
    # Verify Dashboard
    # --------------------------------

    dashboard_title = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//h1[contains(text(),'Dashboard')]"
            )
        )
    )

    assert dashboard_title.is_displayed()

    print("LOGIN SUCCESSFUL")

    # --------------------------------
    # Dashboard Object
    # --------------------------------

    dashboard = DashboardPage(driver)

    # --------------------------------
    # Open Dashboard
    # --------------------------------

    dashboard.open_dashboard()

    print("DASHBOARD OPENED")

    time.sleep(2)

    # --------------------------------
    # Verify All Branch Options
    # --------------------------------

    dashboard.verify_branch_dropdown_options()

    time.sleep(2)

    # --------------------------------
    # Select All
    # --------------------------------

    dashboard.select_branch("All")

    time.sleep(2)

    # --------------------------------
    # Select Specific Branch
    # --------------------------------

    dashboard.select_branch(
        "India - New Delhi"
    )

    time.sleep(3)

    # --------------------------------
    # Notification
    # --------------------------------

    dashboard.click_notification()

    time.sleep(2)

    # --------------------------------
    # Close Browser
    # --------------------------------

    driver.quit()