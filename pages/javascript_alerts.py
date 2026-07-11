from ui.page_actions import PageActions
from ui.web_element import WebElement
from playwright.sync_api import Page


class JavascriptAlerts:
    def __init__(self, page: Page):
        self.page = page
        self.actions = PageActions(page)

        self.button_js_alert = WebElement(
            locator=page.get_by_text("Click for JS Alert"),
            description="Кнопка открытия js alert",
            page=page,
        )

        self.result = WebElement(
            locator=page.locator("#result"),
            description="Result message",
            page=page,
        )

    def open_js_alert(self):
        return self.button_js_alert.click()

    def click_js_alert_and_accept(self) -> str:
        return self.actions.run_and_accept_alert(
            self.button_js_alert.click
        )
