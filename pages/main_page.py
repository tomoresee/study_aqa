from playwright.sync_api import Page


class MainPage:
    def __init__(self, page: Page) -> None:
        self.login_button = page.get_by_test_id("nav-login")

    def open_login_card(self):
        self.login_button.click()
