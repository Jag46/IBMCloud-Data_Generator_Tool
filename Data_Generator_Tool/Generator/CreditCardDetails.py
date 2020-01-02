from faker import Faker

global obj
obj = Faker()

def get_credit_card_number():
    return obj.credit_card_number(card_type=None)

def get_credit_card_provider():
    return obj.credit_card_provider(card_type=None)

def get_credit_card_security_code():
    return obj.credit_card_security_code(card_type=None)