import time

from selenium import webdriver

from pages.login_page import LoginPage
from pages.exam_page import ExamPage


# =====================================================
# LOGIN URL
# =====================================================

LOGIN_URL = "https://aradanaqa.pineappleai.cloud/login"


# =====================================================
# TC_Exam_Search
# Search Exam
# =====================================================

def test_search_exam():

    # =================================================
    # LAUNCH BROWSER
    # =================================================

    driver = webdriver.Chrome()

    driver.maximize_window()

    try:

        # =============================================
        # OPEN WEBSITE
        # =============================================

        driver.get(LOGIN_URL)

        # =============================================
        # LOGIN
        # =============================================

        login = LoginPage(driver)

        login.login(
            "admin",
            "admin123"
        )

        print("LOGIN SUCCESSFUL")

        time.sleep(3)

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
        # SEARCH EXAM
        # =============================================

        exam.search_exam(
            "Keyboard"
        )

        print("EXAM SEARCH PERFORMED")

        time.sleep(2)

        # =============================================
        # VERIFY SEARCH RESULT
        # =============================================

        exam.verify_search_result(
            "keyboard"
        )

        print("SEARCH RESULT VERIFIED")

        print(
            "EXAM SEARCH TEST PASSED"
        )

    finally:

        # =============================================
        # CLOSE BROWSER
        # =============================================

        driver.quit()