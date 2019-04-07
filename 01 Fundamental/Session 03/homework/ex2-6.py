sheep_size = [5,7,300,90,24,50,75]
print("Hello, my name is Duy Anh and here is my flock")
print(sheep_size)
print()

biggest_sheep = max(sheep_size)
print("Now my biggest sheep has size",biggest_sheep,"let's shear it")

pos = sheep_size.index(biggest_sheep)
sheep_size[pos] = 8
print("After shearing, here is my flock")
print(sheep_size)
print()

for i in range(2):
    print("MONTH",i + 1,":")
    
    for i in range(len(sheep_size)):
        sheep_size[i] += 50
    print("One month has passed, now here is my flock")
    print(sheep_size)

    biggest_sheep = max(sheep_size)
    print("Now my biggest sheep has size",biggest_sheep,"let's shear it")

    pos = sheep_size.index(biggest_sheep)
    sheep_size[pos] = 8
    print("After shearing, here is my flock")
    print(sheep_size)
    print()

print("MONTH 3 :")
for i in range(len(sheep_size)):
    sheep_size[i] += 50
print("One month has passed, now here is my flock")
print(sheep_size)
print()

total = sum(sheep_size)
print("My flock has size in total:",total)
print("I would get ",total," * 2$ = ",total*2,"$",sep='')
