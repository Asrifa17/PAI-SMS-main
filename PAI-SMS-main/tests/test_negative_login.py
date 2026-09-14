import time

from selenium import webdriver

from pages.login_page import LoginPage


BASE_URL = "https://aradanaqa.pineappleai.cloud/login"


def test_invalid_username():

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(BASE_URL)

    login = LoginPage(driver)

    login.login("invaliduser", "admin123")

    time.sleep(2)

    assert "/login" in driver.current_url

    print("INVALID USERNAME TEST PASSED")

    driver.quit()


def test_invalid_password():

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(BASE_URL)

    login = LoginPage(driver)

    login.login("admin", "wrongpassword")

    time.sleep(2)

    assert "/login" in driver.current_url

    print("INVALID PASSWORD TEST PASSED")

    driver.quit()


def test_empty_username():

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(BASE_URL)

    login = LoginPage(driver)

    login.login("", "admin123")

    time.sleep(2)

    assert "/login" in driver.current_url

    print("EMPTY USERNAME TEST PASSED")

    driver.quit()


def test_empty_password():

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(BASE_URL)

    login = LoginPage(driver)

    login.login("admin", "")

    time.sleep(2)

    assert "/login" in driver.current_url

    print("EMPTY PASSWORD TEST PASSED")

    driver.quit()


def test_empty_username_and_password():

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(BASE_URL)

    login = LoginPage(driver)

    login.login("", "")

    time.sleep(2)

    assert "/login" in driver.current_url

    print("EMPTY USERNAME AND PASSWORD TEST PASSED")

    driver.quit()