# branch_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


class BranchPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # =====================================================
    # LOCATORS
    # =====================================================

    # Branch menu
    branch_menu = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[1]/div/div[2]/a[3]'
    )

    # Search box
    search_box = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[1]/div/input'
    )

    # Main + Add Branch button
    add_branch_button = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[1]/div[2]/button'
    )

    # =====================================================
    # ADD BRANCH FORM
    # =====================================================

    # Country dropdown
    country_dropdown = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[3]/div/form/div[1]/div[1]/select'
    )

    # Branch name
    branch_name_input = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[3]/div/form/div[1]/div[2]/input'
    )

    # Add Branch button inside form
    add_branch_submit_button = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[3]/div/form/div[3]/button'
    )

    # Submit All Branches
    submit_all_branches_button = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[3]/div/div[2]/button'
    )

    # =====================================================
    # EDIT
    # =====================================================

    edit_button = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[2]/table/tbody/tr[1]/td[4]/button[1]/img'
    )

    # Update button inside Edit form
    update_button = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[3]/div/div[2]/button'
    )

    # =====================================================
    # DELETE
    # =====================================================

    delete_button = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[2]/table/tbody/tr[1]/td[4]/button[2]/img'
    )

    # Delete confirmation button
    delete_confirm_button = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[3]/div/div/button[2]'
    )

    # =====================================================
    # OPEN BRANCH PAGE
    # =====================================================

    def open_branch_page(self):

        branch = self.wait.until(
            EC.element_to_be_clickable(
                self.branch_menu
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            branch
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.search_box
            )
        )

        print("BRANCH PAGE OPENED")

    # =====================================================
    # SEARCH BRANCH
    # =====================================================

    def search_branch(self, keyword):

        search = self.wait.until(
            EC.visibility_of_element_located(
                self.search_box
            )
        )

        search.clear()

        search.send_keys(keyword)

    # =====================================================
    # CLEAR SEARCH
    # =====================================================

    def clear_search(self):

        search = self.wait.until(
            EC.visibility_of_element_located(
                self.search_box
            )
        )

        search.click()

        search.clear()

        # Trigger React events
        self.driver.execute_script(
            """
            arguments[0].dispatchEvent(
                new Event('input', {bubbles: true})
            );

            arguments[0].dispatchEvent(
                new Event('change', {bubbles: true})
            );
            """,
            search
        )

        time.sleep(2)

        # Refresh page so complete table is loaded
        self.driver.refresh()

        # Wait until Branch page loads again
        self.wait.until(
            EC.visibility_of_element_located(
                self.search_box
            )
        )

        time.sleep(2)

    # =====================================================
    # OPEN ADD BRANCH FORM
    # =====================================================

    def click_add_branch(self):

        add_button = self.wait.until(
            EC.element_to_be_clickable(
                self.add_branch_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            add_button
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            add_button
        )

        # Wait for Country dropdown
        self.wait.until(
            EC.visibility_of_element_located(
                self.country_dropdown
            )
        )

        print("ADD BRANCH POPUP OPENED")

    # =====================================================
    # ADD NEW BRANCH
    # =====================================================

    def add_new_branch(self, country, branch_name):

        # ---------------------------------------------
        # Select Country
        # ---------------------------------------------

        dropdown_element = self.wait.until(
            EC.visibility_of_element_located(
                self.country_dropdown
            )
        )

        dropdown = Select(
            dropdown_element
        )

        dropdown.select_by_visible_text(
            country
        )

        # ---------------------------------------------
        # Enter Branch Name
        # ---------------------------------------------

        branch = self.wait.until(
            EC.visibility_of_element_located(
                self.branch_name_input
            )
        )

        branch.clear()

        branch.send_keys(
            branch_name
        )

        time.sleep(1)

        # ---------------------------------------------
        # Click Add Branch inside form
        # ---------------------------------------------

        add_button = self.wait.until(
            EC.element_to_be_clickable(
                self.add_branch_submit_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            add_button
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            add_button
        )

        time.sleep(2)

        print("BRANCH ADDED TO LIST")

    # =====================================================
    # SUBMIT ALL BRANCHES
    # =====================================================

    def submit_all_branches(self):

        submit_button = self.wait.until(
            EC.element_to_be_clickable(
                self.submit_all_branches_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            submit_button
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            submit_button
        )

        time.sleep(4)

        print("ALL BRANCHES SUBMITTED")

    # =====================================================
    # EDIT BRANCH
    # =====================================================

    def click_edit(self):

        # Wait for Edit image
        edit = self.wait.until(
            EC.presence_of_element_located(
                self.edit_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            edit
        )

        time.sleep(1)

        # Click Edit
        self.driver.execute_script(
            "arguments[0].click();",
            edit
        )

        print("EDIT BUTTON CLICKED")

        # Wait until Edit form / Update button appears
        self.wait.until(
            EC.visibility_of_element_located(
                self.update_button
            )
        )

        print("EDIT FORM OPENED")

    # =====================================================
    # UPDATE BRANCH
    # =====================================================

    def update_branch(self):

        update = self.wait.until(
            EC.element_to_be_clickable(
                self.update_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            update
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            update
        )

        print("UPDATE BUTTON CLICKED")

        time.sleep(4)

    # =====================================================
    # DELETE BRANCH
    # =====================================================

    def delete_branch(self):

        # Wait for Delete image
        delete = self.wait.until(
            EC.presence_of_element_located(
                self.delete_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            delete
        )

        time.sleep(1)

        # Click Delete
        self.driver.execute_script(
            "arguments[0].click();",
            delete
        )

        print("DELETE BUTTON CLICKED")

        time.sleep(1)

        # Wait for confirmation button
        confirm = self.wait.until(
            EC.element_to_be_clickable(
                self.delete_confirm_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            confirm
        )

        print("DELETE CONFIRMED")

        time.sleep(4)