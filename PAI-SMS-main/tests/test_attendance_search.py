import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.attendance_page import AttendancePage


# ---------------------------------------------------------
# Test 1 - Open Attendance Page
# ---------------------------------------------------------

def test_attendance_page():

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

    # Attendance
    attendance = AttendancePage(driver)
    attendance.open_attendance_page()

    print("ATTENDANCE PAGE OPENED")

    # Verify Attendance heading
    attendance_heading = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//h1[contains(text(),'Attendance')]")
        )
    )

    assert attendance_heading.is_displayed()

    print("ATTENDANCE PAGE VERIFIED")

    driver.quit()


# ---------------------------------------------------------
# Test 2 - Search Student Name
# ---------------------------------------------------------

def test_attendance_search_student():

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://aradanaqa.pineappleai.cloud/login")

    # Login
    login = LoginPage(driver)
    login.login("admin", "admin123")

    wait = WebDriverWait(driver, 10)

    # Open Attendance
    attendance = AttendancePage(driver)
    attendance.open_attendance_page()

    print("ATTENDANCE PAGE OPENED")

    time.sleep(2)

    # Search student
    attendance.search_attendance("Prashalini")

    print("STUDENT SEARCH PERFORMED")

    time.sleep(3)

    # Verify search result
    rows = driver.find_elements(
        By.XPATH,
        "//main//table/tbody/tr"
    )

    assert len(rows) > 0

    # Verify result contains searched student
    page_text = driver.find_element(
        By.XPATH,
        "//main"
    ).text

    assert "Prashalini" in page_text

    print("STUDENT SEARCH SUCCESSFUL")

    driver.quit()


# ---------------------------------------------------------
# Test 3 - Search Course Name
# ---------------------------------------------------------

def test_attendance_search_course():

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://aradanaqa.pineappleai.cloud/login")

    # Login
    login = LoginPage(driver)
    login.login("admin", "admin123")

    # Open Attendance
    attendance = AttendancePage(driver)
    attendance.open_attendance_page()

    print("ATTENDANCE PAGE OPENED")

    time.sleep(2)

    # Search course
    attendance.search_attendance("Violin")

    print("COURSE SEARCH PERFORMED")

    time.sleep(3)

    # Get table rows
    rows = driver.find_elements(
        By.XPATH,
        "//main//table/tbody/tr"
    )

    assert len(rows) > 0

    # Verify Keyboard is displayed
    page_text = driver.find_element(
        By.XPATH,
        "//main"
    ).text

    assert "Violin" in page_text

    print("COURSE SEARCH SUCCESSFUL")

    driver.quit()


# ---------------------------------------------------------
# Test 4 - Search Invalid / Date-Time Value
# ---------------------------------------------------------

def test_attendance_search_invalid_value():

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://aradanaqa.pineappleai.cloud/login")

    # Login
    login = LoginPage(driver)
    login.login("admin", "admin123")

    # Open Attendance
    attendance = AttendancePage(driver)
    attendance.open_attendance_page()

    print("ATTENDANCE PAGE OPENED")

    time.sleep(2)

    # Enter date-related value
    attendance.search_attendance("2026")

    print("INVALID SEARCH VALUE ENTERED")

    time.sleep(3)

