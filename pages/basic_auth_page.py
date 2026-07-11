from ui.web_element import WebElement
from playwright.sync_api import Page


class BasicAuthPage:
    def __init__(self, page: Page):
        self.page = page

        self.text_message = WebElement(
            locator=page.get_by_text("Congratulations! You must have the proper credentials."),
            description="Сообщение после успеха base auth",
            page=page,
        )

    def assert_text_message(self):
        return (
                self.text_message.get_text_content()
                == "Congratulations! You must have the proper credentials."
        )
