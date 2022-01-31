# class NazwaKlasy:
#     pass
#
# obiekt = NazwaKlasy()
# print(type(obiekt))

# class NazwaKlasy:
#
#     def nazwa_metody(self, argument1, argument2):
#         print(argument1)
#         print(argument2)
#
# obiekt = NazwaKlasy()
# obiekt.nazwa_metody(1,2)

# """Dokumentacja modułu"""
#
# class MyClass:
#     """Dokumentacja klasy"""
#
#     def my_method(self):
#         """Dokumentacja metody"""
#
# def my_function():
#     """Dokumentacja funkcji"""
# help(MyClass)
#
# help(MyClass.my_method)

# class NazwaKlasy:
#     atrybut_pierwszy = "Wartość"
#     atrybut_drugi = 123.0

# class NazwaKlasy:
#     def __init__(self, trzeci):
#         self.atrybut_pierwszy = "Wartość"
#         self.atrybut_drugi = 123.0
#         self.atrybut_trzeci = trzeci
#
# instancja = NazwaKlasy("trzeci")
# print(instancja.atrybut_trzeci)

# class MyClass:
#     x = 5
# p1 = MyClass()
# print(p1.x)
#
# class Parrot:
#     # atrybut klasy
#     species = 'ptak'
#     # atrybut instancja
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# blu = Parrot('Blu', 10)
# woo = Parrot('Woo', 15)
#
# # uzyskanie dostępu do atrybutów klasy
# print("Blu to", blu.__class__.species)
# print("Woo to również", woo.__class__.species)
# # za chwilę wytłumaczymy sobie dokładniej o co chodzi z __class__
# print("Blu to", blu.name, blu.age)
# print("Woo to również", woo.name, woo.age)


# class Parrot:
#
#     # atrybuty instancji
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # metoda instancji
#     def sing(self, song):
#         return self.name + " śpiewa " + song
#
#     def dance(self):
#         return self.name + " teraz tańczy"
#
# blu = Parrot('blu', 10)
# print(blu.sing('happy'))
# print(blu.dance())

# class Person:
#
#     def __init__(self, name, age):
#
#         self.name = name
#         self.age = age
#     def my_func(self):
#         print("cześć, mam na imie: " + self.name)
#
# p1 = Person('Tom', 36)
#
# print(p1.name, ' ', p1.age)
# p1.my_func()
# nie musi byc self ale raczej tak sie przyjelo
# class Person:
#     def __init__(mysillyobject, name, age):
#         mysillyobject.name = name
#         mysillyobject.age = age
#
#     def myfunc(abc):
#         print("Cześć, mam na imię " + abc.name)

# modyfikowanie atrybutów z zewnatrz
#
# class Person:
#
#     def __init__(self, name, age):
#
#         self.name = name
#         self.age = age
#     def my_func(self):
#         print("cześć, mam na imie: " + self.name, ' i mam ', self.age)
#
# p1 = Person('Tom', 36)
# print(p1.name, ' ', p1.age)
# p1.my_func()
#
# p1.age = 40
# p1.my_func()
#
# # mozna usuwać atrybuty i obiekty
# # del p1.age
# # p1.my_func()
# del p1
# p1.my_func()
#
# ćw1
# Klasa o nazwie MyClass z atrybutem o nazwie x
# No to jeszcze raz! Utwórz klasę o nazwie MyClass z atrybutem
# o nazwie x = 5.
# Teraz użyj klasy o nazwie MyClass do stworzenia obiektu.
# Utwórz obiekt o nazwie p1 i wydrukuj wartość x.
#
# class MyClass:
#     x = 5
# p1 = MyClass()
# print(p1.x)

# klasa kont bankowych

# class Account:
#     def __init__(self, nazwa, stan = 0):
#         self.nazwa = nazwa
#         self.stan = stan
#
#     def info(self):
#         print('nazwa: ', self.nazwa)
#         print('stand kont: ', self.stan)
#
#     def wyplac(self, ilosc):
#         self.stan -= ilosc
#     def wplac(self, ilosc):
#         self.stan += ilosc
#
# jk = Account("Roch Kowalski", 1000)
# jk.info()
# jk.wplac(2000)
# jk.wyplac(2500)
# jk.info()

# Ćw2
# Utwórz klasę Vehicle bez żadnych zmiennych i metod.
# class Vehicle:
#     pass
#
# Ćw3
# Klasa (class) dotycząca wyimaginowanego inwentarza odrzutowca
# jest już dla Was zdefiniowana. Również instancja tej klasy Jets
# jest stworzona i przypisana do zmiennej first_item. Wydrukuj name z first_item.

# class Jets:
#
#
#     def __init__(self, name, country):
#         self.name = name
#         self.origin = country
#
#
#
# first_item = Jets("F16", "USA")
#
#
# a = first_item.name
# print(a)
#
# Ćw4
# Tym razem wydrukuj origin z first_item.

#
# class Jets:
#     model = None
#     country = 0
#
#     def __init__(self, name, country):
#         self.name = name
#         self.origin = country
#
#
#
# first_item = Jets("F16", "USA")
#
# a=first_item.name
# b=first_item.origin
#
#
# print(a,b)


# Ćw5
# Utwórz klasę Vehicle z atrybutami instancji max_speed i mileage.
# Stwórz obiekt i w trakcie inicjacji przypisz jego atrybutom
# (odpowiednio) wartości 240 i 18.
# Wydrukuj te atrybuty.

# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
# a = Vehicle(240, 18)
# print(a.max_speed, a.mileage)

# Ćw6
# Utwórz klasę Car z dwoma atrybutami instancji:
# 1.color, który przechowuje nazwę koloru samochodu jako ciąg testowy (str)
# 2.mileage, który przechowuje liczbę kilometrów przejechanych przez
# samochód jako liczbę całkowitą (int)
#
# Następnie utwórz instancję dwóch obiektów Car - niebieski samochód
# mający 20 000 kilometrów przebiegu i czerwony samochód mający
# 30 000 kilometrów przebiegu - i wydrukuj ich kolory oraz przebiegi.
# Twój wynik powinien wyglądać następująco
#
# Niebieski samochód ma 20,000 kilometrów przebiegu.
# Czerwony samochód ma 30,000 kilometrów przebiegu.
#
# # nie działa :(
# class Car:
#     def __init__(self, color, mileage):
#         self.color = color
#         self.mileage = mileage
# car1 = Car('Niebieski', 20000)
# car2 = Car('Czerwony', 30000)
# car3 = Car('Zielony', 100000)
#
# # for x in ('Niebieski', 'Czerwony', 'Zielony'):
# #     print(x.color, x.mileage,)
#
# print(car1.color, 'samochód ma',car1.mileage,'kilometrów przebiegu.')
# print(car2.color, 'samochód ma',car2.mileage,'kilometrów przebiegu.')


# Ćw7
#
# Stwórz nowe instancje od pierwszej do szóstej pozycji w tej kolejności:
# F14, SU 33, AJS37, Mirage 2000, Mig 29, A10. Możesz sprawdzić Podpowiedź 1,
# aby sprawdzić origin
#
# Wskazówka 1
# SU33: Rosja
# AJS37: Szwecja
# Mirage2000: Francja
# F14: USA
# Mig29: ZSRR
# A10: USA
#
# Wskazówka 2
# Możesz utworzyć instancje w następujący sposób:
# first_item=Jets(name, country)
#
# class Jets:
#     def __init__(self, name, country):
#         self.name = name
#         self.origin = country
#     def x(self, other_jet):
#         print(self.name, self.origin)
#         print(other_jet.name, other_jet.origin)
#
# first_item = Jets('F14', 'USA')
# second_item = Jets('SU33', 'Rosja')
# third_item= Jets('AJS37', 'Szwecja')
# fourth_item= Jets('Mirage2000', 'RFrancja')
# fifth_item= Jets('Mig29', 'ZSRR')
# sixth_item= Jets('A10', 'USA')
#
# first_item.x(first_item)
# first_army = [first_item.name,second_item.name,third_item.name,fourth_item.name,fifth_item.name,sixth_item.name]
# print(first_army)

# ćw 8
#
# Dodaj kolejny atrybut o nazwie „quantity” do metody inicjalizacji
# (zwykle nazywanej konstruktorem lub __init__).
# Następnie zdefiniuj przypisanie tego atrybutu do atrybutu self.quantity
# wewnątrz konstruktora.
# Następnie utwórz 2 instancje dla: F14 i Mirage2000 z ilościami 87 i 35
#
# Wskazówka 1
# Możesz dodać parametr quantity do konstruktora w następujący sposób:
# def __init__(self, name, country, quantity):
# Następnie musisz przypisać ten parametr do atrybutu self, aby istniało
# sensowne połączenie między parametrem a atrybutem.
#
# Wskazówka 2
# Możesz dodać parametr quantity do konstruktora w następujący sposób:
# def __init__(self, name, country, quantity):
#
#     self.name = name
#     self.origin = country
#     self.quantity = quantity
# Następnie musisz przypisać ten parametr do atrybutu self,
# aby istniało sensowne połączenie między parametrem a atrybutem.
#
# Wskazówka 3
# Możesz tworzyć instancje klasy Jets jak poniżej:
# first_item=Jets("F14","USA",87)
# second_item=Jets("Mirage2000","France",35)

class Jets:
    def __init__(self, name, country, quantity):
        self.name = name
        self.origin = country
        self.quantity = quantity

first_item = Jets('F14', 'USA', 87)
second_item = Jets("Mirage2000","France",35)
third_item = Jets("MIG29", "ZSRR", 10)
fourth_item = Jets("SU33", "Rosja", 15)

a = [first_item, second_item, third_item, fourth_item]
total2=0
for planes in a:
    total2 += planes.quantity
print(total2)
total = first_item.quantity + second_item.quantity
print(total)
