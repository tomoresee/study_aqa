from faker import Faker


def generate_random_credentials():
    fake = Faker()

    login = fake.user_name()
    password = fake.password(length=12)

    return login, password
