# string=input('podaj jakis wyraz ')
# for litera in string:
#     print('litera:', litera)

# warzywa=['marchew', 'kalafior', 'kapusta']
# for warzywo in warzywa:
#     print('warzywo:', warzywo)

# lista=['Rafał', 'Agata', 'Michał', 'Paweł', 'Grzegorz','Robert', 'Aneta', 'Tomasz', 'Monika', 'Klaudia', 'Wiktor', 'Kinga', 'Marcin', 'Tomasz', 'Przemysław']
# lista.sort()
# i=0
# for t in lista:
#     if t[-1] == 'a':
#         i=i+1
# print(i)

# lista = ["Rafal", "Agata", "Michal", "Pawel", "Grzegorz", "Robert", "Aneta", "Tomasz", "Monika", "Klaudia", "Wiktor", "Kinga", "Marcin", "Tomasz", "Przemyslaw"]
#
# lista.sort()
# i=0
# for t in lista:
#     if t[-1]=="a":
#         i=i+1
# print(i)

# print("Przykład range() w Pythonie")
# print("Uzyskaj liczby z zakresu od 0 do 5")
# for i in range(6):
#     print(i, end=', ')

# liczby = list()
# i = 2
# while i < 11:
#     liczby.append(i)
#     i += 2
# print(liczby) # [2, 4, 6, 8, 10]

# lines = list()
# print('Wprowadź tekst po linijce.')
# print('Żeby zakończyć wprowadź pustą linię.')
# line = input('Następna linijka: ')
# while line != '':
#     lines.append(line)
#     line = input('Następna linijka: ')  # reset
# print(lines)

# Zadanie
# Napisz program, który policzy największy wspólny dzielnik dwóch liczb podanych przez użytkownika
# W tym celu użyj operatora % oraz pętli for
# x = int(input('Podaj liczbe x '))
# y = int(input('Podaj liczbe y '))
# n = min(x, y)
#
# #print(z)
# for z in range(n, 0, -1):
#     if x % z == 0 and y % z ==0:
#         print('NWD', x, 'i', y, 'to ', z)
#         break


# Ćwiczenie
# Zobaczmy ćwiczenie, które pomoże lepiej zrozumieć instrukcję pass
# Umieść instrukcję pass, aby blok if nie zgłaszał błędu
# In [ ]:
name = input("Proszę wpisać swoje imię.")
# Wpisz swoją odpowiedź tutaj.

if len(name) > 0:
    print(name)
else:
    pass





