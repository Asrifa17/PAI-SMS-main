import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.payment_page import PaymentPage


LOGIN_URL = "https://aradanaqa.pineappleai.cloud/login"

USERNAME = "admin"
PASSWORD = "admin123"


# ==================================================
# LOGIN
# ==================================================

def login(driver):

    driver.get(LOGIN_URL)

    login_page = LoginPage(driver)

    login_page.login(
        USERNAME,
        PASSWORD
    )

    time.sleep(3)


# ==================================================
# PAYMENT MODULE
# ==================================================

def test_payment_module():

    # ==================================================
    # LAUNCH BROWSER
    # ==================================================

    driver = webdriver.Chrome()

    driver.maximize_window()

    try:

        # ==================================================
        # LOGIN
        # ==================================================

        login(driver)

        wait = WebDriverWait(driver, 20)

        # ==================================================
        # VERIFY DASHBOARD
        # ==================================================

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

        # ==================================================
        # CREATE PAYMENT PAGE OBJECT
        # ==================================================

        payment = PaymentPage(driver)

        # ==================================================
        # OPEN PAYMENT MODULE
        # ==================================================

        payment.open_payment()

        # ==================================================
        # ADD PAYMENT
        # ==================================================

        payment.click_add_payment()

        # ==================================================
        # SEARCH STUDENT
        # ==================================================

        payment.search_student_name(
            "Muzzamil"
        )

        # ==================================================
        # SELECT STUDENT
        # ==================================================

        payment.select_student()

        # ==================================================
        # STEP 1 -> STEP 2
        # ==================================================

        payment.click_next_step_1()

        # ==================================================
        # SELECT PAYMENT MONTH
        # ==================================================

        payment.select_payment_month()

        # ==================================================
        # STEP 2 -> STEP 3
        # ==================================================

        payment.click_next_step_2()

        # ==================================================
        # SUBMIT PAYMENT
        # ==================================================

        payment.submit_payment()

        # ==================================================
        # GENERATE RECEIPT
        # ==================================================

        payment.generate_receipt()

        print(
            "PAYMENT MODULE AUTOMATION PASSED"
        )

    finally:

        # ==================================================
        # CLOSE BROWSER
        # ==================================================

        driver.quit()