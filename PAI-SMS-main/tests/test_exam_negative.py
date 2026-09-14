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

    time.sleep(2)


# =====================================================
# TC_Exam_NEG_001
# Empty Course + Empty Grade Validation
# =====================================================

def test_empty_course_validation():

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

        time.sleep(2)

        # =============================================
        # OPEN ADD EXAM
        # =============================================

        exam.click_add_exam()

        print("ADD EXAM POPUP OPENED")

        time.sleep(2)

        # =============================================
        # LEAVE COURSE EMPTY
        # LEAVE GRADE EMPTY
        # =============================================

        exam.fill_exam_details_negative(

            exam_type="Theory",

            date="2027-09-18",

            start="09:00",

            end="10:00"

        )

        print("COURSE AND GRADE LEFT EMPTY")

        time.sleep(2)

        # =============================================
        # CLICK CREATE GROUP
        # =============================================

        exam.click(
            exam.CREATE_GROUP_BUTTON
        )

        print("CREATE GROUP CLICKED")

        time.sleep(2)

        # =============================================
        # VERIFY VALIDATION
        # =============================================

        exam.verify_empty_course_validation()

        print(
            "EMPTY COURSE AND GRADE VALIDATION VERIFIED"
        )

    finally:

        # =============================================
        # CLOSE BROWSER
        # =============================================

        driver.quit()


# =====================================================
# TC_Exam_NEG_002
# Empty Grade Validation
# =====================================================

def test_empty_grade_validation():

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

        time.sleep(2)

        # =============================================
        # OPEN ADD EXAM
        # =============================================

        exam.click_add_exam()

        print("ADD EXAM POPUP OPENED")

        time.sleep(2)

        # =============================================
        # SELECT COURSE
        # =============================================

        exam.select_dropdown(
            exam.COURSE,
            "Keyboard"
        )

        print("COURSE SELECTED")

        # =============================================
        # GRADE LEFT EMPTY
        # =============================================

        print("GRADE LEFT EMPTY")

        # =============================================
        # SELECT EXAM TYPE
        # =============================================

        exam.select_dropdown(
            exam.EXAM_TYPE,
            "Theory"
        )

        print("EXAM TYPE SELECTED")

        # =============================================
        # ENTER EXAM DATE
        # =============================================

        exam.enter_text(
            exam.EXAM_DATE,
            "2027-09-18"
        )

        print("EXAM DATE ENTERED")

        # =============================================
        # ENTER START TIME
        # =============================================

        exam.enter_text(
            exam.START_TIME,
            "09:00"
        )

        print("START TIME ENTERED")

        # =============================================
        # ENTER END TIME
        # =============================================

        exam.enter_text(
            exam.END_TIME,
            "10:00"
        )

        print("END TIME ENTERED")

        time.sleep(2)

        # =============================================
        # CLICK CREATE GROUP
        # =============================================

        exam.click(
            exam.CREATE_GROUP_BUTTON
        )

        print("CREATE GROUP CLICKED")

        time.sleep(2)

        # =============================================
        # VERIFY GRADE VALIDATION
        # =============================================

        exam.verify_empty_grade_validation()

        print(
            "EMPTY GRADE VALIDATION VERIFIED"
        )

    finally:

        # =============================================
        # CLOSE BROWSER
        # =============================================

        driver.quit()