import random

print("Rolling the dice...")
saikoro1=random.randint(1,6)
saikoro2=random.randint(1,6)
sum=saikoro1+saikoro2

print(f"Die 1: {saikoro1}")
print(f"Die 2: {saikoro2}")
print(f"Total value: {sum}")

if sum>7:
    print("You won")
else:
    print("You lost")