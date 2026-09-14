from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from pages.login_page import LoginPage
from pages.student_page import StudentPage


def test_student_registration():

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

    try:

        wait = WebDriverWait(
            driver,
            20
        )

        # =================================================
        # LOGIN
        # =================================================

        login = LoginPage(driver)

        login.login(
            "admin",
            "admin123"
        )

        # =================================================
        # VERIFY DASHBOARD
        # =================================================

        dashboard = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//h1[contains(text(),'Dashboard')]"
                )
            )
        )

        assert dashboard.is_displayed()

        print(
            "LOGIN SUCCESSFUL"
        )

        # =================================================
        # USERS PAGE
        # =================================================

        student = StudentPage(
            driver
        )

        student.open_users_page()

        print(
            "USERS PAGE OPENED"
        )

        time.sleep(2)

        # =================================================
        # ADD USER
        # =================================================

        student.click_add_user()

        print(
            "ADD USER POPUP OPENED"
        )

        time.sleep(2)

        # =================================================
        # STEP 1
        # PERSONAL INFORMATION
        # =================================================

        student.fill_personal_information(
            role="Student",
            salutation="Mr",
            first_name="Ashen",
            last_name="Dassanayake",
            year="2005",
            month="January",
            day="15",
            gender="Male"
        )

        print(
            "PERSONAL INFORMATION COMPLETED"
        )

        # =================================================
        # STEP 1 -> STEP 2
        # =================================================

        student.click_next_personal()

        print(
            "CONTACT DETAILS OPENED"
        )

        # =================================================
        # STEP 2
        # CONTACT INFORMATION
        # =================================================

        student.enter_contact_information(
            phone="+94761234567",
            email="dassanayaka.student@gmail.com",
            ice_contact="+94769876543",
            address="Jaffna, Sri Lanka"
        )

        print(
            "CONTACT INFORMATION COMPLETED"
        )

        # =================================================
        # STEP 2 -> STEP 3
        # =================================================

        student.click_next_contact()

        print(
            "EDUCATIONAL RECORDS OPENED"
        )

        # =================================================
        # STEP 3
        # EDUCATIONAL RECORDS
        # =================================================

        student.assign_course(
            course="Cello (Co_05)",
            grade= "06"
        )

        print(
            "COURSE ASSIGNED"
        )

        # =================================================
        # STEP 3 -> STEP 4
        # =================================================

        student.click_next_educational()

        print(
            "ACADEMIC DETAILS OPENED"
        )

        # =================================================
        # STEP 4
        # ACADEMIC DETAILS
        # =================================================

        student.assign_schedule(
            branch="United Kingdom - Oxford",
            student_id="ST-011",
            schedule_day="Monday",
            schedule_time="09:00:00-23:00:00"
        )

        print(
            "SCHEDULE ASSIGNED"
        )

        # =================================================
        # STEP 4 -> SUMMARY
        # =================================================

        student.click_next_academic()

        print(
            "SUMMARY OPENED"
        )

        # =================================================
        # SAVE
        # =================================================

        student.click_save_summary()

        print(
            "STUDENT REGISTRATION COMPLETED"
        )

        time.sleep(5)

    finally:

        # =================================================
        # CLOSE BROWSER
        # =================================================

        driver.quit()