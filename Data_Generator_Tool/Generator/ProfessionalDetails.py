from faker import Faker
from barnum import gen_data
global obj
obj = Faker()

def get_job():
    return obj.job()

def get_company_name():
    return gen_data.create_company_name()

def get_email_address():
    return gen_data.create_email(tld="co.uk")
