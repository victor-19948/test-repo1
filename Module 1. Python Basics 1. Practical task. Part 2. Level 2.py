x1 = int(input('номер столбца первой клетки: '))
y1 = int(input('номер строки первой клетки: '))
x2 = int(input('номер столбца второй клетки: '))
y2 = int(input('номер строки второй клетки: '))
if x1 == x2:
    print('YES')
elif y1 == y2:
    print('YES')
else:
    print('NO')
