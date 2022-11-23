import random
random.seed()
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
result = random.randrange(lower,upper,1)
print(result)
