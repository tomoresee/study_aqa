from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.login_card = page.get_by_test_id("login-card")
        self.login_input = page.get_by_test_id("login-username")
        self.password_input = page.get_by_test_id("login-password")
        self.login_submit_button = page.get_by_test_id("login-submit")
        self.error_login_message = page.get_by_test_id("login-error-inline")
        self.button_spinner = page.get_by_test_id("login-submit-spinner")

    def login(self, username, password):
        self.login_input.fill(username)
        self.password_input.fill(password)
        self.login_submit_button.click()

    def is_spinner_visible(self) -> bool:
        return self.button_spinner.is_visible()

    def is_spinner_hidden(self) -> bool:
        try:
            self.button_spinner.wait_for(state="hidden")
            return True
        except TimeoutError:
            return False

    def is_error_message_visible(self) -> bool:
        return self.error_login_message.is_visible()

    def get_error_message_text(self) -> str:
        return self.error_login_message.text_content()
