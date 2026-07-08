"""
1. открыть сайт http://144.31.63.127:5000/
2. нажать кнопку логина
3. Ввести случайные данные в поля логина и пароля. Нажать кнопку входа
4. проверить что отобразились:
  1. Отображается индикатор загрузки
  2. После исчезновения индикатора появляется сообщение об ошибке "Invalid login or password."
"""

from playwright.sync_api import Page, expect
from faker import Faker

BASE_URL = "http://144.31.63.127:5000/"


def generate_random_credentials():
    fake = Faker()

    login = fake.user_name()
    password = fake.password(length=12)

    return login, password


class MainPage:
    def __init__(self, page: Page) -> None:
        self.login_button = page.get_by_test_id("nav-login")

    def open_login_card(self):
        self.login_button.click()


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.login_card = page.get_by_test_id("login-card")
        self.login_input = page.get_by_test_id("login-username")
        self.password_input = page.get_by_test_id("login-password")
        self.login_submit_button = page.get_by_test_id("login-submit")
        self.error_login_message = page.get_by_test_id("login-error-inline")
        self.button_spinner = page.get_by_test_id("login-submit-spinner")

    def fill_username(self, username):
        self.login_input.fill(username)

    def fill_password(self, password):
        self.password_input.fill(password)

    def click_submit(self):
        self.login_submit_button.click()


def test_invalid_login(page: Page):
    page.goto(BASE_URL)
    main_page = MainPage(page)
    login_page = LoginPage(page)
    login, password = generate_random_credentials()

    main_page.open_login_card()
    login_page.fill_username(login)
    login_page.fill_password(password)
    login_page.click_submit()

    expect(login_page.button_spinner).to_be_visible()
    expect(login_page.button_spinner).not_to_be_visible()
    expect(login_page.error_login_message).to_be_visible()
    expect(login_page.error_login_message).to_have_text("Invalid login or password.")
