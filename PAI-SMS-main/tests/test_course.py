# test_course.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from pages.login_page import LoginPage
from pages.course_page import CoursePage


def test_course_module():

    # Launch Browser
    driver = webdriver.Chrome()

    driver.maximize_window()

    # Open Website
    driver.get("https://aradanaqa.pineappleai.cloud/login")

    # Login
    login = LoginPage(driver)

    login.login("admin", "admin123")

    # Wait
    wait = WebDriverWait(driver, 10)

    # Verify Dashboard
    dashboard = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//h1[contains(text(),'Dashboard')]")
        )
    )

    assert dashboard.is_displayed()

    print("LOGIN SUCCESSFUL")

    # Course Page
    course = CoursePage(driver)

    course.open_course_page()

    print("COURSE PAGE OPENED")

    time.sleep(3)

    # Search Course
    course.search_course("Keyboard")

    print("COURSE SEARCH SUCCESSFUL")

    time.sleep(3)

    # Add Course
    course.click_add_course()

    print("ADD COURSE POPUP OPENED")

    time.sleep(2)

    course.add_course(
        "C1003",
        "Drumstick",
        "Jaffna",
        "1",
        "Active",
        "5000"
    )

    print("NEW COURSE ADDED")

    time.sleep(5)

    # Edit Course
    course.click_edit()

    print("EDIT BUTTON CLICKED")

    time.sleep(3)

    # Update Course
    course.click_update()

    print("COURSE UPDATED")

    time.sleep(5)

    # Delete Course
    course.delete_course()

    print("COURSE DELETED")

    time.sleep(5)

    # Close Browser
    driver.quit()