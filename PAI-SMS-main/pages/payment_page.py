import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class PaymentPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # ==================================================
    # LOCATORS
    # ==================================================

    # Payment menu
    payment_menu = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[1]/div/div[2]/a[6]"
    )

    # Add Payment button
    add_payment_button = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div[1]/button"
    )

    # Student search input
    search_student = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div[4]/div/div[3]/div/div[1]/input"
    )

    # Student search result
    student_result = (
        By.XPATH,
        "//*[contains(normalize-space(),'Muzzamil')]"
    )

    # Step 1 Next button
    next_button_1 = (
        By.XPATH,
        "//button[normalize-space()='Next']"
    )

    # March month
    month_button = (
        By.XPATH,
        "//button[normalize-space()='March']"
    )

    # Step 2 Next button
    next_button_2 = (
        By.XPATH,
        "//button[normalize-space()='Next']"
    )

    # Submit button
    submit_payment_button = (
        By.XPATH,
        "//button[normalize-space()='Submit Payment' "
        "or normalize-space()='Submit']"
    )

    # Generate Receipt
    generate_receipt_button = (
        By.XPATH,
        "//button[contains(normalize-space(),'Generate Receipt') "
        "or contains(normalize-space(),'Receipt')]"
    )

    # ==================================================
    # OPEN PAYMENT
    # ==================================================

    def open_payment(self):

        payment = self.wait.until(
            EC.element_to_be_clickable(
                self.payment_menu
            )
        )

        payment.click()

        time.sleep(3)

        print("PAYMENT PAGE OPENED")

    # ==================================================
    # ADD PAYMENT
    # ==================================================

    def click_add_payment(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.add_payment_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        time.sleep(1)

        button.click()

        time.sleep(3)

        print("ADD PAYMENT POPUP OPENED")

    # ==================================================
    # SEARCH STUDENT
    # ==================================================

    def search_student_name(self, student):

        search = self.wait.until(
            EC.visibility_of_element_located(
                self.search_student
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            search
        )

        search.click()
        search.clear()

        search.send_keys(student)

        time.sleep(3)

        print(
            f"STUDENT NAME ENTERED: {student}"
        )

    # ==================================================
    # SELECT STUDENT
    # ==================================================

    def select_student(self):

        student = self.wait.until(
            EC.element_to_be_clickable(
                self.student_result
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            student
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            student
        )

        time.sleep(3)

        print("STUDENT SELECTED")

    # ==================================================
    # STEP 1 NEXT
    # ==================================================

    def click_next_step_1(self):

        buttons = self.wait.until(
            EC.presence_of_all_elements_located(
                self.next_button_1
            )
        )

        for button in buttons:

            if (
                button.is_displayed()
                and button.is_enabled()
            ):

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    button
                )

                time.sleep(1)

                self.driver.execute_script(
                    "arguments[0].click();",
                    button
                )

                time.sleep(4)

                print("NEXT STEP 1 COMPLETED")

                return

        raise TimeoutException(
            "Step 1 Next button was not available."
        )

    # ==================================================
    # SELECT PAYMENT MONTH
    # ==================================================

    def select_payment_month(self):

        month = self.wait.until(
            EC.element_to_be_clickable(
                self.month_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            month
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            month
        )

        time.sleep(3)

        print("MARCH MONTH SELECTED")

    # ==================================================
    # STEP 2 NEXT
    # ==================================================

    def click_next_step_2(self):

        buttons = self.wait.until(
            EC.presence_of_all_elements_located(
                self.next_button_2
            )
        )

        visible_buttons = []

        for button in buttons:

            if (
                button.is_displayed()
                and button.is_enabled()
            ):
                visible_buttons.append(button)

        if not visible_buttons:

            raise TimeoutException(
                "Step 2 Next button was not available."
            )

        next_button = visible_buttons[-1]

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            next_button
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            next_button
        )

        time.sleep(4)

        print("NEXT STEP 2 COMPLETED")

    # ==================================================
    # SUBMIT PAYMENT
    # ==================================================

    def submit_payment(self):

        submit = self.wait.until(
            EC.element_to_be_clickable(
                self.submit_payment_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            submit
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            submit
        )

        time.sleep(5)

        print("PAYMENT SUBMITTED")

    # ==================================================
    # GENERATE RECEIPT
    # ==================================================

    def generate_receipt(self):

        receipt = self.wait.until(
            EC.element_to_be_clickable(
                self.generate_receipt_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            receipt
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            receipt
        )

        time.sleep(5)

        print("RECEIPT GENERATED")