import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage


class SchedulePage(BasePage):

    # =========================================================
    # NAVIGATION
    # =========================================================

    SCHEDULE_MENU = (
        By.XPATH,
        "//span[normalize-space()='Schedule']"
    )

    # =========================================================
    # MAIN PAGE
    # =========================================================

    SEARCH_BOX = (
        By.CSS_SELECTOR,
        "input[placeholder='Search...']"
    )

    ADD_BUTTON = (
        By.CSS_SELECTOR,
        "button.schedule-add-btn"
    )

    TABLE_ROWS = (
        By.CSS_SELECTOR,
        "tbody tr"
    )

    # =========================================================
    # ADD / EDIT MODAL
    # =========================================================

    MODAL = (
        By.CSS_SELECTOR,
        ".addScheduleForm-modal-content"
    )

    CLOSE_BUTTON = (
        By.CSS_SELECTOR,
        "img.addScheduleForm-cancel-icon"
    )

    # =========================================================
    # FORM FIELDS
    # =========================================================

    BRANCH = (
        By.ID,
        "branch_id"
    )

    LECTURER = (
        By.ID,
        "user_id"
    )

    COURSE = (
        By.ID,
        "course_id"
    )

    GRADE = (
        By.ID,
        "grade_id"
    )

    DAY = (
        By.CSS_SELECTOR,
        ".addScheduleForm-dropdown-toggle"
    )

    START_TIME = (
        By.ID,
        "startTime"
    )

    END_TIME = (
        By.ID,
        "endTime"
    )

    # =========================================================
    # BUTTONS
    # =========================================================

    ADD_FORM_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'addScheduleForm-button-btn') "
        "and normalize-space()='Add Schedule']"
    )

    UPDATE_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Update']"
    )

    FINAL_SUBMIT = (
        By.CSS_SELECTOR,
        "button.addScheduleForm-submit-btn"
    )

    # =========================================================
    # TABLE ICONS
    # =========================================================

    EDIT_ICON = (
        By.XPATH,
        "(//img[@alt='Edit'])[1]"
    )

    DELETE_ICON = (
        By.XPATH,
        "(//img[@alt='Delete'])[1]"
    )

    VIEW_ICON = (
        By.XPATH,
        "(//img[@alt='View'])[1]"
    )

    # =========================================================
    # DELETE MODAL
    # =========================================================

    DELETE_MODAL = (
        By.CSS_SELECTOR,
        ".DeleteModal-content"
    )

    DELETE_CONFIRM = (
        By.CSS_SELECTOR,
        "button.DeleteModal-delete"
    )

    # =========================================================
    # SUCCESS MESSAGE
    # =========================================================

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//*[contains(translate(.,"
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
        "'abcdefghijklmnopqrstuvwxyz'),"
        "'schedule updated successfully')]"
    )

    # =========================================================
    # OPEN SCHEDULE
    # =========================================================

    def open_schedule(self):

        menu = self.wait.until(
            EC.element_to_be_clickable(
                self.SCHEDULE_MENU
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            menu
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_BOX
            )
        )

    # =========================================================
    # SEARCH
    # =========================================================

    def search_schedule(self, text):

        box = self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_BOX
            )
        )

        box.clear()
        box.send_keys(text)

        time.sleep(1)

    # =========================================================
    # OPEN ADD SCHEDULE POPUP
    # =========================================================

    def click_add_schedule(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.MODAL
            )
        )

    # =========================================================
    # CHECK ADD POPUP
    # =========================================================

    def is_add_popup_visible(self):

        try:

            return self.wait.until(
                EC.visibility_of_element_located(
                    self.MODAL
                )
            ).is_displayed()

        except TimeoutException:

            return False

    # =========================================================
    # GENERIC DROPDOWN
    # =========================================================

    def select_dropdown(self, locator, value):

        element = self.wait.until(
            EC.presence_of_element_located(
                locator
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        dropdown = Select(element)

        value = str(value).strip().lower()

        # -----------------------------------------------------
        # First try visible text
        # -----------------------------------------------------

        for option in dropdown.options:

            option_text = option.text.strip().lower()

            if option_text == value:

                option_value = option.get_attribute(
                    "value"
                )

                dropdown.select_by_value(
                    option_value
                )

                return

        # -----------------------------------------------------
        # Try partial visible text
        # -----------------------------------------------------

        for option in dropdown.options:

            option_text = option.text.strip().lower()

            if value in option_text:

                option_value = option.get_attribute(
                    "value"
                )

                dropdown.select_by_value(
                    option_value
                )

                return

        # -----------------------------------------------------
        # Try option value
        # -----------------------------------------------------

        for option in dropdown.options:

            option_value = (
                option.get_attribute("value")
                or ""
            ).strip().lower()

            if option_value == value:

                dropdown.select_by_value(
                    option.get_attribute("value")
                )

                return

        # -----------------------------------------------------
        # Debug available options
        # -----------------------------------------------------

        available = [
            option.text.strip()
            for option in dropdown.options
        ]

        raise Exception(
            f"'{value}' not found in dropdown. "
            f"Available options: {available}"
        )

    # =========================================================
    # WAIT FOR GRADE
    # =========================================================

    def wait_grade_loaded(self):

        self.wait.until(
            lambda driver:
            len(
                Select(
                    driver.find_element(
                        *self.GRADE
                    )
                ).options
            ) > 1
        )

    # =========================================================
    # SELECT DAY
    # =========================================================

    def select_day(self, day):

        dropdown = self.wait.until(
            EC.element_to_be_clickable(
                self.DAY
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            dropdown
        )

        checkbox = (
            By.XPATH,
            f"//input[@value='{day}']"
        )

        box = self.wait.until(
            EC.presence_of_element_located(
                checkbox
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            box
        )

        if not box.is_selected():

            self.driver.execute_script(
                "arguments[0].click();",
                box
            )

    # =========================================================
    # ENTER TEXT
    # =========================================================

    def enter_text(self, locator, value):

        field = self.wait.until(
            EC.visibility_of_element_located(
                locator
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            field
        )

        field.clear()
        field.send_keys(value)

    # =========================================================
    # FILL SCHEDULE
    # =========================================================

    def fill_schedule(
        self,
        branch,
        lecturer,
        course,
        grade,
        day,
        start_time,
        end_time
    ):

        # Branch
        self.select_dropdown(
            self.BRANCH,
            branch
        )

        # Lecturer
        self.select_dropdown(
            self.LECTURER,
            lecturer
        )

        # Course
        self.select_dropdown(
            self.COURSE,
            course
        )

        # Grade depends on Course
        self.wait_grade_loaded()

        self.select_dropdown(
            self.GRADE,
            grade
        )

        # Day
        self.select_day(
            day
        )

        # Start time
        self.enter_text(
            self.START_TIME,
            start_time
        )

        # End time
        self.enter_text(
            self.END_TIME,
            end_time
        )

    # =========================================================
    # ADD SCHEDULE
    # =========================================================

    def click_add_form_button(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_FORM_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        time.sleep(3)

    # =========================================================
    # EDIT
    # =========================================================

    def click_edit(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.EDIT_ICON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.UPDATE_BUTTON
            )
        )

    # =========================================================
    # CHANGE START TIME
    # =========================================================

    def change_start_time(self, new_time):

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.START_TIME
            )
        )

        field.clear()
        field.send_keys(new_time)

    # =========================================================
    # UPDATE
    # =========================================================

    def click_update(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.UPDATE_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )



    # =========================================================
    # DELETE ICON
    # =========================================================

    def click_delete_icon(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.DELETE_ICON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.DELETE_MODAL
            )
        )

    # =========================================================
    # DELETE MODAL CHECK
    # =========================================================

    def is_delete_modal_visible(self):

        try:

            return self.wait.until(
                EC.visibility_of_element_located(
                    self.DELETE_MODAL
                )
            ).is_displayed()

        except TimeoutException:

            return False

    # =========================================================
    # CONFIRM DELETE
    # =========================================================

    def confirm_delete(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.DELETE_CONFIRM
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        self.wait.until(
            EC.invisibility_of_element_located(
                self.DELETE_MODAL
            )
        )

    # =========================================================
    # DELETE SCHEDULE
    # =========================================================

    def delete_schedule(self):

        self.click_delete_icon()

        self.confirm_delete()

        time.sleep(3)

    # =========================================================
    # VIEW
    # =========================================================

    def view_schedule(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.VIEW_ICON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button

        )

        time.sleep(2)

    # =========================================================
    # CLOSE POPUP
    # =========================================================

    def close_popup(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.CLOSE_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        self.wait.until(
            EC.invisibility_of_element_located(
                self.MODAL
            )
        )

    # =========================================================
    # TABLE ROW COUNT
    # =========================================================

    def get_row_count(self):

        return len(
            self.driver.find_elements(
                *self.TABLE_ROWS
            )
        )

    # =========================================================
    # TABLE VISIBLE
    # =========================================================

    def is_schedule_table_visible(self):

        return self.get_row_count() > 0

    # =========================================================
    # SUCCESS MESSAGE
    # =========================================================

    def get_success_message(self):

        try:

            message = self.wait.until(
                EC.visibility_of_element_located(
                    self.SUCCESS_MESSAGE
                )
            )

            return message.text.strip()

        except TimeoutException:

            return ""