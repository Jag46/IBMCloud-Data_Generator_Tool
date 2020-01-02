from faker import Faker
fake = Faker()
from faker.providers import BaseProvider



class providers(BaseProvider):
    def bank_customer(self):
        return fake.random_int(10**9, ((10**10)-1))
    def bank_ibanNumber(self):
        return fake.iban()

fake.add_provider(providers)

#print(fake.bank_customer())
#print(fake.bank_ibanNumber())