from playwright.sync_api import Page
import pytest

from pages.main_page import MainPage
from pages.search_page import SearchPage
from utils.config_reader import ConfigReader


@pytest.mark.parametrize("name", ["city", "habits"])
@pytest.mark.parametrize("n", [10, 15])
@pytest.mark.parametrize(
    "filter_type",
    [
        "Price: low to high",
        "Price: high to low",
    ]
)
def test_search_and_filter(page: Page, name, n, filter_type):
    """
    1. Перейти на главную страницу
    2. Ввести в строку поиска название статьи name
    3. Перейти на страницу с результатами поиска
    4. Установить фильтр отображения в значение filter_type
    5. Получить цены первых n статей | Цены отсортированы в соответствии с выбранным фильтром
    """
    page.goto(ConfigReader.get("base_url"))
    main_page = MainPage(page)
    search_page = SearchPage(page)

    main_page.find(name)
    search_page.select_sort(filter_type)
    assert search_page.is_loader_visible(), "Лоадер не появился после применения сортировки"
    assert search_page.is_loader_hidden(), "Лоадер не исчез после загрузки результатов"
    search_page.get_prices(n)

    assert search_page.are_prices_sorted(n, filter_type), (
        f"Цены отсортированы неверно для фильтра '{filter_type}'"
    )
