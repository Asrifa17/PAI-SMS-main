from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


class BranchNegativePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # =====================================================
    # LOCATORS
    # =====================================================

    branch_menu = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[1]/div/div[2]/a[3]'
    )

    add_branch_button = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[1]/div[2]/button'
    )

    country_dropdown = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[3]/div/form/div[1]/div[1]/select'
    )

    branch_name_input = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[3]/div/form/div[1]/div[2]/input'
    )

    # Add Branch inside form
    add_branch_submit_button = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[3]/div/form/div[3]/button'
    )

    # =====================================================
    # OPEN BRANCH PAGE
    # =====================================================

    def open_branch_page(self):

        branch = self.wait.until(
            EC.element_to_be_clickable(self.branch_menu)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            branch
        )

        time.sleep(2)

    # =====================================================
    # OPEN ADD BRANCH FORM
    # =====================================================

    def open_add_branch(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.add_branch_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.country_dropdown
            )
        )

        time.sleep(1)

    # =====================================================
    # SELECT COUNTRY
    # =====================================================

    def select_country(self, country):

        dropdown_element = self.wait.until(
            EC.visibility_of_element_located(
                self.country_dropdown
            )
        )

        dropdown = Select(dropdown_element)

        dropdown.select_by_visible_text(country)

    # =====================================================
    # ENTER BRANCH NAME
    # =====================================================

    def enter_branch_name(self, branch_name):

        branch = self.wait.until(
            EC.visibility_of_element_located(
                self.branch_name_input
            )
        )

        branch.clear()
        branch.send_keys(branch_name)

    # =====================================================
    # CLICK ADD BRANCH
    # =====================================================

    def click_add_branch(self):

        button = self.wait.until(
            EC.presence_of_element_located(
                self.add_branch_submit_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        time.sleep(2)

    # =====================================================
    # GET FORM VALIDATION TEXT
    # =====================================================

    def get_validation_messages(self):

        # Collect visible validation/error messages
        elements = self.driver.find_elements(
            By.XPATH,
            "//form//*[self::p or self::span or self::div]"
        )

        messages = []

        for element in elements:

            try:

                if element.is_displayed():

                    text = element.text.strip()

                    if text:
                        messages.append(text)

            except:
                pass

        return messages

    # =====================================================
    # CHECK ADD BUTTON STATE
    # =====================================================

    def is_add_button_disabled(self):

        button = self.wait.until(
            EC.presence_of_element_located(
                self.add_branch_submit_button
            )
        )

        return button.get_attribute("disabled") is not None