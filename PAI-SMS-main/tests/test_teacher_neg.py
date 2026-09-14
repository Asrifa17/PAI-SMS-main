from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from pages.login_page import LoginPage
from pages.teacher_page import TeacherPage


# ============================================================
# COMMON FUNCTIONS
# ============================================================

def login_and_open_teacher():

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(
        "https://aradanaqa.pineappleai.cloud/login"
    )

    wait = WebDriverWait(driver, 20)

    # --------------------------------------------------------
    # LOGIN
    # --------------------------------------------------------

    login = LoginPage(driver)

    login.login(
        "admin",
        "admin123"
    )

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

    # --------------------------------------------------------
    # USERS PAGE
    # --------------------------------------------------------

    teacher = TeacherPage(driver)

    teacher.open_users_page()

    print("USERS PAGE OPENED")

    time.sleep(1)

    # --------------------------------------------------------
    # ADD USER
    # --------------------------------------------------------

    teacher.click_add_user()

    print("ADD USER POPUP OPENED")

    time.sleep(1)

    return driver, wait, teacher


def get_required_errors(driver):

    """
    Find validation messages displayed by the application.

    The application uses:
        <span class="error">Required</span>
    """

    errors = driver.find_elements(
        By.XPATH,
        "//span[contains(@class,'error') and normalize-space()='Required']"
    )

    visible_errors = [
        error for error in errors
        if error.is_displayed()
    ]

    return visible_errors


def click_personal_next(driver, wait, teacher):

    """
    Click the actual Step 1 Next button.

    IMPORTANT:
    We use TeacherPage.next_personal_button because this is
    the locator from the working teacher_page.py.
    """

    next_button = wait.until(
        EC.presence_of_element_located(
            teacher.next_personal_button
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        next_button
    )

    time.sleep(0.5)

    # Use JavaScript click because the popup can intercept
    # normal Selenium click.
    driver.execute_script(
        "arguments[0].click();",
        next_button
    )

    print("PERSONAL NEXT BUTTON CLICKED")

    time.sleep(2)


def assert_personal_validation(driver):

    """
    Verify that the form did not move to Contact Information
    and that Required validation is displayed.
    """

    errors = get_required_errors(driver)

    assert len(errors) > 0, (
        "Expected Required validation message, "
        "but no visible Required message was found."
    )

    print(
        f"REQUIRED VALIDATION FOUND: {len(errors)}"
    )

    # Contact page should NOT be opened
    phone_fields = driver.find_elements(
        *TeacherPage.phone_input
    )

    visible_phone_fields = [
        field
        for field in phone_fields
        if field.is_displayed()
    ]

    assert len(visible_phone_fields) == 0, (
        "Form moved to Contact Information even though "
        "required Personal Information was missing."
    )

    print(
        "FORM REMAINED ON PERSONAL INFORMATION"
    )


# ============================================================
# TEST 1
# FIRST NAME REQUIRED
# ============================================================

def test_teacher_first_name_required():

    driver, wait, teacher = login_and_open_teacher()

    try:

        # ----------------------------------------------------
        # Fill everything EXCEPT First Name
        # ----------------------------------------------------

        teacher.select_role("Teacher")

        teacher.select_salutation("Ms")

        # First Name intentionally EMPTY
        teacher.enter_name(
            "",
            "Perera"
        )

        teacher.select_dob(
            "2010",
            "January",
            "19"
        )

        teacher.select_gender(
            "Female"
        )

        print(
            "FIRST NAME LEFT EMPTY"
        )

        # ----------------------------------------------------
        # Click Next
        # ----------------------------------------------------

        click_personal_next(
            driver,
            wait,
            teacher
        )

        # ----------------------------------------------------
        # Verify
        # ----------------------------------------------------

        assert_personal_validation(
            driver
        )

        print(
            "TEST PASSED - FIRST NAME REQUIRED"
        )

    finally:

        driver.quit()


# ============================================================
# TEST 2
# LAST NAME REQUIRED
# ============================================================

def test_teacher_last_name_required():

    driver, wait, teacher = login_and_open_teacher()

    try:

        # ----------------------------------------------------
        # Fill everything EXCEPT Last Name
        # ----------------------------------------------------

        teacher.select_role("Teacher")

        teacher.select_salutation("Ms")

        teacher.enter_name(
            "Kamala",
            ""
        )

        teacher.select_dob(
            "2010",
            "January",
            "19"
        )

        teacher.select_gender(
            "Female"
        )

        print(
            "LAST NAME LEFT EMPTY"
        )

        # ----------------------------------------------------
        # Click Next
        # ----------------------------------------------------

        click_personal_next(
            driver,
            wait,
            teacher
        )

        # ----------------------------------------------------
        # Verify
        # ----------------------------------------------------

        assert_personal_validation(
            driver
        )

        print(
            "TEST PASSED - LAST NAME REQUIRED"
        )

    finally:

        driver.quit()





# ============================================================
# TEST 3
# ROLE REQUIRED
# ============================================================

def test_teacher_role_required():

    driver, wait, teacher = login_and_open_teacher()

    try:

        # ----------------------------------------------------
        # Role intentionally NOT selected
        # ----------------------------------------------------

        teacher.select_salutation("Ms")

        teacher.enter_name(
            "Kamala",
            "Perera"
        )

        teacher.select_dob(
            "2010",
            "January",
            "19"
        )

        teacher.select_gender(
            "Female"
        )

        print(
            "ROLE LEFT EMPTY"
        )

        # ----------------------------------------------------
        # Click Next
        # ----------------------------------------------------

        click_personal_next(
            driver,
            wait,
            teacher
        )

        # ----------------------------------------------------
        # Verify
        # ----------------------------------------------------

        assert_personal_validation(
            driver
        )

        print(
            "TEST PASSED - ROLE REQUIRED"
        )

    finally:

        driver.quit()



