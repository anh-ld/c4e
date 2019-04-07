from models.customer import Customer
import mlab
from faker import Faker
from random import randint, choice

mlab.connect()

fake = Faker()
# create a document
for i in range(100):
    new_customer = Customer(
        name = fake.name(),
        gender = randint(0,1), # 0: female, 1: male
        email = fake.safe_email(),
        phone = fake.phone_number(),
        job = fake.job(),
        company = fake.company(),
        contacted = choice([True, False])
    )
    new_customer.save()
