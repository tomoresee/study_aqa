from playwright.sync_api import Page
import pytest

from pages.main_page import MainPage
from pages.search_page import SearchPage
from utils.config_reader import ConfigReader
from utils.data import SortOrderType


@pytest.mark.parametrize(
    "name, n",
    [
        ("city", 10),
        ("habits", 15),
    ]
)
@pytest.mark.parametrize(
    "filter_type",
    [
        SortOrderType.PRICE_LOW_TO_HIGH,
        SortOrderType.PRICE_HIGH_TO_LOW,
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
