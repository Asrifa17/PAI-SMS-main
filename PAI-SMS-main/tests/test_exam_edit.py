import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.exam_page import ExamPage


# =====================================================
# LOGIN DETAILS
# =====================================================

LOGIN_URL = "https://aradanaqa.pineappleai.cloud/login"

USERNAME = "admin"
PASSWORD = "admin123"


# =====================================================
# LOGIN
# =====================================================

def login(driver):

    driver.get(LOGIN_URL)

    login_page = LoginPage(driver)

    login_page.login(
        USERNAME,
        PASSWORD
    )

    # Verify Dashboard
    wait = WebDriverWait(driver, 20)

    dashboard = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//h1[contains(text(),'Dashboard')]"
            )
        )
    )

    assert dashboard.is_displayed()

    print("LOGIN SUCCESSFUL")

    time.sleep(3)


# =====================================================
# TC_Exam_191
# Edit Exam Update
# =====================================================

def test_edit_exam_update():

    # =================================================
    # LAUNCH BROWSER
    # =================================================

    driver = webdriver.Chrome()

    driver.maximize_window()

    try:

        # =============================================
        # LOGIN
        # =============================================

        login(driver)

        # =============================================
        # CREATE EXAM PAGE OBJECT
        # =============================================

        exam = ExamPage(driver)

        # =============================================
        # OPEN EXAM MODULE
        # =============================================

        exam.open_exam_page()

        print("EXAM PAGE OPENED")

        time.sleep(3)

        # =============================================
        # CLICK EDIT ICON
        # =============================================

        exam.click_edit_exam()

        print("EDIT EXAM OPENED")

        time.sleep(2)

        # =============================================
        # CHANGE EXAM TYPE
        # Practical -> Theory
        # =============================================

        exam.change_exam_type(
            "Theory"
        )

        print("EXAM TYPE CHANGED TO THEORY")

        time.sleep(2)

        # =============================================
        # EDIT GROUP
        # =============================================

        exam.click_edit_group()

        print("EDIT GROUP OPENED")

        time.sleep(2)

        # =============================================
        # NO STUDENT CHANGE
        # =============================================

        exam.click_next()

        print("GROUP NEXT CLICKED")

        time.sleep(2)

        # =============================================
        # UPDATE GROUP
        # =============================================

        exam.update_group_save()

        print("GROUP UPDATED")

        time.sleep(2)

        # =============================================
        # UPDATE EXAM
        # =============================================

        exam.update_exam()

        print("EXAM UPDATE CLICKED")

        time.sleep(3)

        # =============================================
        # VERIFY SUCCESS MESSAGE
        # =============================================

        exam.verify_update_success()

        print("UPDATE SUCCESS MESSAGE VERIFIED")

        # =============================================
        # VERIFY UPDATED EXAM IN TABLE
        # =============================================

        exam.verify_updated_exam()

        print("UPDATED EXAM VERIFIED")

        print("EDIT EXAM TEST PASSED")

    finally:

        # =============================================
        # CLOSE BROWSER
        # =============================================

        driver.quit()