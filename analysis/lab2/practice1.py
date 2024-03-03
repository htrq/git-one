import numpy as np
from math import ceil, floor, factorial    # это как импортировать несколько методов из библиотеки
import sys
import subprocess

print(ceil(4.5))
print(floor(4.5))
fact = 4
print("Факториал: ", fact, ' ', factorial(fact))

print("Аргументы с которыми запущена программа: ", sys.argv)
print("subprocess.STDOUT: ", subprocess.STDOUT)


a = np.array(['3', '4',])   # create numpy array
print("Массив: ", a)
print("Тип: ", type(a))
z = list(a) # так можно превратить массив numpy в простой
print("Тип нового, превращенного массива: ", type(z))

# ndim shape size
print("a.ndim: ", a.ndim)
print("a.shape: ", a.shape)
print("a.size: ", a.size)

b = np.array([[1, 2, 3], [4, 5, 6]])
print("Массив b: \n", b)
print("b.ndim: ", b.ndim)
print("b.shape: ", b.shape)
print("b.size: ", b.size)

#c = np.array([['1', '2', '3'], ['4', '5', '6', '7']])   # ошибка из-за размерности

print("массив где элементы меньше 3:", b[b<3])   # вывести массив где элементы меньше 3
print("Ко всем элементам массива b применен sin: ", np.sin(b))
print("Превращение многомерного массива в вектор: ", b.ravel())
print("Превращение b в массив 3 по 2: ", b.reshape(3,2))
print("reshape(3, -1) -1 значит что по одной оси будет высчитано програмно: ", b.reshape(3, -1))


a1 = np.arange(2, 10)
a2 = np.arange(0, 8)
a3 = a1 * a2
triples = zip(a1, a2, a3)
print(triples)  # так выводит просто тип
print([triple for triple in triples])   # чтобы вывести содержимое нужно использовать цикл
