B = list(map(int, input("Введіть числа через пробіл: ").split()))

newB = []

for i in B:
    if i >= 0:
        newB.append(i)

for i in B:
    if i < 0:
        newB.append(i)

print("Список з невідʼємними числами на початку та відʼємнивми в кінці:", newB)
