i = 0
counter = 0

numbArr = list(map(int, input("Введіть числа для списку через пробіл: ").split()))
numbArr.append(0)
maximum = max(numbArr)
while numbArr[i] != 0:
    if numbArr[i] == maximum:
        counter += 1
    i += 1
print("Кількість чисел, рівних найбільшому: ", counter)