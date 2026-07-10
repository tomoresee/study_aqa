from faker import Faker

from enum import StrEnum


class SortOrder(StrEnum):
    PRICE_LOW_TO_HIGH = "Price: low to high"
    PRICE_HIGH_TO_LOW = "Price: high to low"


def generate_random_credentials():
    fake = Faker()

    login = fake.user_name()
    password = fake.password(length=12)

    return login, password
