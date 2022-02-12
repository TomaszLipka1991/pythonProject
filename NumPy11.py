# import numpy as np
# # print(np.__version__)

# python rozpoznaje rodzaj zmiennej

# l = [1, '2', True, 3.0, None]
# [type(item) for item in l]
#
# ar = np.array([1,2,3,4,5])
# print(ar)
# print(type(ar))

# ar2 = np.array([range(i, i+3) for i in [2,4,6]])
# print(ar2)
#
# sposoby tworzenia tablic w numpy

# zeros = np.zeros((2, 2,2,2,2), dtype = int)
# print(zeros)

# ones = np.ones((5,3), dtype = float)
# print(ones)

# # ciag liniowy
# ciag = np.arange(0, 20, 2)
# print(ciag)

# tablica losowa z rozkładu N(0,1)
# random = np.random.normal(0,1, (3,3))
# print(random)

# Tablica o wymiarach 3x3 z wartościami wylosowanymi z rozkładu N(0, 1)
# rand_int = np.random.randint(1, 10, (4, 5))
# print(rand_int)

# trojwymiarowa tablica z liczbami całkowitymi
# x = np.random.randint(100, size=(2,3,4))
# print(x)
#
# print(f"x ndim: {x.ndim}")  # liczba wymiarów
# print(f"x shape: {x.shape}")  # wymiary tablicy
# print(f"x size: {x.size}")  # całkowity rozmiar tablicy
# print(f"x dtype: {x.dtype}")  # typ danych przechowywanych w tablicy
# print(f"itemsize: {x.itemsize} bytes")  # rozmiar jednego elementu
# print(f"nbytes: {x.nbytes} bytes")  # rozmiar całej tablicy (itemsize x size)
# indeksowanie
# y = np.arange(0,10)
# print(y)
# print(y[5])
# print(y[-2])
# wielowymiarowo:
# x = np.random.randint(100, size=(2,3,4))
# print(x)
# # print(x[0,1,2])
#
# # mozna tez modyfikowac te dane
#
# x[0,1,2]=42
# print(x)

# wycinek fragmentu tabeli
# y = np.arange(0,10)
# print(y)
# print(y[:5])
# print(y[4:7])
# wielowymiar:
# x = np.random.randint(100, size=(2,3,4))
# print(x)
#
# print(x[:1, :, :3])

# Pythonowa lista

# l1 = [1, 2, 3]
# l2 = l1[2:]
# l2[0] = 4
# print(l1)  # l1 pozostaje nie zmienione!
# print(l2)  # l1 pozostaje nie zmienione!

# NumPy
# x = np.zeros((2, 3))
# y = x[0, :]
# y[0] = 1
#
# print(x)  # x i y reprezentują tą samą tablicę!
# print(y)  # x i y reprezentują tą samą tablicę!

# x_copy = x[:2, :2].copy()
# x_copy[0, 0] = 42
#
# print(x)
# print(x_copy)  # zmiana x_copy nie zmieniła x

# zmiana wymiarów tablicy
# a = np.arange(1,10)
# b = np.arange(1,10).reshape((3,3))
# print(a)
# print(b)

# x = np.array([1, 2, 3])
# print(x.reshape((1, 3))) # dwuwymiarowa tablica z jednym wierszem i trzema kolumnami
# print(x.reshape((3, 1))) # dwuwymiarowa tablica z trzema wierszami i jedną kolumną

# grid = np.array([[1, 2, 3],
#                  [4, 5, 6]])
#
# print(np.concatenate([grid, grid]))
# print(np.concatenate([grid, grid], axis=0))
# print(np.concatenate([grid, grid], axis=1))# łączenie wzdłuż drugiego wymiaru

# x = np.array([1, 2, 3])
# grid = np.array([[9, 8, 7],
#                  [6, 5, 4]])
#
# print(np.vstack([x, grid]))
#
# y = np.array([[99],
#               [99]])
# print(np.hstack([grid, y]))


# dzielenie np.split
#
# x = np.arange(10)
# x1,x2,x3 = np.split(x, [3,5])
# print(x1,x2,x3)
# # # wynik [0 1 2] [3 4] [5 6 7 8 9]
#
# # wektory??
#
# def compute_reciprocals(values):
#     output = np.empty(len(values))
#     for i, value in enumerate(values):
#         print(i, value)
#         output[i] = 1.0 / value
#     return output
# values = np.random.randint(1,19, size=5)
# print(values)
# print(compute_reciprocals(values))
