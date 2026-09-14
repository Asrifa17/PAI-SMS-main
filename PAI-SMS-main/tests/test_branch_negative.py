from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.branch_negative_page import BranchNegativePage

import time


# =========================================================
# LOGIN HELPER
# =========================================================

def login_to_system(driver):

    driver.get(
        "https://aradanaqa.pineappleai.cloud/login"
    )

    login = LoginPage(driver)

    login.login(
        "admin",
        "admin123"
    )

    wait = WebDriverWait(driver, 15)

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


# =========================================================
# TC 01
# COUNTRY EMPTY + BRANCH NAME EMPTY
# =========================================================

def test_branch_empty_country_empty_name():

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:

        login_to_system(driver)

        branch = BranchNegativePage(driver)

        branch.open_branch_page()

        print("BRANCH PAGE OPENED")

        branch.open_add_branch()

        print("ADD BRANCH FORM OPENED")

        # Leave both fields empty
        branch.click_add_branch()

        print("ADD BRANCH CLICKED")

        time.sleep(2)



    finally:

        driver.quit()


# =========================================================
# TC 02
# COUNTRY SELECTED + BRANCH NAME EMPTY
# =========================================================

def test_branch_country_selected_name_empty():

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:

        login_to_system(driver)

        branch = BranchNegativePage(driver)

        branch.open_branch_page()

        branch.open_add_branch()

        branch.select_country("India")

        print("COUNTRY SELECTED")

        # Branch name intentionally empty
        branch.click_add_branch()

        print("ADD BRANCH CLICKED")

        time.sleep(2)



    finally:

        driver.quit()


# =========================================================
# TC 03
# COUNTRY EMPTY + BRANCH NAME ENTERED
# =========================================================

def test_branch_country_empty_name_entered():

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:

        login_to_system(driver)

        branch = BranchNegativePage(driver)

        branch.open_branch_page()

        branch.open_add_branch()

        branch.enter_branch_name(
            "Negative Test Branch"
        )

        print("BRANCH NAME ENTERED")

        # Country intentionally empty
        branch.click_add_branch()

        print("ADD BRANCH CLICKED")

        time.sleep(2)



    finally:

        driver.quit()


# =========================================================
# TC 04
# BRANCH NAME ONLY SPACES
# =========================================================

def test_branch_name_spaces_only():

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:

        login_to_system(driver)

        branch = BranchNegativePage(driver)

        branch.open_branch_page()

        branch.open_add_branch()

        branch.select_country("India")

        branch.enter_branch_name(
            "     "
        )

        print("SPACES ENTERED")

        branch.click_add_branch()

        print("ADD BRANCH CLICKED")

        time.sleep(2)



    finally:

        driver.quit()


# =========================================================
# TC 05
# SPECIAL CHARACTERS
# =========================================================

def test_branch_special_characters():

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:

        login_to_system(driver)

        branch = BranchNegativePage(driver)

        branch.open_branch_page()

        branch.open_add_branch()

        branch.select_country("India")

        branch.enter_branch_name(
            "@@@###$$$"
        )

        print("SPECIAL CHARACTERS ENTERED")

        branch.click_add_branch()

        print("ADD BRANCH CLICKED")

        time.sleep(2)



    finally:

        driver.quit()


# =========================================================
# TC 06
# NUMERIC BRANCH NAME
# =========================================================

def test_branch_numeric_name():

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:

        login_to_system(driver)

        branch = BranchNegativePage(driver)

        branch.open_branch_page()

        branch.open_add_branch()

        branch.select_country("India")

        branch.enter_branch_name(
            "123456789"
        )

        print("NUMERIC VALUE ENTERED")

        branch.click_add_branch()

        print("ADD BRANCH CLICKED")

        time.sleep(2)



    finally:

        driver.quit()


# =========================================================
# TC 07
# VERY LONG BRANCH NAME
# =========================================================

def test_branch_very_long_name():

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:

        login_to_system(driver)

        branch = BranchNegativePage(driver)

        branch.open_branch_page()

        branch.open_add_branch()

        branch.select_country("India")

        long_name = "A" * 300

        branch.enter_branch_name(
            long_name
        )

        print("VERY LONG BRANCH NAME ENTERED")

        branch.click_add_branch()

        print("ADD BRANCH CLICKED")

        time.sleep(2)



    finally:

        driver.quit()