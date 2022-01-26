# funkcje anonimowe (lambda)
# lambda arg1, arg2: arg1**arg2
# c = lambda a, b: ((a**2) + (b**2))**0.5
# print(c(3,4))
# print(lambda 3,4)
# filtrowanie
temperatury = [
    37.6, 35.8, 37.6, 33.4, 34.1, 37.1, 35.9, 34.1, 37.1, 40.5, 38.5, 37.6,
    35.8, 34.5, 36.4, 38.3, 37.5, 37.7, 34.0, 35.3, 35.7, 38.9, 34.8, 34.1,
    39.6, 35.4, 34.7, 37.6, 38.4, 36.4, 39.8, 39.1, 37.1, 35.6, 36.8, 37.6,
    36.7, 40.0, 38.0, 34.1, 35.5, 38.5, 36.1, 32.6, 32.9, 34.5, 41.0, 38.3,
    33.7, 38.7, 36.9, 36.2, 33.7, 38.3, 35.3, 38.3, 40.1, 39.3, 38.2, 37.6,
    39.1, 37.1, 34.4, 38.7, 35.8, 38.2, 38.2, 33.1, 37.8, 36.5, 37.6, 37.4,
    34.3, 37.7, 36.0, 37.5, 37.6, 36.5, 31.3, 37.7, 40.3, 39.5, 35.7, 38.1,
    34.7, 36.5, 34.3, 38.0, 37.0, 38.5, 39.4, 37.6, 41.7, 40.0, 38.4, 38.9,
    34.2, 40.2, 34.3, 35.3
]
# wynik = list(filter(lambda x: x>=40.0, temperatury))
# print(wynik)
# wynik_sort = sorted(wynik)
# print(wynik_sort)

##aplikowanie
# print(temperatury)
# from statistics import mean
# sr_temp = mean(temperatury)
# print(sr_temp)
#
# #odchylenie od sredniej
# odch = list(map(lambda x: round(x - sr_temp, 1), temperatury))
# print(odch)

# redukowanie
# from functools import reduce
# nums = [1, 2, 3, 4, 5]
# print(reduce(lambda a, b: a+b, nums))
#
# print(reduce(lambda a,b: a * b, [1,2,3,4,5]))

##tworzenie zbiorów danych w locie : list comprehension
# szesciany = []
# for x in range(10):
#     szesciany.append(x**3)
# print(szesciany)
#
# #mozna prosciej
# szesciany2=[x**3 for x in range(10)]
# print(szesciany2)

##kwadraty liczb nieparzystych od 1 do 101
# kwadraty = [el**2 for el in range(1, 102) if el % 2 != 0]
# print(kwadraty)

# ##tworzenie innych zbiorów
# zbior = {znak for znak in 'abracadabra' if znak not in 'abc'}
# print(zbior)

##tworzenie slownika
# tekst='abracadabra'
# wystapienia = {znak: tekst.count(znak) for znak in tekst}
# print(wystapienia)
#
# c = {x: x**2 for x in (2,4,6)}
# print(c)

##wyrazenia generatorowe generator expressions

# list_comp = [x ** 0.5 for x in range(1,11)]
# gene_expr = (x ** 0.5 for x in range(1,11))#ta lista tworzy sie dopiero gdy jest wywoływana,
# #                                               # ta wyzej juz od razu sie zapisuje
#
# for x in list_comp:
#     print(x)
# for x in gene_expr:
#     print(x)

# cw1
# Utwórz funkcję lambda, która przyjmuje jeden parametr (a) i zwraca go
# x = lambda a: a
# print(x('ala'))

# cw2
# Napisz program w Pythonie, aby utworzyć funkcję lambda,
# która dodaje 15 do podanej liczby przekazanej jako argument i zwraca to wynik.
# Następnie wydrukuj wynik.
# y = lambda a: a+15
# print(y(4))

# cw3
# funkcja lambda jako iloczyn dwoch liczb
# z = lambda a, b: a * b
# print(z(-2, 7))

# cw4
# Napisz program w Pythonie wsparcia sortowania
# listy krotek za pomocą lambda po drugim elemencie
# subject_marks = [('Język angielski', 88),
#                  ('Nauka',           90),
#                  ('Matematyka',      97),
#                  ('Nauki społeczne', 82)]
# print(sorted(subject_marks, key = lambda krotka: krotka[1]))

# cw5
# Napisz program w Pythonie, aby posortować za pomocą
# lambda listę słowników po kluczu model lub kolor.

# models = [{'marka': 'Nokia',   'model': '3310',   'kolor': 'Czarny'},
#           {'marka': 'Apple',   'model': '11',     'kolor': 'Złoty'},
#           {'marka': 'Samsung', 'model': 'Galaxy', 'kolor': 'Srebrny'}]
# print(sorted(models, key=lambda a:a["model"]))
# print(sorted(models, key=lambda a:a["kolor"]))

# cw6
# Napisz program w Pythonie, aby sprawdzić, czy dany ciąg (str)
# zaczyna się od znaku ‘P’, używając lambda
# Podpowiedź: skorzystaj z funkcji (metody) startswith()

# tekst = 'Poniewaz ten tekst zaczyna sie na litere p'
# f = lambda a: a.startswith('p')
# print(f(tekst))

# cw7
# Napisz program w Pythonie, aby wyodrębnić rok, miesiąc, dzień i
# godzinę za pomocą lambda
# Podpowiedź: skorzystaj z modułu datetime:
# now = datetime.datetime.now() - przypisuje do nowaktualną lokalną datę i godzinę.
# now.year - wyodrębnia i zwraca rok z now.
# now.month - wyodrębnia i zwraca miesiąc z now.
# now.day - wyodrębnia i zwraca dzień z now.
# now.time() - wyodrębnia i zwraca godzinę z now.
# import datetime
# czas = datetime.datetime.now()
# rok = lambda a : (a.year, a.month, a.day, str(a.time()))
# # miesiac = lambda a : a.month
# # dzien = lambda a : a.day
# # godzina = lambda a : a.time()
#
# print(rok(czas))

# cw8
# Napisz program w Pythonie, aby sprawdzić, czy dany ciąg jest liczbą, czy nie,
# używając lambda
#
# Podpowiedź: przydatna metoda to
# string.replace(oldvalue, newvalue, count)
# Składnia parametrów:
# oldvalue – Wymagany; ciąg do wyszukania
# newvalue – Wymagany; ciąg znaków, który ma zastąpić starą wartość
# count – Opcjonalny; liczba określająca, ile wystąpień starej wartości chcesz zastąpić;
# domyślnie są to wszystkie wystąpienia
tekst = '-a77.8'
# print(tekst.replace('t','b'))
y = lambda i: i.replace('.', '', 1).isdigit()
z = lambda j: y(j[1:]) if j[0] == '-' else y(j)

print(z(tekst))