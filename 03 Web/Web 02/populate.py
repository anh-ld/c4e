from models.service import Service
import mlab
from faker import Faker
from random import randint, choice

mlab.connect()

fake = Faker()
# create a document
for i in range(100):
    print("Saving service", i + 1)
    new_service = Service(
        name = fake.name(),
        yob = randint(1995, 2000),
        gender = randint(0, 1),
        height = randint(150, 180),
        phone = fake.phone_number(),
        address = fake.address(),
        status = choice([True, False])
    )

    new_service.save()

# print(fake.address())
