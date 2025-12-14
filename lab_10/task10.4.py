import numpy as np

A = np.array([2, 4, 6, 8])
B = np.array([1, 2, 3, 4])

print("Масив A:", A)
print("Масив B:", B)

print("\nДодавання масивів:", A + B)
print("Віднімання масивів:", A - B)
print("Множення масивів:", A * B)
print("Ділення масивів:", A / B)

C = np.concatenate((A, B))
print("\nОб'єднаний масив C:", C)

print("\nМаксимальний елемент:", np.max(C))
print("Мінімальний елемент:", np.min(C))
print("Сума елементів:", np.sum(C))
print("Добуток елементів:", np.prod(C))
