# f = open('file.txt', 'w')
# f = open('append_file_name', 'a')
# f = open('read_file_name', 'r')
#
# f.read(1)
#
# f.readline()

# f.write('Witaj\n')
# value = 42
# f.write(value)

# >>>Traceback (most recent call last):
# >>> File "<stdin>", line 1, in <module>
# >>>TypeError: must be str, not int
#
# s = str(value)
# f.write(s)

# Otwórz plik
# fo = open("text.txt", "r")
# print("Nazwa pliku: ", fo.name)
#
# line = fo.readline()
# print("Czytaj linię: >" + line + "<")
# #
# # # Ponownie ustaw wskaźnik na początek
# fo.seek(0, 0)  # fo.seek(0)
# line = fo.readline()
# print("Czytaj linię: >" + line + "<")
#
# # Zamknij otwarty plik
# fo.close()
#
# # Otwórz plik
# fo = open("text.txt", "r")
# print("Nazwa pliku: ", fo.name)
#
# # Uzyskaj aktualną pozycję pliku.
# pos = fo.tell()
# print("Aktualna pozycja: " + str(pos))
#
# line = fo.readline()
# print("Czytaj linię: >" + line + "<")
#
# # Uzyskaj aktualną pozycję pliku.
# pos = fo.tell()
# print("Aktualna pozycja: " + str(pos))
#
# # Zamknij otwarty plik
# fo.close()

# Napisz program w Pythonie, aby odczytać i wyświetlić cały plik tekstowy.
# fo = open("text.txt", "r")
# print(fo.read())

# Odczytywanie pliku wiersz po wierszu i zapisywanie go na liście
# fo = open("text.txt", "w")
# try:
#     fo.write('hello world')
# finally:
#     fo.close()
# z instrukcja with powyższy kod:
# with open('text.txt', 'w') as file:
#     file.write('hello world !!!')


# Napisz program w Pythonie, który odczyta plik tekstowy wiersz po wierszu i zapisze
# go na liście content_list.
# content_list to lista zawierająca przeczytane wiersze.
# Możesz skorzystać z podpowiedzi (podanej dalej - chodzi o with)

# with open('text.txt', 'r') as file:
#     line = file.readlines()
# print(line)
# print(line[1])

# Napisz program w Pythonie, który znajdzie najdłuższe słowa w pliku tekstowym
# with open('text.txt', 'r') as file:
#     a = file.read()
# # b = type(a)
# c = a.split()
# max = ''
# for n in c:
#     len(n)> len(max)
#     max = n
# print(max)

# def longest_word(filename):
#     with open(filename, 'r') as infile:
#         words = infile.read().split()
#     max_len = len(max(words, key=len))
#     return [word for word in words if len(word) == max_len]
#
#
# print(longest_word('text.txt'))

# Napisz program w Pythonie, który zapisze listę do pliku
#
# lista = [1, 'bbbbb', 'sdsdsd']
# with open('nowy.txt', 'a') as file:
#     for n in lista:
#         file.write(str(n) + '\n')
#
# Ćwiczenie
# Napisz program w Pythonie, aby ocenić, czy plik jest zamknięty, czy nie.

f = open('text.txt', 'r')
print(f.closed)
if not f.closed:
    f.close()
    print(f.closed)
else:
    print(f.closed)