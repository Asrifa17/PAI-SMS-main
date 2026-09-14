from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    # Dashboard menu
    dashboard_menu = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[1]/div/div[2]/a[1]'
    )

    # Branch / All dropdown
    branch_dropdown = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/main/div/div/div[1]/div[1]/div/select'
    )

    # Notification button
    notification_button = (
        By.XPATH,
        '//*[@id="root"]/div/div[2]/div[2]/header/div/div[2]'
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Open Dashboard
    def open_dashboard(self):

        self.wait.until(
            EC.element_to_be_clickable(self.dashboard_menu)
        ).click()

    # Verify branch dropdown options
    def verify_branch_dropdown_options(self):

        dropdown = self.wait.until(
            EC.presence_of_element_located(self.branch_dropdown)
        )

        select = Select(dropdown)

        # Get all available options
        options = [
            option.text.strip()
            for option in select.options
        ]

        print("\nAvailable Branches:")

        for option in options:
            print(option)

        # Expected options
        expected_options = [
            "All",
            "Afghanistan - Jaffna",
            "Afghanistan - colombo",
            "Australia - colombo",
            "Brazil - Rio",
            "Brazil - kandy",
            "Brazil - kkk",
            "Brazil - lavo",
            "Canada - lisha",
            "Colombia - Jaffna",
            "India - New Delhi",
            "Sri Lanka - Galle",
            "Sri Lanka - colombo",
            "Sri Lanka - jaffna"

        ]

        # Verify every expected option
        for option in expected_options:

            assert option in options, (
                f"Branch option not found: {option}"
            )

        print("ALL BRANCH DROPDOWN OPTIONS VERIFIED")

    # Select a branch
    def select_branch(self, branch_name):

        dropdown = self.wait.until(
            EC.presence_of_element_located(self.branch_dropdown)
        )

        Select(dropdown).select_by_visible_text(branch_name)

        print(f"BRANCH SELECTED: {branch_name}")

    # Click notification button
    def click_notification(self):

        self.wait.until(
            EC.element_to_be_clickable(self.notification_button)
        ).click()

        print("NOTIFICATION BUTTON CLICKED")