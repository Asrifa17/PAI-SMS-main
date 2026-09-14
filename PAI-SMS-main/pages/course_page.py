# course_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


class CoursePage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ================= LOCATORS =================

    course_menu = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[1]/div/div[2]/a[5]'
    )

    search_box = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[1]/div/input'
    )

    add_course_button = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[1]/button'
    )

    course_id = (
        By.ID,
        'courseId'
    )

    course_name = (
        By.ID,
        'courseName'
    )

    branch_select = (
        By.ID,
        'branchId'
    )

    grade_input = (
        By.ID,
        'grade'
    )

    status_select = (
        By.ID,
        'status'
    )

    fees_input = (
        By.ID,
        'fees'
    )

    add_button = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[2]/div/div/form/button'
    )

    delete_icon = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[2]/table/tbody/tr[1]/td[4]/div/img[3]'
    )

    delete_button = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[2]/div/div/div/button[2]'
    )

    edit_icon = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[2]/table/tbody/tr[1]/td[4]/div/img[2]'
    )

    update_button = (
        By.XPATH,
        "//button[contains(text(),'Update')]"
    )

    # ================= METHODS =================

    def open_course_page(self):

        course = self.wait.until(
            EC.element_to_be_clickable(self.course_menu)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            course
        )

    def search_course(self, keyword):

        search = self.wait.until(
            EC.presence_of_element_located(self.search_box)
        )

        search.clear()

        search.send_keys(keyword)

    def click_add_course(self):

        add = self.wait.until(
            EC.element_to_be_clickable(self.add_course_button)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add
        )

    def add_course(
            self,
            course_id,
            course_name,
            branch,
            grade,
            status,
            fees
    ):

        # Course ID
        cid = self.wait.until(
            EC.presence_of_element_located(self.course_id)
        )

        cid.clear()

        cid.send_keys(course_id)

        # Course Name
        cname = self.wait.until(
            EC.presence_of_element_located(self.course_name)
        )

        cname.clear()

        cname.send_keys(course_name)

        # Branch
        branch_dropdown = Select(
            self.wait.until(
                EC.presence_of_element_located(self.branch_select)
            )
        )

        branch_dropdown.select_by_visible_text(branch)

        # Grade
        grade_input = self.wait.until(
            EC.presence_of_element_located(self.grade_input)
        )

        grade_input.clear()

        grade_input.send_keys(grade)

        # Status
        status_dropdown = Select(
            self.wait.until(
                EC.presence_of_element_located(self.status_select)
            )
        )

        status_dropdown.select_by_visible_text(status)

        # Fees
        fee = self.wait.until(
            EC.presence_of_element_located(self.fees_input)
        )

        fee.clear()

        fee.send_keys(fees)

        # Add Button
        add_btn = self.wait.until(
            EC.element_to_be_clickable(self.add_button)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add_btn
        )

    def click_edit(self):

        time.sleep(3)

        edit = self.wait.until(
            EC.element_to_be_clickable(self.edit_icon)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            edit
        )

    def click_update(self):

        update = self.wait.until(
            EC.element_to_be_clickable(self.update_button)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            update
        )

    def delete_course(self):

        time.sleep(3)

        delete = self.wait.until(
            EC.element_to_be_clickable(self.delete_icon)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            delete
        )

        confirm_delete = self.wait.until(
            EC.element_to_be_clickable(self.delete_button)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            confirm_delete
        )