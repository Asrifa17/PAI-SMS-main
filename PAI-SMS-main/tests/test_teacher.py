from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.teacher_page import TeacherPage

import time


def test_teacher_registration():

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

        # =================================================
        # LOGIN
        # =================================================

        login = LoginPage(driver)

        login.login(
            "admin",
            "admin123"
        )

        wait = WebDriverWait(
            driver,
            20
        )

        # Verify Dashboard
        dashboard = wait.until(
            EC.presence_of_element_located(
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
        # TEACHER PAGE OBJECT
        # =================================================

        teacher = TeacherPage(
            driver
        )

        # =================================================
        # OPEN USERS PAGE
        # =================================================

        teacher.open_users_page()

        print(
            "USERS PAGE OPENED"
        )

        time.sleep(2)

        # =================================================
        # CLICK ADD USER
        # =================================================

        teacher.click_add_user()

        print(
            "ADD USER POPUP OPENED"
        )

        time.sleep(2)

        # =================================================
        # STEP 1 - PERSONAL INFORMATION
        # =================================================

        teacher.fill_personal_information(
            role="Teacher",
            salutation="Mr",
            first_name="Kamal",
            last_name="Perera",
            year="2010",
            month="January",
            day="19",
            gender="Male"
        )

        print(
            "PERSONAL INFORMATION ENTERED"
        )

        # =================================================
        # STEP 1 -> STEP 2
        # =================================================

        teacher.click_next_personal()

        print(
            "PERSONAL INFORMATION NEXT SUCCESSFUL"
        )

        # =================================================
        # STEP 2 - CONTACT INFORMATION
        # =================================================

        teacher.enter_contact_information(
            phone="+94778657989",
            email="teacherkamal.test@gmail.com",
            ice_contact="+94771434567",
            address="Colombo, Sri Lanka"
        )

        print(
            "CONTACT INFORMATION ENTERED"
        )

        # =================================================
        # STEP 2 -> SUMMARY
        # =================================================

        teacher.click_contact_next()

        print(
            "CONTACT NEXT SUCCESSFUL"
        )

        time.sleep(2)

        # =================================================
        # SUMMARY -> SAVE
        # =================================================

        teacher.click_save()

        print(
            "TEACHER REGISTERED SUCCESSFULLY"
        )

    finally:

        time.sleep(5)

        driver.quit()