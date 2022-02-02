# class KlasaBazowa:
#     pass
#
# class KlasaPochodna(KlasaBazowa):
#     pass

# class KontoBankowe:
#     def __init__(self, nazwa, stan = 0):
#         self.nazwa = nazwa
#         self.stan = stan
#
#     def info(self):
#         print('nazwa: ', self.nazwa)
#         print('stan kont: ', self.stan)
#
#     def wyplac(self, ilosc):
#         self.stan -= ilosc
#     def wplac(self, ilosc):
#         self.stan += ilosc

# class KontoDebetowe(KontoBankowe):
#     pass
# jk = KontoDebetowe('Antoni', 300)
# jk.info()

# class KontoDebetowe(KontoBankowe):
#     def __init__(self, nazwa, stan=0, limit=0):
#         KontoBankowe.__init__(self, nazwa, stan)
#         self.limit = limit
#
#     def wyplac(self, ilosc):
#         """Jeżeli stan konta po operacji przekroczyłby limit, przerwij."""
#         if (self.stan - ilosc) < (-self.limit):
#             print("Brak srodkow na koncie")
#         else:
#             KontoBankowe.wyplac(self, ilosc)
# jk = KontoDebetowe('Roch Kowalski', 5000, 300)

# metoda super

# class KontoDebetowe(KontoBankowe):
#     def __init__(self, nazwa, stan=0, limit=0):
#         super().__init__(nazwa, stan)
#         self.limit = limit
#
#     def wyplac(self, ilosc):
#         """Jeżeli stan konta po operacji przekroczyłby limit, przerwij."""
#         if (self.stan - ilosc) < (-self.limit):
#             print("Brak srodkow na koncie")
#         else:
#             super().wyplac(ilosc)
# account = KontoDebetowe('Roch', 0, 1000)
# account.wplac(500)
# account.wyplac(2000)
# account.info()

# class A:
#     """Rodzic pierwszy"""
#     def __init__(self):
#         super().__init__()
#         self.a = "A"
#     def fa(self):
#         print("a:", self.a)
# class B:
#     """Rodzic drugi"""
#     def __init__(self):
#         super().__init__()
#         self.b = "B"
#     def fb(self):
#         print("b:", self.b)
# class Pochodna(B, A):
#     """Dziecko"""
#     def __init__(self):
#         super().__init__()
# print(A.__doc__)
# print(B.__doc__)
# print(Pochodna.__doc__)
# d = Pochodna()
# print(d.a)
# print(d.b)
# d.fa()
# d.fb()

# ćw1 klasa figur geometrycznych

import math


# class Figura:
#     def obwod(self):  # L
#         """Obliczanie obwodu."""
#         raise NotImplementedError
#
#     def pole(self):  # S/P
#         """Obliczanie pola powierzchni."""
#         raise NotImplementedError
# # a = Figura()
# a.obwod()
# class Kolo(Figura):
#     """Oblicczanie pola i obwodu koła"""
#     def __init__(self, r):
#         self.r = r
#     def obwod(self):
#         return 2*math.pi*self.r
#     def pole(self):
#         return math.pi*self.r**2
# k1= Kolo(5)
# print(k1.obwod())
# print(k1.pole())
#
# class Trojkat(Figura):
#     def __init__(self, a):
#         self.a = a
#     def obwod(self):
#         return 3*self.a
#     def pole(self):
#         return (self.a)**2 * 3**(1/2)/4
#
# T1 = Trojkat(3)
# print(T1.obwod())
# print(T1.pole())
#
# class Prostokat(Figura):
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def obwod(self):
#         return self.a*2 + self.b*2
#     def pole(self):
#         return self.a * self.b
# P1 = Prostokat(3,4)
# print(P1.obwod())
# print(P1.pole())
#
# class Kwadrat(Prostokat):
#     def __init__(self,a):
#         self.a = a
#         self.b = a
# Kw1 = Kwadrat(3)
# print(Kw1.obwod())
# print(Kw1.pole())
#
# class Rownoleglobok(Prostokat):
#     def __init__(self,a,b,h):
#         self.a = a
#         self.b = b
#         self.h =h
#     def pole(self):
#         return self.a*self.h
# R1 = Rownoleglobok(3,4,5)
# print(R1.obwod())
# print(R1.pole())
#
#
# class TrapezProstokatny(Figura):
#     def __init__(self, a, b, h):
#         self.a, self.b, self.h = a, b, h
#     def obwod(self):
#             return self.a + self.b + self.h + math.sqrt(self.h**2 + (self.a - self.b)**2)
#     def pole(self):
#             return (self.a+self.b)/2 * self.h
# Trap = TrapezProstokatny(4,6,2)
# print(Trap.obwod())
# print(Trap.pole())
# Ćw2
# Utwórz obiekt klasy Bus, która dziedziczy wszystkie zmienne i metody
# klasy Vehicle i wyświetli je.
# Oczekiwany wynik:
# Nazwa pojazdu: Szkolne Volvo Prędkość: 180 Przebieg: 12

# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
# class Bus(Vehicle):
#     pass
# v1 = Bus('Szkolne Volvo', 180, 12)
# print('Nazwa pojazdu:', v1.name, 'Prędkość:', v1.max_speed,
#       'Przebieg:', v1.mileage)

# Ćw3
# Utwórz klasę Bus, która dziedziczy po klasie Vehicle.
# Podaj argument pojemności w metodzie Bus.seating_capacity()
# # o domyślnej wartości 50.
# school_vehicle = Vehicle("Szkolne Volvo", 180, 12)
# print(school_vehicle.seating_capacity(100))
# ma sie tez wywołać print(school_vehicle.seating_capacity()) i pojemnosc ma byc 50
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#
# class Bus(Vehicle):
#
#     def seating_capacity(self, capacity=50):
#         return f"Liczba miejsc siedzących w {self.name} to {capacity} pasażerów"
# k = Bus('volvo', 12,12)
# print(k.seating_capacity())
# k2 = Bus('volvo', 12,12)
# print(k2.seating_capacity(88))

# Ćw4
#
# Zdefiniuj atrybut klasy „color” z domyślną wartością biały.
# Oznacza to, że każdy Vehicle (pojazd) powinien być biały.
# Użyj poniższego kodu do tego ćwiczenia.

# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#     color = 'bialy'
#
# class Bus(Vehicle):
#     color = 'czerwony'
#     pass
#
# class Car(Vehicle):
#     pass
# bus = Bus('Volvo', 12, 160)
# car = Car('Audi Q5', 240, 11)
# print(bus.color, car.color)


# Ćw 5
#
# Utwórz podrzędną klasę Bus, która dziedziczy po klasie Vehicle.
# Domyślna opłata za przejazd dla dowolnego pojazdu to liczba miejsc * 100.
# Natomiast jeśli School_bus to instancja klasy Bus, musimy dodać dodatkowe 10%
# do pełnej ceny jako opłatę za utrzymanie. Tak więc łączna opłata za przejazd
# autobusem stanie się ostateczną kwotą = opłata całkowita + 10% ceny całkowitej.
# Uwaga: autobus może pomieścić 50 osób, więc ostateczna kwota taryfy powinna
# wynosić 5500. Musisz zastąpić metodę fare() klasy Vehicle w klasie Bus.
# Użyj poniższego kodu dla swojej nadrzędnej klasy Vehicle. Musimy uzyskać
# dostęp do klasy nadrzędnej z wnętrza metody klasy potomnej


# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
#     def fare(self):
#         return self.capacity * 100
#
# class Bus(Vehicle):
#     def fare(self):
#         return self.capacity * 110
#
# School_bus = Bus("Szkolne Volvo", 12, 50)
# print("Całkowita opłata za przejazd autobusem wynosi:", School_bus.fare())
#
# print(type(School_bus))


# Ćw 6
#
# Określ, do której klasy należy dany obiekt Bus (sprawdź typ obiektu)
#
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
# class Bus(Vehicle):
#     pass
#
# school_bus = Bus("Szkolne Volvo", 12, 50)
#
# print(type(school_bus))
#
















