from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time


class TeacherPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 25)

    # =====================================================
    # LOCATORS
    # =====================================================

    # Users menu
    users_menu = (
        By.XPATH,
        "//span[text()='Users']"
    )

    # Add User
    add_user_button = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div[1]/div[2]/button"
    )

    # -----------------------------------------------------
    # STEP 1 - PERSONAL INFORMATION
    # -----------------------------------------------------

    role_dropdown = (
        By.ID,
        "role"
    )

    salutation_dropdown = (
        By.ID,
        "salutation"
    )

    first_name_input = (
        By.ID,
        "first_name"
    )

    last_name_input = (
        By.ID,
        "last_name"
    )

    # DOB
    dob_input = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div[5]/div/div[3]/div/div/div[2]/div[3]/div[1]/div/div/div/input"
    )

    # Date picker
    month_dropdown = (
        By.XPATH,
        "//select[contains(@class,'month-select')]"
    )

    year_dropdown = (
        By.XPATH,
        "//select[contains(@class,'year-select')]"
    )

    gender_dropdown = (
        By.ID,
        "gender"
    )

    # Step 1 Next
    next_personal_button = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div[5]/div/div[4]/div/button"
    )

    # -----------------------------------------------------
    # STEP 2 - CONTACT INFORMATION
    # -----------------------------------------------------

    phone_input = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div[5]/div/div[3]/div/div/div/div[1]/div[1]/input"
    )

    email_input = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div[5]/div/div[3]/div/div/div/div[2]/div[1]/div/input"
    )

    ice_contact_input = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div[5]/div/div[3]/div/div/div/div[1]/div[2]/input"
    )

    address_input = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div[5]/div/div[3]/div/div/div/div[2]/div[2]/textarea"
    )

    # Step 2 -> Summary Next
    next_contact_button = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div[5]/div/div[4]/button[2]"
    )

    # -----------------------------------------------------
    # SUMMARY
    # -----------------------------------------------------

    save_button = (
        By.XPATH,
        "/html/body/div[4]/div/div/div/div[2]/button[1]"
    )

    # =====================================================
    # COMMON CLICK METHOD
    # =====================================================

    def safe_click(self, locator):

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        time.sleep(0.5)

        try:
            element.click()

        except ElementClickInterceptedException:

            self.driver.execute_script(
                "arguments[0].click();",
                element
            )

    # =====================================================
    # OPEN USERS PAGE
    # =====================================================

    def open_users_page(self):

        self.safe_click(
            self.users_menu
        )

        self.wait.until(
            EC.presence_of_element_located(
                self.add_user_button
            )
        )

    # =====================================================
    # CLICK ADD USER
    # =====================================================

    def click_add_user(self):

        self.safe_click(
            self.add_user_button
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.role_dropdown
            )
        )

    # =====================================================
    # SELECT ROLE
    # =====================================================

    def select_role(self, role):

        dropdown = self.wait.until(
            EC.visibility_of_element_located(
                self.role_dropdown
            )
        )

        Select(dropdown).select_by_visible_text(
            role
        )

    # =====================================================
    # SELECT SALUTATION
    # =====================================================

    def select_salutation(self, salutation):

        dropdown = self.wait.until(
            EC.visibility_of_element_located(
                self.salutation_dropdown
            )
        )

        Select(dropdown).select_by_visible_text(
            salutation
        )

    # =====================================================
    # ENTER NAME
    # =====================================================

    def enter_name(self, first_name, last_name):

        first = self.wait.until(
            EC.visibility_of_element_located(
                self.first_name_input
            )
        )

        first.clear()
        first.send_keys(first_name)

        last = self.wait.until(
            EC.visibility_of_element_located(
                self.last_name_input
            )
        )

        last.clear()
        last.send_keys(last_name)

    # =====================================================
    # SELECT DOB
    # =====================================================

    def select_dob(self, year, month, day):

        # -------------------------------------------------
        # Open date picker
        # -------------------------------------------------

        dob = self.wait.until(
            EC.element_to_be_clickable(
                self.dob_input
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            dob
        )

        time.sleep(1)

        dob.click()

        time.sleep(1)

        # -------------------------------------------------
        # Select Year
        # -------------------------------------------------

        year_dropdown = self.wait.until(
            EC.visibility_of_element_located(
                self.year_dropdown
            )
        )

        Select(
            year_dropdown
        ).select_by_value(
            str(year)
        )

        time.sleep(0.5)

        # -------------------------------------------------
        # Select Month
        # -------------------------------------------------

        month_dropdown = self.wait.until(
            EC.visibility_of_element_located(
                self.month_dropdown
            )
        )

        Select(
            month_dropdown
        ).select_by_visible_text(
            month
        )

        time.sleep(1)

        # -------------------------------------------------
        # Select Day
        # -------------------------------------------------

        day_xpath = (
            "//div[contains(@class,'react-datepicker__day') "
            "and not(contains(@class,'outside-month')) "
            f"and normalize-space(text())='{day}']"
        )

        day_element = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, day_xpath)
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            day_element
        )

        time.sleep(0.5)

        day_element.click()

        # -------------------------------------------------
        # Verify DOB
        # -------------------------------------------------

        self.wait.until(
            lambda d:
            d.find_element(
                *self.dob_input
            ).get_attribute("value")
            not in (
                None,
                "",
                "MM/DD/YYYY"
            )
        )

        dob_value = self.driver.find_element(
            *self.dob_input
        ).get_attribute("value")

        print(
            f"DOB SELECTED: {dob_value}"
        )

    # =====================================================
    # SELECT GENDER
    # =====================================================

    def select_gender(self, gender):

        dropdown = self.wait.until(
            EC.visibility_of_element_located(
                self.gender_dropdown
            )
        )

        Select(
            dropdown
        ).select_by_visible_text(
            gender
        )

        time.sleep(1)

        # -------------------------------------------------
        # Verify DOB was not cleared
        # -------------------------------------------------

        dob_value = self.driver.find_element(
            *self.dob_input
        ).get_attribute("value")

        print(
            f"DOB AFTER GENDER SELECTION: {dob_value}"
        )

        if not dob_value:
            raise AssertionError(
                "DOB was cleared after selecting gender"
            )

    # =====================================================
    # COMPLETE PERSONAL INFORMATION
    # =====================================================

    def fill_personal_information(
        self,
        role,
        salutation,
        first_name,
        last_name,
        year,
        month,
        day,
        gender
    ):

        # Role
        self.select_role(
            role
        )

        # Salutation
        self.select_salutation(
            salutation
        )

        # Name
        self.enter_name(
            first_name,
            last_name
        )

        # DOB
        self.select_dob(
            year,
            month,
            day
        )

        # Gender
        self.select_gender(
            gender
        )

        print(
            "PERSONAL INFORMATION ENTERED"
        )

    # =====================================================
    # STEP 1 -> STEP 2
    # =====================================================

    def click_next_personal(self):

        # Final DOB check
        dob_value = self.driver.find_element(
            *self.dob_input
        ).get_attribute("value")

        print(
            f"DOB BEFORE PERSONAL NEXT: {dob_value}"
        )

        if not dob_value:
            raise AssertionError(
                "DOB is empty before clicking Personal Next"
            )

        self.safe_click(
            self.next_personal_button
        )

        time.sleep(2)

        # Wait for contact field
        self.wait.until(
            EC.visibility_of_element_located(
                self.phone_input
            )
        )

        print(
            "MOVED TO CONTACT INFORMATION"
        )

    # =====================================================
    # ENTER CONTACT INFORMATION
    # =====================================================

    def enter_contact_information(
        self,
        phone,
        email,
        ice_contact,
        address
    ):

        # Phone
        phone_field = self.wait.until(
            EC.visibility_of_element_located(
                self.phone_input
            )
        )

        phone_field.clear()
        phone_field.send_keys(
            phone
        )

        # Email
        email_field = self.wait.until(
            EC.visibility_of_element_located(
                self.email_input
            )
        )

        email_field.clear()
        email_field.send_keys(
            email
        )

        # ICE Contact
        ice_field = self.wait.until(
            EC.visibility_of_element_located(
                self.ice_contact_input
            )
        )

        ice_field.clear()
        ice_field.send_keys(
            ice_contact
        )

        # Address
        address_field = self.wait.until(
            EC.visibility_of_element_located(
                self.address_input
            )
        )

        address_field.clear()
        address_field.send_keys(
            address
        )

        print(
            "CONTACT INFORMATION ENTERED"
        )

    # =====================================================
    # STEP 2 -> SUMMARY
    # =====================================================

    def click_contact_next(self):

        next_button = self.wait.until(
            EC.element_to_be_clickable(
                self.next_contact_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            next_button
        )

        time.sleep(1)

        try:

            next_button.click()

        except ElementClickInterceptedException:

            self.driver.execute_script(
                "arguments[0].click();",
                next_button
            )

        time.sleep(2)

        print(
            "MOVED TO SUMMARY"
        )

    # =====================================================
    # SAVE FROM SUMMARY
    # =====================================================

    def click_save(self):

        save_button = self.wait.until(
            EC.element_to_be_clickable(
                self.save_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            save_button
        )

        time.sleep(1)

        try:

            save_button.click()

        except ElementClickInterceptedException:

            self.driver.execute_script(
                "arguments[0].click();",
                save_button
            )

        time.sleep(3)

        print(
            "TEACHER SAVE BUTTON CLICKED"
        )

