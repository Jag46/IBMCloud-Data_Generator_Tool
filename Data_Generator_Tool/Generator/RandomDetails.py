from faker import Faker
global obj
obj = Faker()


def get_random_digit():
    return obj.random_digit()

def get_date():
    return obj.date(pattern="%Y-%m-%d", end_datetime=None)