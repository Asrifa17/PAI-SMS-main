from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.teacher_page import TeacherPage

import time


def test_branch_admin_registration():

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

        print("LOGIN SUCCESSFUL")

        # =================================================
        # USER PAGE OBJECT
        # =================================================

        branch_admin = TeacherPage(driver)

        # =================================================
        # OPEN USERS PAGE
        # =================================================

        branch_admin.open_users_page()

        print("USERS PAGE OPENED")

        time.sleep(2)

        # =================================================
        # CLICK ADD USER
        # =================================================

        branch_admin.click_add_user()

        print("ADD USER POPUP OPENED")

        time.sleep(2)

        # =================================================
        # STEP 1 - PERSONAL INFORMATION
        # =================================================

        branch_admin.fill_personal_information(
            role="Branch admin",
            salutation="Ms",
            first_name="Nadeeshani",
            last_name="Perera",
            year="1995",
            month="January",
            day="19",
            gender="Female"
        )

        print("PERSONAL INFORMATION ENTERED")

        # =================================================
        # STEP 1 -> STEP 2
        # =================================================

        branch_admin.click_next_personal()

        print("PERSONAL INFORMATION NEXT SUCCESSFUL")

        # =================================================
        # STEP 2 - CONTACT INFORMATION
        # =================================================

        branch_admin.enter_contact_information(
            phone="+94778657788",
            email="nadeeshani.branchadmin@gmail.com",
            ice_contact="+94771234568",
            address="Colombo, Sri Lanka"
        )

        print("CONTACT INFORMATION ENTERED")

        # =================================================
        # STEP 2 -> SUMMARY
        # =================================================

        branch_admin.click_contact_next()

        print("CONTACT NEXT SUCCESSFUL")

        time.sleep(2)

        # =================================================
        # SUMMARY -> SAVE
        # =================================================

        branch_admin.click_save()

        print("BRANCH ADMIN REGISTERED SUCCESSFULLY")

    finally:

        time.sleep(5)

        driver.quit()