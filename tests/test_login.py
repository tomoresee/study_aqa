from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.main_page import MainPage
from utils.data import generate_random_credentials
from utils.config_reader import ConfigReader


def test_invalid_login(page: Page):
    """
    1. Открыть сайт http://144.31.63.127:5000/
    2. Нажать кнопку логина
    3. Ввести случайные данные в поля логина и пароля. Нажать кнопку входа
    4. Проверить что отобразились:
      1. Индикатор загрузки
      2. После исчезновения индикатора появляется сообщение об ошибке "Invalid login or password."
    """
    page.goto(ConfigReader.get("base_url"))
    main_page = MainPage(page)
    login_page = LoginPage(page)
    login, password = generate_random_credentials()

    main_page.open_login_card()
    login_page.login(login, password)

    assert login_page.is_spinner_visible(), "Спиннер не отобразился"
    assert login_page.is_spinner_hidden(), "Спиннер не пропал после загрузки"
    assert login_page.is_error_message_visible(), "Нет сообщения об ошибке"
    assert login_page.get_error_message_text() == "Invalid login or password.", \
        f"Ожидалось: 'Invalid login or password.', Получено: '{login_page.get_error_message_text()}'"
