from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from pages.login_page import LoginPage
from pages.course_page import CoursePage


def test_course_required_field_validation():

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

    try:

        wait = WebDriverWait(driver, 20)

        # =================================================
        # LOGIN
        # =================================================

        login = LoginPage(driver)

        login.login(
            "admin",
            "admin123"
        )

        # =================================================
        # VERIFY DASHBOARD
        # =================================================

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

        # =================================================
        # OPEN COURSE PAGE
        # =================================================

        course = CoursePage(driver)

        course.open_course_page()

        print("COURSE PAGE OPENED")

        time.sleep(2)

        # =================================================
        # OPEN ADD COURSE
        # =================================================

        course.click_add_course()

        print("ADD COURSE POPUP OPENED")

        time.sleep(2)

        # =================================================
        # LOCATE FIELDS
        # =================================================

        course_id = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "courseId")
            )
        )

        course_name = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "courseName")
            )
        )

        grade = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "grade")
            )
        )

        fees = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "fees")
            )
        )

        # =================================================
        # CLEAR REQUIRED FIELDS
        # =================================================

        course_id.clear()
        course_name.clear()
        grade.clear()
        fees.clear()

        print("REQUIRED FIELDS LEFT EMPTY")

        # =================================================
        # CLICK ADD BUTTON
        # =================================================

        add_button = wait.until(
            EC.element_to_be_clickable(
                course.add_button
            )
        )

        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            add_button
        )

        driver.execute_script(
            "arguments[0].click();",
            add_button
        )

        print("ADD BUTTON CLICKED")

        time.sleep(2)

        # =================================================
        # CHECK FORM IS STILL OPEN
        # =================================================

        course_id_after = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "courseId")
            )
        )

        assert course_id_after.is_displayed()

        print(
            "ADD COURSE FORM REMAINS OPEN"
        )

        # =================================================
        # VERIFY COURSE ID IS STILL EMPTY
        # =================================================

        assert (
            course_id_after.get_attribute("value") == ""
        )

        print(
            "COURSE ID REMAINS EMPTY"
        )

        # =================================================
        # VERIFY COURSE NAME IS STILL EMPTY
        # =================================================

        assert (
            course_name.get_attribute("value") == ""
        )

        print(
            "COURSE NAME REMAINS EMPTY"
        )

        # =================================================
        # VERIFY GRADE IS STILL EMPTY
        # =================================================

        assert (
            grade.get_attribute("value") == ""
        )

        print(
            "GRADE REMAINS EMPTY"
        )

        # =================================================
        # VERIFY FEES IS STILL EMPTY
        # =================================================

        assert (
            fees.get_attribute("value") == ""
        )

        print(
            "FEES REMAINS EMPTY"
        )

        # =================================================
        # CHECK HTML5 VALIDATION
        # =================================================

        invalid_fields = []

        for field, name in [
            (course_id, "Course ID"),
            (course_name, "Course Name"),
            (grade, "Grade"),
            (fees, "Fees")
        ]:

            is_valid = driver.execute_script(
                "return arguments[0].checkValidity();",
                field
            )

            if not is_valid:
                invalid_fields.append(name)

        # =================================================
        # RESULT
        # =================================================

        if invalid_fields:

            print(
                "HTML5 VALIDATION DETECTED FOR:",
                ", ".join(invalid_fields)
            )

        else:

            print(
                "No HTML5 validation detected; "
                "form remained open after empty submission."
            )

        print(
            "NEGATIVE COURSE TEST PASSED - "
            "EMPTY COURSE WAS NOT SUBMITTED"
        )

    finally:

        time.sleep(3)

        driver.quit()