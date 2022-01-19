# def hello(x,y):
#     print(x)
#     print(y)
#
# hello('Hello', 'Python')

# x = float(input('Podaj pierwsza liczbe '))
# y = float(input('Podaj druga liczbe '))
#
# def add(x, y):
#     return x + y
#
# print(add(x,y))
#
# def my_function():
#     """Dokumentacja funkcji"""
# help(my_function)
#
# def fibo(n):
#     """zwraca liczby fibonacciego mniejsze od n"""
#     wynik = []
#     a, b = 0, 1
#     while a < n:
#         wynik.append(a)
#         a, b = b, a+b
#     return wynik

# def fibbonaci_numbers(n):
#     ''' zwraca liczby Fibonacciego mniejsze od n '''
#     wynik = []
#     a, b = 0, 1
#     while a < n:
#     # while len(wynik) < n:
#         wynik.append(a)
#         a, b = b, a+b
#     return wynik
# x = fibbonaci_numbers(10)
# print(x)

#obliczanie długosci łancucha znaków (napisac swoja funkcje len

# def dlugosc(x):
#     z=0
#     for y in x:
#         z += 1
#     return z
# print(dlugosc('jsd'))

# suma elementów listy
# def suma(x):
#     sum = 0
#     for a in x:
#         sum += a
#     return sum
# x = input('Podaj wektor liczb ')
# print(suma([1,2,3]))

#mnozenie elementów listy
#
# def iloczyn(x):
#     iloczyn = x[0]
#     for a in x[1:]:
#         iloczyn = iloczyn * a
#     return iloczyn
# print (iloczyn([2, 2, 3, 6]))

#najwieksza z liczb
#
# def maks(x):
#     a = x[0]
#     for b in x[1:]:
#         if a < b:
#             a = b
#     return a
# print (maks([3,6,-6,0,21,5,6]))

# jaki znak ile razy w ciagu

# def znaki(x):
#     a = {}
#     for i in x:
#         b = a.keys()
#         if i in b:
#             a[i]+=1
#         else:
#             a[i]=1
#     return a
# print(znaki('trtrtr'))


# Ćwiczenie
# Napisz funkcję w Pythonie, który zlicza ciągi znaków, w których długość ciągu wynosi 2 lub więcej,
# a pierwszy' i ostatni znak są takie same z podanej listy ciągów.
# Przykładowa lista : ['abc', 'xyz', 'aba', '1221']
# Oczekiwany wynik: 2
#
# def znaki_listy(x):
#     licznik = 0
#     for a in x:
#         if len(a)>1 and a[0] ==a[-1]:
#             licznik += 1
#     return licznik
# print(znaki_listy(['xxx', 'aaa', 'ab']))

# Ćwiczenie
# Napisz funkcję w Pythonie, aby uzyskać listę posortowaną w
# porządku rosnącym według ostatniego elementu w każdej krotce z podanej listy niepustych krotek.
# Przykładowa lista: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Oczekiwany wynik : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# def sortowanie (x):
#     p = sorted(x)
#     return p
# print(sortowanie([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
#
# def last(x): #parametrem bedzie krotka
#     return x[-1]
#
# def sortowanie (lista):
#     p = sorted(lista, key = last)
#     return p
# print(sortowanie([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# string = "ABC for the purpose of LetterCounting program"
# print(string)
# words = 1
# letters = 0
# hash_table = {}
# for char in string:
#     char = char.lower()
#     if char == ' ':
#         words += 1
#     else:
#         letters += 1
#         if char in hash_table:
#             hash_table[char] += 1
#         else:
#             hash_table[char] = 1
#
# print("Words:", words, "Letters:", letters, "Freq:", hash_table

# def zlozenie (string):
#     l=len(string)
#     if l>=2:
#         p = string[0:2] + string[l-2:l]
#     else:
#         p=''
#     return p
# print(zlozenie("P"))

# def fibbonaci_numbers(n):
#     ''' zwraca liczby Fibonacciego mniejsze od n '''
#     wynik = []
#     a, b = 0, 1
#     while a < n:
#     # while len(wynik) < n:
#         wynik.append(a)
#         a, b = b, a+b
#     return wynik
# x = fibbonaci_numbers(10)
# print(x)

#silnia

# def silnia (n):
#     if n == 1:
#         return 1
#     return silnia(n-1)*n
# print(silnia(2))

# rekurencyjny ciag fibonacciego

# def fibo2 (n):
#     if n ==1 or n==0:
#         return 1
#     return fibo2(n-2) + fibo2(n-1)
#for i in range (15)
    #print(fibo2(n))

