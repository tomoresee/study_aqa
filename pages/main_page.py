from playwright.sync_api import Page


class MainPage:
    def __init__(self, page: Page) -> None:
        self.login_button = page.get_by_test_id("nav-login")
        self.search_input = page.get_by_test_id("search-input")
        self.search_button = page.get_by_test_id("search-button")

    def open_login_card(self):
        self.login_button.click()

    def find(self, name):
        self.search_input.fill(name)
        self.search_button.click()
