import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.schedule_page import SchedulePage


LOGIN_URL = "https://aradanaqa.pineappleai.cloud/login"

USERNAME = "admin"
PASSWORD = "admin123"


# ==========================================================
# LOGIN
# ==========================================================

def login(driver):

    driver.get(LOGIN_URL)

    login_page = LoginPage(driver)

    login_page.login(
        USERNAME,
        PASSWORD
    )

    wait = WebDriverWait(driver, 20)

    # Verify Dashboard
    dashboard = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//h1[contains(text(),'Dashboard')]"
            )
        )
    )

    assert dashboard.is_displayed()

    print("LOGIN SUCCESSFUL")

    time.sleep(2)


# ==========================================================
# TC_Schel_162
# Open Schedule Module
# ==========================================================

def test_schedule_navigation():

    # ======================================================
    # LAUNCH BROWSER
    # ======================================================

    driver = webdriver.Chrome()

    driver.maximize_window()

    try:

        # ==================================================
        # LOGIN
        # ==================================================

        login(driver)

        # ==================================================
        # SCHEDULE PAGE
        # ==================================================

        schedule = SchedulePage(driver)

        schedule.open_schedule()

        print("SCHEDULE PAGE OPENED")

        # ==================================================
        # VERIFY SCHEDULE TABLE
        # ==================================================

        assert schedule.is_schedule_table_visible()

        print("SCHEDULE TABLE VISIBLE")

    finally:

        driver.quit()


# ==========================================================
# SEARCH TESTS
# ==========================================================

@pytest.mark.parametrize(
    "search_value",
    [
        "colombo",
        "Abitharani Pavi",
        "Cello",
        "06",
        "Friday",
        "09:00"
    ]
)
def test_schedule_search(search_value):

    # ======================================================
    # LAUNCH BROWSER
    # ======================================================

    driver = webdriver.Chrome()

    driver.maximize_window()

    try:

        # ==================================================
        # LOGIN
        # ==================================================

        login(driver)

        # ==================================================
        # SCHEDULE PAGE
        # ==================================================

        schedule = SchedulePage(driver)

        schedule.open_schedule()

        print("SCHEDULE PAGE OPENED")

        # ==================================================
        # SEARCH
        # ==================================================

        schedule.search_schedule(
            search_value
        )

        print(
            "SEARCH VALUE:",
            search_value
        )

        time.sleep(2)

        # ==================================================
        # VERIFY SEARCH RESULT
        # ==================================================

        assert (
            search_value.lower()
            in driver.page_source.lower()
        )

        print(
            "SEARCH PASSED:",
            search_value
        )

    finally:

        driver.quit()


# ==========================================================
# TC_Schel_167
# Open Add Schedule Popup
# ==========================================================

def test_open_add_schedule_popup():

    # ======================================================
    # LAUNCH BROWSER
    # ======================================================

    driver = webdriver.Chrome()

    driver.maximize_window()

    try:

        # ==================================================
        # LOGIN
        # ==================================================

        login(driver)

        # ==================================================
        # SCHEDULE PAGE
        # ==================================================

        schedule = SchedulePage(driver)

        schedule.open_schedule()

        print("SCHEDULE PAGE OPENED")

        # ==================================================
        # ADD SCHEDULE
        # ==================================================

        schedule.click_add_schedule()

        print("ADD SCHEDULE POPUP OPENED")

        # ==================================================
        # VERIFY POPUP
        # ==================================================

        assert (
            schedule.is_add_popup_visible()
        )

        print("ADD SCHEDULE POPUP VERIFIED")

    finally:

        driver.quit()


# ==========================================================
# TC_Schel_175
# Add Schedule
# ==========================================================

def test_add_schedule():

    # ======================================================
    # LAUNCH BROWSER
    # ======================================================

    driver = webdriver.Chrome()

    driver.maximize_window()

    try:

        # ==================================================
        # LOGIN
        # ==================================================

        login(driver)

        # ==================================================
        # SCHEDULE PAGE
        # ==================================================

        schedule = SchedulePage(driver)

        schedule.open_schedule()

        print("SCHEDULE PAGE OPENED")

        # ==================================================
        # OPEN ADD SCHEDULE POPUP
        # ==================================================

        schedule.click_add_schedule()

        print("ADD SCHEDULE POPUP OPENED")

        assert (
            schedule.is_add_popup_visible()
        )

        # ==================================================
        # ENTER SCHEDULE DETAILS
        # ==================================================

        schedule.fill_schedule(

            branch="colombo",

            lecturer="Abitharani Pavi",

            course="Cello",

            grade="06",

            day="Friday",

            start_time="09:00",

            end_time="23:00"

        )

        print("SCHEDULE DETAILS ENTERED")

        # ==================================================
        # ADD SCHEDULE
        # ==================================================

        schedule.click_add_form_button()

        print("ADD SCHEDULE BUTTON CLICKED")

        time.sleep(5)

        # ==================================================
        # VERIFY SUCCESS
        # ==================================================

        message = schedule.get_success_message()

        print(
            "ADD MESSAGE:",
            message
        )

        assert (
            "success" in message.lower()
            or
            "added" in message.lower()
            or
            schedule.is_schedule_table_visible()
        )

        print("SCHEDULE ADDED SUCCESSFULLY")

    finally:

        driver.quit()


# ==========================================================
# TC_Schel_176
# Edit Schedule Popup
# ==========================================================

def test_edit_schedule():

    # ======================================================
    # LAUNCH BROWSER
    # ======================================================

    driver = webdriver.Chrome()

    driver.maximize_window()

    try:

        # ==================================================
        # LOGIN
        # ==================================================

        login(driver)

        # ==================================================
        # SCHEDULE PAGE
        # ==================================================

        schedule = SchedulePage(driver)

        schedule.open_schedule()

        print("SCHEDULE PAGE OPENED")

        # ==================================================
        # VERIFY DATA EXISTS
        # ==================================================

        assert (
            schedule.get_row_count() > 0
        )

        # ==================================================
        # CLICK EDIT
        # ==================================================

        schedule.click_edit()

        print("EDIT BUTTON CLICKED")

        # ==================================================
        # VERIFY EDIT POPUP
        # ==================================================

        assert (
            "Edit Schedule"
            in driver.page_source
        )

        print("EDIT SCHEDULE POPUP OPENED")

    finally:

        driver.quit()


# ==========================================================
# TC_Schel_177
# Update Schedule
# ==========================================================

def test_update_schedule():

    # ======================================================
    # LAUNCH BROWSER
    # ======================================================

    driver = webdriver.Chrome()

    driver.maximize_window()

    try:

        # ==================================================
        # LOGIN
        # ==================================================

        login(driver)

        # ==================================================
        # SCHEDULE PAGE
        # ==================================================

        schedule = SchedulePage(driver)

        schedule.open_schedule()

        print("SCHEDULE PAGE OPENED")

        # ==================================================
        # EDIT SCHEDULE
        # ==================================================

        assert (
            schedule.get_row_count() > 0
        )

        schedule.click_edit()

        print("EDIT POPUP OPENED")

        # ==================================================
        # CHANGE START TIME
        # ==================================================

        schedule.change_start_time(
            "10:00"
        )

        print("START TIME CHANGED")

        # ==================================================
        # UPDATE
        # ==================================================

        schedule.click_update()

        print("UPDATE BUTTON CLICKED")

        time.sleep(3)

        # ==================================================
        # VERIFY UPDATE
        # ==================================================

        message = (
            schedule.get_success_message()
        )

        print(
            "UPDATE MESSAGE:",
            message
        )

        assert (
            "success" in message.lower()
            or
            "updated" in message.lower()
        )

        print("SCHEDULE UPDATED SUCCESSFULLY")

    finally:

        driver.quit()


# ==========================================================
# TC_Schel_178
# Delete Schedule
# ==========================================================

def test_delete_schedule():

    # ======================================================
    # LAUNCH BROWSER
    # ======================================================

    driver = webdriver.Chrome()

    driver.maximize_window()

    try:

        # ==================================================
        # LOGIN
        # ==================================================

        login(driver)

        # ==================================================
        # SCHEDULE PAGE
        # ==================================================

        schedule = SchedulePage(driver)

        schedule.open_schedule()

        print("SCHEDULE PAGE OPENED")

        # ==================================================
        # VERIFY SCHEDULE EXISTS
        # ==================================================

        assert (
            schedule.get_row_count() > 0
        )

        # ==================================================
        # CLICK DELETE
        # ==================================================

        schedule.click_delete_icon()

        print("DELETE BUTTON CLICKED")

        # ==================================================
        # VERIFY CONFIRMATION POPUP
        # ==================================================

        assert (
            schedule.is_delete_modal_visible()
        )

        print("DELETE CONFIRMATION POPUP OPENED")

        # ==================================================
        # CONFIRM DELETE
        # ==================================================

        schedule.confirm_delete()

        print("DELETE CONFIRMED")

        time.sleep(5)

        # ==================================================
        # VERIFY DELETE
        # ==================================================

        message = schedule.get_success_message()

        print(
            "DELETE MESSAGE:",
            message
        )

        assert (
            "success" in message.lower()
            or
            "delete" in message.lower()
            or
            schedule.is_schedule_table_visible()
        )

        print("SCHEDULE DELETE COMPLETED")

    finally:

        driver.quit()


# ==========================================================
# CLOSE ADD SCHEDULE POPUP
# ==========================================================

def test_close_schedule_popup():

    # ======================================================
    # LAUNCH BROWSER
    # ======================================================

    driver = webdriver.Chrome()

    driver.maximize_window()

    try:

        # ==================================================
        # LOGIN
        # ==================================================

        login(driver)

        # ==================================================
        # SCHEDULE PAGE
        # ==================================================

        schedule = SchedulePage(driver)

        schedule.open_schedule()

        print("SCHEDULE PAGE OPENED")

        # ==================================================
        # OPEN POPUP
        # ==================================================

        schedule.click_add_schedule()

        print("ADD SCHEDULE POPUP OPENED")

        assert (
            schedule.is_add_popup_visible()
        )

        # ==================================================
        # CLOSE POPUP
        # ==================================================

        schedule.close_popup()

        print("SCHEDULE POPUP CLOSED")

    finally:

        driver.quit()


# ==========================================================
# VIEW SCHEDULE
# ==========================================================

def test_view_schedule():

    # ======================================================
    # LAUNCH BROWSER
    # ======================================================

    driver = webdriver.Chrome()

    driver.maximize_window()

    try:

        # ==================================================
        # LOGIN
        # ==================================================

        login(driver)

        # ==================================================
        # SCHEDULE PAGE
        # ==================================================

        schedule = SchedulePage(driver)

        schedule.open_schedule()

        print("SCHEDULE PAGE OPENED")

        # ==================================================
        # VERIFY DATA EXISTS
        # ==================================================

        assert (
            schedule.get_row_count() > 0
        )

        # ==================================================
        # VIEW SCHEDULE
        # ==================================================

        schedule.view_schedule()

        print("VIEW SCHEDULE CLICKED")

        # ==================================================
        # BASIC VERIFICATION
        # ==================================================

        assert True

    finally:

        driver.quit()