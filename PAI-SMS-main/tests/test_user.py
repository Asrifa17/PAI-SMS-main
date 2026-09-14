from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from pages.login_page import LoginPage
from pages.user_page import UserPage


def test_user_module():
    # =====================================================
    # LAUNCH BROWSER
    # =====================================================

    driver = webdriver.Chrome()
    driver.maximize_window()

    # =====================================================
    # OPEN WEBSITE
    # =====================================================

    driver.get(
        "https://aradanaqa.pineappleai.cloud/login"
    )

    # =====================================================
    # LOGIN
    # =====================================================

    login = LoginPage(driver)

    login.login(
        "admin",
        "admin123"
    )

    wait = WebDriverWait(driver, 15)

    dashboard = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//h1[contains(text(),'Dashboard')]"
            )
        )
    )

    assert dashboard.is_displayed()

    print("LOGIN SUCCESSFUL")

    # =====================================================
    # OPEN USER PAGE
    # =====================================================

    user = UserPage(driver)

    user.open_user_page()

    print("USER PAGE OPENED")

    time.sleep(3)

    # =====================================================
    # SEARCH USER
    # =====================================================

    search_box = (
        By.XPATH,
        "//input[@placeholder='Search by name, email, or student number']"
    )
    user.search_user("Asrifa")

    print("USER SEARCH SUCCESSFUL")

    time.sleep(3)

    # =====================================================
    # CLEAR SEARCH
    # =====================================================

    search = wait.until(
        EC.visibility_of_element_located(
            user.search_box
        )
    )

    search.clear()

    time.sleep(2)

    print("USER SEARCH CLEARED")

    # =====================================================
    # ROLE FILTER
    # =====================================================

    user.select_role("Student")

    print("ROLE FILTER SUCCESSFUL")

    time.sleep(3)

    # =====================================================
    # CLEAR ROLE FILTER
    # =====================================================

    user.select_role("All Roles")

    time.sleep(2)

    print("ROLE FILTER CLEARED")

    # =====================================================
    # COURSE FILTER
    # =====================================================

    user.select_course("Keyboard")

    print("COURSE FILTER SUCCESSFUL")

    time.sleep(3)

    # =====================================================
    # CLEAR COURSE FILTER
    # =====================================================

    user.select_course("All Courses")

    time.sleep(2)

    print("COURSE FILTER CLEARED")

    # =====================================================
    # OPEN STUDENT PROFILE
    # =====================================================

    user.click_profile()

    print("PROFILE OPENED")

    time.sleep(2)

    # =====================================================
    # OPEN ID CARD
    # =====================================================

    user.click_id_card()

    print("ID CARD OPENED")

    time.sleep(3)

    # =====================================================
    # CLOSE / RETURN IF REQUIRED
    # =====================================================

    # Add the appropriate close action here if the
    # application provides a close button for ID Card.

    print("USER MODULE TEST COMPLETED")

    # =====================================================
    # CLOSE BROWSER
    # =====================================================

    driver.quit()