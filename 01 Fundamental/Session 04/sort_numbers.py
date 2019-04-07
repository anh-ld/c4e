x = [8,7,6,5,4,3,2,1]
y = []
while len(x) != 0:
    y.append(min(x))
    x.remove(min(x))
print(y)
# # bubble sort
# z = [8,7,6,5,4,3,2,1]
# for i in range(len(z)):
#     for j in range(len(z) - 1):
#         if z[j] > z[j + 1]:
#             z[j], z[j + 1] = z[j + 1], z[j]
# print(z)
