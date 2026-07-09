from playwright.sync_api import Page


class SearchPage:
    def __init__(self, page: Page):
        self.sort_dropdown = page.get_by_test_id("filter-sort")
        self.apply_filters_button = page.get_by_test_id("apply-filters-button")
        self.search_result_prices = page.locator("[data-testid^='search-result-price-']")
        self.results_loader_track = page.get_by_test_id("results-loader-track")

    def select_sort(self, filter_type):
        self.sort_dropdown.select_option(filter_type)
        self.apply_filters_button.click()

    def is_loader_visible(self) -> bool:
        return self.results_loader_track.is_visible()

    def is_loader_hidden(self) -> bool:
        try:
            self.results_loader_track.wait_for(state="hidden")
            return True
        except TimeoutError:
            return False

    def get_prices(self, n) -> list:
        return [
            int(price.get_attribute("data-price"))
            for price in self.search_result_prices.all()[:n]
        ]

    def are_prices_sorted(self, n, sort_type) -> bool:
        prices = self.get_prices(n)

        print(prices)

        if sort_type == "Price: low to high":
            return prices == sorted(prices)

        elif sort_type == "Price: high to low":
            return prices == sorted(prices, reverse=True)

        return False
