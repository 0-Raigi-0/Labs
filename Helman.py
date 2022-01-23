import random
g = int(input())
p = int(input())
a = random.randrange(10000000, 9999999999)
b = random.randrange(10000000, 9999999999)
A = (g**a) % p
B = (g**b) % p
K_a = (B**a) % p
K_b = (A**b) % p
print(K_a)
print(K_b)