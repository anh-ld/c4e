from models.service import Service
import mlab
from faker import Faker
from random import randint, choice

mlab.connect()

fake = Faker()
# create a document

male_img = ["https://i.anh4.com/EwZ5TIN.jpg",
            "https://i.anh4.com/VFPW3Hj.jpg",
            "https://i.anh4.com/3PH8BSN.jpg",
            "https://i.anh4.com/uAPBcfX.jpg",
            "https://i.anh4.com/G0j8Vuo.jpg",
            "https://i.anh4.com/TyIF5bE.jpg",
            "https://i.anh4.com/bl0I8Ug.jpg"]

female_img = ["https://i.anh4.com/qZzBuXW.jpg",
            "https://i.anh4.com/wm6wgI0.jpg",
            "https://i.anh4.com/gUNrhHl.jpg",
            "https://i.anh4.com/LfMn5xs.jpg",
            "https://i.anh4.com/JdrYGT5.jpg",
            "https://i.anh4.com/YauJuH0.jpg"
]
for i in range(55):
    print("Saving service", i + 1)
    new_service = Service(
        name = fake.name(),
        yob = randint(1995, 2000),
        gender = 0,
        height = randint(150, 180),
        phone = fake.phone_number(),
        address = fake.address(),
        status = choice([True, False]),
        description = fake.sentence(nb_words=8, variable_nb_words=True, ext_word_list=None),
        measurements = [randint(50,120), randint(50,120), randint(50,120)],
        image = choice(female_img)
    )

    new_service.save()

# print(fake.address())
