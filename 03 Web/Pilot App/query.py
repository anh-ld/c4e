from models.service import Service
import mlab

mlab.connect()

all_services = Service.objects()

# print(all_services[6].name)

id_to_find = "5ac08cfab99c7f2dc4c2f592"

# kieu_anh = Service.objects(id = id_to_find)

# kieu_anh = Service.objects.get(id = id_to_find)

# service = Service.objects.with_id(id_to_find)
#
# if service is None:
#     print("Service not found.")
# else:
#     print(service.to_mongo())
#     # kieu_anh.delete()
#     service.update(set__address = "Tran Duy Hung")
#     service.reload()
#     print(service.address)

# delete all service's docs
for i in all_services:
    i.delete()
