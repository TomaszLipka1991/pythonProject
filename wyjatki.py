# print(5 * (1 / 0))

# print(4 + x * 3)

# print('2' + 2)
# try except else finally

# try:
#     print("x")
# except:
#     print("Coś poszło nie tak")
# finally:
#     print("Klauzula 'try except' jest zakończona")

# Blok try zgłosi błąd podczas próby zapisu do pliku tylko do odczytu::

# try:
#     file = open("demofile.txt")
#     try:
#         file.write("Lorum Ipsum")
#     except:
#         print("Coś poszło nie tak podczas ZAPISYWANIA do pliku")
#     finally:
#         file.close()
# except:
#     print("Coś poszło nie tak podczas OTWIERANIA pliku")
#
# x = -1
#
# if x < 0:
#     raise Exception("Przepraszamy, brak liczb poniżej zera")

# Ćwiczenie1
# Podczas pisania funkcji najlepiej jest przeprowadzić walidację liczb.
# Jeśli użytkownicy wprowadzą tekst, pojawi się błąd podczas próby konwersji na int.
# Napisz program, który poprosi użytkownika o podanie dwóch liczb.
# Dodaj i wydrukuj wynik.
# Jeśli nie zostanie wprowadzona liczba, zwróć komunikat o błędzie i poproś ponownie.


# while True:
#     try:
#         x = int(input("podaj pierwsza liczbe: "))
#         y = int(input("podaj druga liczbe: "))
#         print(x+ y)
#         break
#     except ValueError:
#         print ('błąd')
#
# Ćw 2
# Wyjątek ZeroDivisionError z instrukcjami try except
# Podziel przez siebie dwie liczby
# Umieść:
# result = "Nie możesz podzielić przez 0"
# we właściwym miejscu, aby program uniknął ZeroDivisionError
# Podpowiedź 1: Po prostu umieść przypisanie wartości dla wyniku po linii Except
# Podpowiedź 2: Zwróć uwagę na wcięcia

# a = 4
# b = 0
# try:
#     result = a/b
# except ZeroDivisionError:
#     result = "Nie mozesz podzielic przez zero"
# print(result)
#
# a = 4
# b = '5fff'
# try:
#     print(a + b)
# except TypeError:
#     pass

# Ćw 4
# Wyjątek Exception z instrukcjami try except
# Spróbuj dodać int dociągu.
# Umieść:
# msg = "Nie możesz dodać int do string"
# by program uniknął błędu BaseException
# Możesz użyć wyjątku Exception, chociaż zwykle powinno się ostrożnie używać tak potężnych instrukcji wyjątków.

# a = 5
# b = 44
# try:
#     msg = a + b
# except TypeError:
#     msg = "Nie możesz dodać int do string"
# print(msg)
#
# Ćwiczenie
# Stwórz trójelementową listę.
# Spróbuj wydrukować piąty element.
# Umieść:
# msg = "Jesteś poza zakresem listy"
# aby uniknąć wyjątku IndexError.
# import sys

# x = [3,4,1,3,44,5]
# msg = x[7]
# try:
#     msg = x[7]
#     print(msg)
# except IndexError:
#     msg = "Jesteś poza zakresem listy: ", sys.exc_info()[]
#     print(msg)

#słowo kluczowe else
# Spróbuj otworzyć do czytania plik (podpowiedź: f = open(arg, "r")).
# W razie braku możliwości otwarcia pliku, obsłuż wyjątek.
# W przeciwnym przypadku wypisz:
# Nazwę pliku;
# Liczbę wierszy (podpowiedź: len(f.readlines()).
# Na koniec zamknij ten plik (podpowiedź: f.close()).
# arg = 'wyjatki2.py'
# try:
#     f = open(arg, "r")
# except IOError:
#     print("Nie można otworzyć pliku")
# else:
#     print("Ilość wierzy: " + str(len(f.readlines())))
#     f.close()
#
#     Ćwiczenie
# # Użyj finally do zamykania obiektów i czyszczenia zasobów.
# # Spróbuj otworzyć i zapisać (podpowiedź: write) w pliku, którego nie można zapisać.
# # Zapewnij, aby program mógł kontynuować bez pozostawiania otwartego obiektu pliku.

try:
    plik = open("wyjatki.py", "r")
    plik.write("string")
except IOError:
    print("błąd")
finally:
    plik.close()

