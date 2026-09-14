from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from pages.login_page import LoginPage


def test_valid_login_logout():

    # Launch Browser
    driver = webdriver.Chrome()

    # Maximize Browser
    driver.maximize_window()

    # Open Website
    driver.get("https://aradanaqa.pineappleai.cloud/login")

    # Create Login Page Object
    login = LoginPage(driver)

    # Login
    login.login("admin", "admin123")

    # Wait Object
    wait = WebDriverWait(driver, 10)

    # Verify Dashboard Opened
    dashboard = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//h1[contains(text(),'Dashboard')]")
        )
    )

    assert dashboard.is_displayed()

    print("LOGIN SUCCESSFUL")

    # Stay 10 seconds in dashboard
    time.sleep(10)



    # Click Logout Icon/Text
    logout_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[2]/div/span')
        )
    )

    # JavaScript Click
    driver.execute_script("arguments[0].click();", logout_button)

    print("LOGOUT Menu CLICKED")

    # Wait 2 seconds
    time.sleep(2)

    # Click YES Logout Button
    yes_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div[2]/div/div[2]/button[2]')
        )
    )

    yes_button.click()

    print("LOGOUT BUTTON CLICKED")

    # Verify Redirected to Login Page
    login_page = wait.until(
        EC.presence_of_element_located(
            (By.NAME, "username")
        )
    )

    assert login_page.is_displayed()

    print("LOGOUT SUCCESSFUL - REDIRECTED TO LOGIN PAGE")

    # Close Browser
    driver.quit()