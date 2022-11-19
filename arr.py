import random

arr = []
div2 = []
div = []

for i in range(1,20):
    num = random.randint(1,19)
    arr.append(num)
    if (num % 2 == 0) and (num != 0):
        div2.append(num)
    else:
        div.append(num)

print(f"numbers in an array {arr}")
print(f"\nnumber in an array which are divisible by 2 {div2}")
print(f"\nnumbers in an array which are not divisible by 2 {div}")