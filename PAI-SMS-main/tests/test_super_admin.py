from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.teacher_page import TeacherPage

import time


def test_super_admin_registration():

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

        # =================================================
        # VERIFY DASHBOARD
        # =================================================

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

        # =================================================
        # TEACHER PAGE OBJECT
        # Using TeacherPage for Super Admin registration
        # =================================================

        super_admin = TeacherPage(driver)

        # =================================================
        # OPEN USERS PAGE
        # =================================================

        super_admin.open_users_page()

        print("USERS PAGE OPENED")

        time.sleep(2)

        # =================================================
        # CLICK ADD USER
        # =================================================

        super_admin.click_add_user()

        print("ADD USER POPUP OPENED")

        time.sleep(2)

        # =================================================
        # STEP 1 - PERSONAL INFORMATION
        # =================================================

        super_admin.fill_personal_information(
            role="Super admin",
            salutation="Ms",
            first_name="Menaka",
            last_name="Perera",
            year="1997",
            month="January",
            day="21",
            gender="Female"
        )

        print("PERSONAL INFORMATION ENTERED")

        # =================================================
        # STEP 1 -> STEP 2
        # =================================================

        super_admin.click_next_personal()

        print("PERSONAL INFORMATION NEXT SUCCESSFUL")

        # =================================================
        # STEP 2 - CONTACT INFORMATION
        # =================================================

        super_admin.enter_contact_information(
            phone="+94768657289",
            email="Menakas.superadmin@gmail.com",
            ice_contact="+94769234567",
            address="Colombo, Sri Lanka"
        )

        print("CONTACT INFORMATION ENTERED")

        # =================================================
        # STEP 2 -> SUMMARY
        # =================================================

        super_admin.click_contact_next()

        print("CONTACT NEXT SUCCESSFUL")

        time.sleep(2)

        # =================================================
        # SUMMARY -> SAVE
        # =================================================

        super_admin.click_save()

        print("SUPER ADMIN REGISTERED SUCCESSFULLY")

    finally:

        # =================================================
        # CLOSE BROWSER
        # =================================================

        time.sleep(5)

        driver.quit()