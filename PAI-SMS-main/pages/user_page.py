from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time


class UserPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # =====================================================
    # LOCATORS
    # =====================================================

    user_menu = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[1]/div/div[2]/a[4]/span'
    )

    search_box = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div[1]/div/input'
    )

    roles_filter = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div[2]/select[1]'
    )

    course_filter = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div[2]/select[3]'
    )

    # =====================================================
    # STUDENT PROFILE
    # =====================================================

    profile_button = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div/main/div/div[3]/div/div/div[1]/img[1]'
    )

    # =====================================================
    # STUDENT DETAILS POPUP
    # =====================================================

    id_card_button = (
        By.XPATH,
        '/html/body/div[4]/div/div/button[2]'
    )

    edit_student_button = (
        By.XPATH,
        '/html/body/div[4]/div/div/div[2]/div/button'
    )

    # =====================================================
    # DELETE
    # =====================================================

    delete_icon = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div/main/div/div[3]/div/div/div[7]/img[2]'
    )

    delete_confirm_button = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div/main/div/div[3]/div[2]/div/div/button[2]'
    )

    # =====================================================
    # OPEN USER PAGE
    # =====================================================

    def open_user_page(self):

        user = self.wait.until(
            EC.element_to_be_clickable(
                self.user_menu
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            user
        )

        time.sleep(2)

    # =====================================================
    # SEARCH USER
    # =====================================================

    def search_user(self, keyword):

        search = self.wait.until(
            EC.visibility_of_element_located(
                self.search_box
            )
        )

        search.clear()
        search.send_keys(keyword)

        time.sleep(2)

    # =====================================================
    # SELECT ROLE
    # =====================================================

    def select_role(self, role):

        role_dropdown = Select(
            self.wait.until(
                EC.visibility_of_element_located(
                    self.roles_filter
                )
            )
        )

        role_dropdown.select_by_visible_text(role)

        time.sleep(2)

    # =====================================================
    # SELECT COURSE
    # =====================================================

    def select_course(self, course):

        course_dropdown = Select(
            self.wait.until(
                EC.visibility_of_element_located(
                    self.course_filter
                )
            )
        )

        course_dropdown.select_by_visible_text(course)

        time.sleep(2)

    # =====================================================
    # OPEN STUDENT PROFILE
    # =====================================================

    def click_profile(self):

        profile = self.wait.until(
            EC.presence_of_element_located(
                self.profile_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            profile
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            profile
        )

        time.sleep(2)

        print("STUDENT DETAILS POPUP OPENED")

    # =====================================================
    # OPEN ID CARD
    # =====================================================

    def click_id_card(self):

        id_card = self.wait.until(
            EC.element_to_be_clickable(
                self.id_card_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            id_card
        )

        time.sleep(2)

        print("ID CARD OPENED")

    # =====================================================
    # EDIT STUDENT
    # =====================================================

    def click_edit_student(self):

        edit = self.wait.until(
            EC.presence_of_element_located(
                self.edit_student_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            edit
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            edit
        )

        time.sleep(2)

        print("EDIT STUDENT BUTTON CLICKED")

    # =====================================================
    # DELETE USER
    # =====================================================

    def click_delete(self):

        delete = self.wait.until(
            EC.presence_of_element_located(
                self.delete_icon
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            delete
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            delete
        )

        time.sleep(2)

        print("DELETE POPUP OPENED")

    # =====================================================
    # CONFIRM DELETE
    # =====================================================

    def confirm_delete(self):

        delete_button = self.wait.until(
            EC.element_to_be_clickable(
                self.delete_confirm_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            delete_button
        )

        time.sleep(3)

        print("USER DELETED")