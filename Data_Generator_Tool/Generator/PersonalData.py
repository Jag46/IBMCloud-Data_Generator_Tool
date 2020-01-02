from faker import Faker
from barnum import gen_data
global obj
obj = Faker()

def get_name():
    return obj.name()

def get_name_male():
    return obj.name_male()

def get_name_female():
    return obj.name_female()

def get_mobile_number():
    num = obj.random_int(10**7, ((10**8)-1))
    num = str(num)
    return '74' + num

def get_phone_number():
    return gen_data.create_phone()

    
