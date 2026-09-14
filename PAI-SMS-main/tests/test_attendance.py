# test_attendance.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from pages.login_page import LoginPage
from pages.attendance_page import AttendancePage


def test_attendance_page():

    # Launch Browser
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://aradanaqa.pineappleai.cloud/login")

    # Login
    login = LoginPage(driver)

    login.login("admin", "admin123")

    wait = WebDriverWait(driver, 10)

    # Verify Dashboard
    dashboard = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//h1[contains(text(),'Dashboard')]")
        )
    )

    assert dashboard.is_displayed()

    print("LOGIN SUCCESSFUL")

    # Attendance Page
    attendance = AttendancePage(driver)

    attendance.open_attendance_page()

    print("ATTENDANCE PAGE OPENED")

    # Search Attendance
    attendance.search_attendance("Keyboard")

    print("ATTENDANCE SEARCH SUCCESSFUL")

    time.sleep(3)

    # Click Scan QR
    attendance.click_scan_qr()

    print("SCAN QR BUTTON CLICKED")

    time.sleep(5)

    # Close Browser
    driver.quit()