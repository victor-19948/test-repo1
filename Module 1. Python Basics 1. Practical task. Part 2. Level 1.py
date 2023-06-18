a = int(input('первое число: '))
b = int(input('второе число: '))
c = int(input('третье число: '))
quantity = 0
if a == b:
    quantity += 1
if a == c:
    quantity += 1
if b == c:
    quantity += 1
if (quantity == 1) | (quantity == 2):
    value = 2
elif quantity == 3:
    value = 3
else:
    value = 0
print(value)
