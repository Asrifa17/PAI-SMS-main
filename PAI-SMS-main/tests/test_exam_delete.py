from selenium import webdriver

from pages.login_page import LoginPage
from pages.exam_page import ExamPage

import time


# =====================================================
# LOGIN URL
# =====================================================

LOGIN_URL = "https://aradanaqa.pineappleai.cloud/login"


# =====================================================
# TC_Exam_XXX
# Delete Exam
# =====================================================

def test_delete_exam():

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
        # DELETE EXAM
        # =============================================

        exam.delete_exam()

        print("EXAM DELETED SUCCESSFULLY")

        time.sleep(3)

    finally:

        # =============================================
        # CLOSE BROWSER
        # =============================================

        driver.quit()