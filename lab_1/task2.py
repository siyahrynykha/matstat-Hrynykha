i = 0
counter = 0

numbArr = list(map(int, input("Введіть числа для списку через пробіл: ").split()))
numbArr.append(0)
while numbArr[i] != 0:
    if numbArr[i] == max(numbArr):
        counter +1
    i +1
print(counter)