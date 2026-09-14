from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from pages.login_page import LoginPage
from pages.branch_page import BranchPage


def test_branch_module():

    # =====================================================
    # LAUNCH BROWSER
    # =====================================================

    driver = webdriver.Chrome()
    driver.maximize_window()

    # =====================================================
    # OPEN WEBSITE
    # =====================================================

    driver.get(
        "https://aradanaqa.pineappleai.cloud/login"
    )

    # =====================================================
    # LOGIN
    # =====================================================

    login = LoginPage(driver)

    login.login(
        "admin",
        "admin123"
    )

    wait = WebDriverWait(driver, 10)

    # Verify Dashboard
    dashboard = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//h1[contains(text(),'Dashboard')]"
            )
        )
    )

    assert dashboard.is_displayed()

    print("LOGIN SUCCESSFUL")

    # =====================================================
    # BRANCH PAGE
    # =====================================================

    branch = BranchPage(driver)

    branch.open_branch_page()

    time.sleep(3)

    # =====================================================
    # SEARCH
    # =====================================================

    branch.search_branch("New Delhi")

    print("BRANCH SEARCH SUCCESSFUL")

    time.sleep(2)

    # =====================================================
    # CLEAR SEARCH
    # =====================================================

    branch.clear_search()

    print("SEARCH CLEARED")

    time.sleep(2)

    # =====================================================
    # ADD BRANCH
    # =====================================================

    branch.click_add_branch()

    time.sleep(2)

    branch.add_new_branch(
        "India",
        "Bangalore"
    )

    time.sleep(2)

    # =====================================================
    # SUBMIT ALL BRANCHES
    # =====================================================

    branch.submit_all_branches()

    time.sleep(5)

    # =====================================================
    # EDIT
    # =====================================================

    branch.click_edit()

    time.sleep(2)

    # =====================================================
    # UPDATE
    # =====================================================

    branch.update_branch()

    time.sleep(3)

    # =====================================================
    # DELETE
    # =====================================================

    branch.delete_branch()

    time.sleep(3)

    print("BRANCH MODULE COMPLETED")