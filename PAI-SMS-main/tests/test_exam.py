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
# LOGIN FUNCTION
# =====================================================

def login(driver):

    driver.get(LOGIN_URL)

    login_page = LoginPage(driver)

    login_page.login(
        USERNAME,
        PASSWORD
    )

    wait = WebDriverWait(driver, 20)

    # Verify Dashboard
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

    time.sleep(2)


# =====================================================
# TC_EXAM_001
# CREATE EXAM
# =====================================================

def test_create_exam():

    # =================================================
    # LAUNCH BROWSER
    # =================================================

    driver = webdriver.Chrome()

    driver.maximize_window()

    try:

        # =================================================
        # LOGIN
        # =================================================

        login(driver)

        # =================================================
        # CREATE EXAM PAGE OBJECT
        # =================================================

        exam = ExamPage(driver)

        # =================================================
        # OPEN EXAM MODULE
        # =================================================

        exam.open_exam_page()

        print("EXAM PAGE OPENED")

        time.sleep(2)

        # =================================================
        # OPEN ADD EXAM
        # =================================================

        exam.click_add_exam()

        print("ADD EXAM POPUP OPENED")

        time.sleep(2)

        # =================================================
        # FILL EXAM DETAILS
        # =================================================

        exam.fill_exam_details(

            course="Flute",

            grade="10",

            exam_type="Practical",

            date="2026-11-12",

            start="08:00",

            end="10:00"

        )

        print("EXAM DETAILS ENTERED")

        time.sleep(2)

        # =================================================
        # CREATE GROUP
        # =================================================

        exam.create_group(

            student_name="hfgf fhfh",

            group_name="Floo"

        )

        print("EXAM GROUP CREATED")

        time.sleep(2)

        # =================================================
        # SAVE EXAM
        # =================================================

        exam.save_exam()

        print("EXAM SAVED")

        time.sleep(5)

        # =================================================
        # VERIFY EXAM CREATED
        # =================================================

        exam.verify_exam_created(

            course="Flute",

            group_name="Floo"

        )

        print("EXAM CREATED SUCCESSFULLY")

    finally:

        # =================================================
        # CLOSE BROWSER
        # =================================================

        driver.quit()