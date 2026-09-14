# attendance_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AttendancePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    attendance_menu = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[1]/div/div[2]/a[2]'
    )

    search_box = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div[1]/div/input'
    )

    scan_qr_button = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div[1]/button'
    )

    # Actions
    def open_attendance_page(self):
        attendance = self.wait.until(
            EC.element_to_be_clickable(self.attendance_menu)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            attendance
        )

    def search_attendance(self, keyword):
        search = self.wait.until(
            EC.presence_of_element_located(self.search_box)
        )

        search.send_keys(keyword)

    def click_scan_qr(self):
        qr = self.wait.until(
            EC.element_to_be_clickable(self.scan_qr_button)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            qr
        )