n = int(input("Insert n: "))
s = 1
for i in range(1,n + 1):
    s *= i
print("Factorial of",n,"is",s)
# a faster way
# import math
# print("Factorial of",n,"is",math.factorial(n))
