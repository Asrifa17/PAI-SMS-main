from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage

import time


def test_teacher_empty_personal_information():

    # =====================================================
    # LAUNCH BROWSER
    # =====================================================

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(
        "https://aradanaqa.pineappleai.cloud/login"
    )

    try:

        wait = WebDriverWait(driver, 20)

        # =================================================
        # LOGIN
        # =================================================

        login = LoginPage(driver)

        login.login(
            "admin",
            "admin123"
        )

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

        # =================================================
        # OPEN USERS PAGE
        # =================================================

        users_menu = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//span[text()='Users']"
                )
            )
        )

        driver.execute_script(
            "arguments[0].click();",
            users_menu
        )

        print("USERS PAGE OPENED")

        # =================================================
        # CLICK ADD USER
        # =================================================

        add_user = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="root"]/div/div[2]/div[2]/main/div/div[1]/div[2]/button'
                )
            )
        )

        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            add_user
        )

        driver.execute_script(
            "arguments[0].click();",
            add_user
        )

        print("ADD USER POPUP OPENED")

        # =================================================
        # VERIFY REGISTRATION POPUP
        # =================================================

        registration = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//*[normalize-space()='Registration']"
                )
            )
        )

        assert registration.is_displayed()

        print("REGISTRATION FORM DISPLAYED")

        # =================================================
        # DO NOT ENTER ANY DATA
        # =================================================
        #
        # Role       = Empty
        # Salutation = Empty
        # First Name = Empty
        # Last Name  = Empty
        # DOB        = Empty
        # Gender     = Empty
        #
        # =================================================

        # =================================================
        # CLICK NEXT
        # =================================================

        next_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="root"]/div/div[2]/div[2]/main/div/div[5]/div/div[4]/div/button'
                )
            )
        )

        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            next_button
        )

        driver.execute_script(
            "arguments[0].click();",
            next_button
        )

        print("NEXT CLICKED WITH EMPTY PERSONAL INFORMATION")

        # =================================================
        # VALIDATION ERROR TOAST
        # =================================================

        validation_error = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//*[normalize-space()='Validation Error']"
                )
            )
        )

        assert validation_error.is_displayed()

        print("VALIDATION ERROR TOAST DISPLAYED")

        # =================================================
        # VERIFY VALIDATION MESSAGE
        # =================================================

        fix_message = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//*[normalize-space()='Fix highlighted fields']"
                )
            )
        )

        assert fix_message.is_displayed()

        print("FIX HIGHLIGHTED FIELDS MESSAGE DISPLAYED")

        # =================================================
        # VERIFY REQUIRED VALIDATIONS
        # =================================================

        required_messages = wait.until(
            EC.visibility_of_all_elements_located(
                (
                    By.XPATH,
                    "//*[normalize-space()='Required']"
                )
            )
        )

        # According to the current UI:
        #
        # Role       -> Required
        # First Name -> Required
        # Last Name  -> Required
        # DOB        -> Required
        #
        assert len(required_messages) >= 4

        print(
            f"REQUIRED VALIDATIONS DISPLAYED: "
            f"{len(required_messages)}"
        )

        # =================================================
        # VERIFY STILL ON PERSONAL INFORMATION
        # =================================================

        personal_information = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//*[normalize-space()='Personal Information']"
                )
            )
        )

        assert personal_information.is_displayed()

        print(
            "USER REMAINED ON PERSONAL INFORMATION STEP"
        )

        print(
            "NEGATIVE TEST PASSED - "
            "EMPTY PERSONAL INFORMATION VALIDATION"
        )

    finally:

        time.sleep(3)
        driver.quit()