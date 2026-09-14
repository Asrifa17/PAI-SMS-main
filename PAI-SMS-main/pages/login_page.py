# login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.XPATH, '//*[@id="root"]/div/div/div/form/button')

    # Actions
    def enter_username(self, username):
        self.wait.until(
            EC.presence_of_element_located(self.username_input)
        ).send_keys(username)

    def enter_password(self, password):
        self.wait.until(
            EC.presence_of_element_located(self.password_input)
        ).send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()