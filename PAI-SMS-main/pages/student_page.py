from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time


class StudentPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 25)

    # =====================================================
    # LOCATORS
    # =====================================================

    # =====================================================
    # USERS MENU
    # =====================================================

    users_menu = (
        By.XPATH,
        "//span[text()='Users']"
    )

    # =====================================================
    # ADD USER
    # =====================================================

    add_user_button = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div[1]/div[2]/button"
    )

    # =====================================================
    # STEP 1 - PERSONAL INFORMATION
    # Same structure as Teacher
    # =====================================================

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

    # -----------------------------------------------------
    # DOB
    # Same working Teacher locator
    # -----------------------------------------------------

    dob_input = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div[5]/div/div[3]/div/div/div[2]/div[3]/div[1]/div/div/div/input"
    )

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

    # -----------------------------------------------------
    # STEP 1 NEXT
    # -----------------------------------------------------

    next_personal_button = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div[5]/div/div[4]/div/button"
    )

    # =====================================================
    # STEP 2 - CONTACT INFORMATION
    # Same as Teacher
    # =====================================================

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

    # -----------------------------------------------------
    # STEP 2 NEXT
    # -----------------------------------------------------

    next_contact_button = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div[5]/div/div[4]/button[2]"
    )

    # =====================================================
    # STEP 3 - EDUCATIONAL RECORDS
    # =====================================================

    course_dropdown = (
        By.ID,
        "course"
    )

    grade_dropdown = (
        By.ID,
        "grade"
    )

    assign_course_button = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div[5]/div/div[3]/div/button"
    )

    # -----------------------------------------------------
    # STEP 3 NEXT
    # -----------------------------------------------------

    next_educational_button = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div[5]/div/div[4]/button[2]"
    )

    # =====================================================
    # STEP 4 - ACADEMIC DETAILS
    # =====================================================

    branch_dropdown = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div[5]/div/div[3]/div/div[1]/div[1]/div/select"
    )

    student_id_input = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div[5]/div/div[3]/div/div[1]/div[2]/div/input"
    )

    schedule_day_dropdown = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div[5]/div/div[3]/div/div[2]/div[1]/div/select"
    )

    schedule_time_dropdown = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div[5]/div/div[3]/div/div[2]/div[2]/div/select"
    )

    assign_schedule_button = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div[5]/div/div[3]/div/button"
    )

    # -----------------------------------------------------
    # STEP 4 NEXT
    # -----------------------------------------------------

    next_academic_button = (
        By.XPATH,
        "//*[@id='root']/div/div[2]/div[2]/main/div/div[5]/div/div[4]/button[2]"
    )

    # =====================================================
    # SAVE SUMMARY
    # =====================================================

    save_summary_button = (
        By.XPATH,
        "/html/body/div[4]/div/div/div/div[2]/button[1]"
    )

    # =====================================================
    # COMMON SAFE CLICK
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

    def enter_name(
        self,
        first_name,
        last_name
    ):

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
    # Same working Teacher implementation
    # =====================================================

    def select_dob(
        self,
        year,
        month,
        day
    ):

        # -------------------------------------------------
        # OPEN DATE PICKER
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
        # SELECT YEAR
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
        # SELECT MONTH
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
        # SELECT DAY
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
        # VERIFY DOB
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
        # VERIFY DOB IS STILL PRESENT
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

        # Names

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

        # -------------------------------------------------
        # FINAL DOB CHECK
        # -------------------------------------------------

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

        # -------------------------------------------------
        # CLICK NEXT
        # -------------------------------------------------

        self.safe_click(
            self.next_personal_button
        )

        time.sleep(2)

        # -------------------------------------------------
        # WAIT FOR CONTACT PAGE
        # -------------------------------------------------

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
    # Same as Teacher
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
    # STEP 2 -> STEP 3
    # CONTACT -> EDUCATIONAL RECORDS
    # =====================================================

    def click_next_contact(self):

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

        # -------------------------------------------------
        # WAIT FOR EDUCATIONAL RECORDS
        # -------------------------------------------------

        self.wait.until(
            EC.visibility_of_element_located(
                self.course_dropdown
            )
        )

        print(
            "MOVED TO EDUCATIONAL RECORDS"
        )

    # =====================================================
    # SELECT COURSE
    # =====================================================

    def select_course(self, course):

        course_dropdown = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[@id='course']")
            )
        )

        Select(course_dropdown).select_by_visible_text(course)

        print("COURSE SELECTED:", course)

    # =====================================================
    # SELECT GRADE
    # =====================================================

    def select_grade(self, grade):

        grade_dropdown = self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "grade")
            )
        )

        # Wait until the requested grade option is available
        self.wait.until(
            lambda driver: driver.find_element(
                By.XPATH,
                f"//select[@id='grade']/option[normalize-space()='{grade}']"
            ).is_displayed()
        )

        # Find the option
        grade_option = self.driver.find_element(
            By.XPATH,
            f"//select[@id='grade']/option[normalize-space()='{grade}']"
        )

        # Get actual value from HTML
        grade_value = grade_option.get_attribute("value")

        print(
            f"GRADE OPTION FOUND: {grade}"
        )

        print(
            f"GRADE VALUE: {grade_value}"
        )

        # Select using actual HTML value
        Select(grade_dropdown).select_by_value(
            grade_value
        )

        print(
            f"GRADE SELECTED: {grade}"
        )

    # =====================================================
    # ASSIGN COURSE
    # =====================================================

    def assign_course(self, course, grade):

        # Select Course
        self.select_course(course)

        # Select Grade
        self.select_grade(grade)

        # Click Assign Course
        assign_course_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//*[@id='root']/div/div[2]/div[2]/main/div/div[5]/div/div[3]/div/button"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            assign_course_button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            assign_course_button
        )

        print("COURSE ASSIGNED:", course, "-", grade)

        time.sleep(2)



    # =====================================================
    # STEP 3 -> STEP 4
    # EDUCATIONAL -> ACADEMIC
    # =====================================================

    def click_next_educational(self):

        next_button = self.wait.until(
            EC.element_to_be_clickable(
                self.next_educational_button
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

        # -------------------------------------------------
        # WAIT FOR ACADEMIC DETAILS
        # -------------------------------------------------

        self.wait.until(
            EC.visibility_of_element_located(
                self.student_id_input
            )
        )

        print(
            "MOVED TO ACADEMIC DETAILS"
        )

    # =====================================================
    # SELECT BRANCH
    # =====================================================

    def select_branch(self, branch):

        branch_dropdown = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "branch")
            )
        )

        self.wait.until(
            lambda driver: len(
                Select(branch_dropdown).options
            ) > 1
        )

        select = Select(branch_dropdown)

        branch_value = str(branch).strip()

        # Find the option by visible text
        for option in select.options:

            option_text = option.text.strip()
            option_value = option.get_attribute("value")

            if option_text == branch_value:
                print(f"BRANCH OPTION FOUND: {option_text}")
                print(f"BRANCH VALUE: {option_value}")

                select.select_by_value(option_value)

                print(f"BRANCH SELECTED: {option_text}")

                return

        raise Exception(
            f"Branch '{branch}' not found. "
            f"Available branches: "
            f"{[(o.text.strip(), o.get_attribute('value')) for o in select.options]}"
        )

    # =====================================================
    # ENTER STUDENT ID
    # =====================================================

    def enter_student_id(self, student_id):

        student_id_field = self.wait.until(
            EC.visibility_of_element_located(
                self.student_id_input
            )
        )

        student_id_field.clear()

        student_id_field.send_keys(
            student_id
        )

    # =====================================================
    # SELECT SCHEDULE DAY
    # =====================================================

    def select_schedule_day(self, day):

        day_dropdown = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "schedule_day")
            )
        )

        self.wait.until(
            lambda driver: len(
                Select(day_dropdown).options
            ) > 1
        )

        select = Select(day_dropdown)

        day_value = str(day).strip()

        # Find by visible text
        for option in select.options:

            option_text = option.text.strip()
            option_value = option.get_attribute("value")

            if option_text == day_value:
                print(f"SCHEDULE DAY OPTION FOUND: {option_text}")
                print(f"SCHEDULE DAY VALUE: {option_value}")

                select.select_by_value(option_value)

                print(f"SCHEDULE DAY SELECTED: {option_text}")

                return

        raise Exception(
            f"Schedule day '{day}' not found. "
            f"Available days: "
            f"{[(o.text.strip(), o.get_attribute('value')) for o in select.options]}"
        )

    # =====================================================
    # SELECT SCHEDULE TIME
    # =====================================================

    def select_schedule_time(self, schedule_time):

        time_dropdown = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "schedule_time")
            )
        )

        self.wait.until(
            lambda driver: len(
                Select(time_dropdown).options
            ) > 1
        )

        select = Select(time_dropdown)

        target_time = str(schedule_time).strip()

        # Find by visible text
        for option in select.options:

            option_text = option.text.strip()
            option_value = option.get_attribute("value")

            if (
                    option_text == target_time
                    or
                    option_value == target_time
            ):
                print(f"SCHEDULE TIME OPTION FOUND: {option_text}")
                print(f"SCHEDULE TIME VALUE: {option_value}")

                select.select_by_value(option_value)

                print(f"SCHEDULE TIME SELECTED: {option_text}")

                return

        raise Exception(
            f"Schedule time '{schedule_time}' not found. "
            f"Available times: "
            f"{[(o.text.strip(), o.get_attribute('value')) for o in select.options]}"
        )

    # =====================================================
    # ASSIGN SCHEDULE
    # =====================================================

    def assign_schedule(
            self,
            branch,
            student_id,
            schedule_day,
            schedule_time
    ):

        # =================================================
        # BRANCH
        # =================================================

        self.select_branch(branch)

        # =================================================
        # STUDENT ID
        # =================================================

        student_id_field = self.wait.until(
            EC.visibility_of_element_located(
                self.student_id_input
            )
        )

        student_id_field.clear()
        student_id_field.send_keys(student_id)

        print(
            f"STUDENT ID ENTERED: {student_id}"
        )

        # =================================================
        # SCHEDULE DAY
        # =================================================

        self.select_schedule_day(
            schedule_day
        )

        # =================================================
        # SCHEDULE TIME
        # =================================================

        self.select_schedule_time(
            schedule_time
        )

        print(
            "ACADEMIC DETAILS ENTERED"
        )

        # =================================================
        # ASSIGN SCHEDULE
        # =================================================

        assign_button = self.wait.until(
            EC.element_to_be_clickable(
                self.assign_schedule_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            assign_button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            assign_button
        )

        print(
            "SCHEDULE ASSIGNED"
        )

    # =====================================================
    # STEP 4 -> SUMMARY
    # =====================================================

    def click_next_academic(self):

        next_button = self.wait.until(
            EC.element_to_be_clickable(
                self.next_academic_button
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
    # SAVE SUMMARY
    # =====================================================

    def click_save_summary(self):

        save_button = self.wait.until(
            EC.element_to_be_clickable(
                self.save_summary_button
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
            "STUDENT REGISTRATION SAVED SUCCESSFULLY"
        )