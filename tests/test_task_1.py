from utils.url_utils import embed_credentials_in_url
from ui.web_element import WebElement
from playwright.sync_api import Page
from pages.basic_auth_page import BasicAuthPage

url = "http://the-internet.herokuapp.com/basic_auth"

# Это бы я сохранил в .env
login = "admin"
password = "admin"


def test_basic_auth(basic_auth_page: BasicAuthPage, actions):
    """
    1. Перейти по URL
    2. Выполнить авторизацию с корректными учетными данными
    login: admin
    password: admin

    3. Получить текст, отображаемый на странице
    Текст соответствует: Congratulations! You must have the proper credentials.
    """

    actions.goto(embed_credentials_in_url(url, login, password))

    assert basic_auth_page.assert_text_message()
