# Lista1

'''
UWAGA! Nie należy zmieniać nazw funkcji, oraz wartości zmiennych podanych w pliku
poza wartościami ze stringiem "PODAJ WYNIK" - w tych zmiennych należy przechowywać wynik
dotyczący poszczególnych zadań w_1, w_2 ... w_6.

Ciało funkcji wpisujemy w kodzie zamiast "pass".

Wyniki z każdego zadania powinny wyświetlać się w jednej linijce.
Nie należy wyświetlań nic poza wynikiem działania kodu z poszczególnych zadań
w kolejności tak jak w pliku.
Plik należy zapisać w postaci: imie_nazwisko_lista1.py
'''

# 1. Ile unikatowych elementów znajduje się w liście:
# 1 pkt
import random
import re

lista_1 = [0, 7, 8, 3, 3, 0, 7, 0, 3]

w_1 = len(set(lista_1))
print(w_1)

# 2. Napisz kod, który podmieni losowy znak ze stringa
s_2 = "ala ma kota"
# na '0':
# 2 pkt
list_string = list(s_2)
list_string[random.randint(0, len(list_string) - 1)] = '0'
w_2 = "".join(list_string)
print(w_2)

# 3. Napisz kod który podmieni z lista_3 język programowania R na JS, następnie wyświetl podmieniony JS.
# Przed JS nadal musi znajdować się python w strukturze takiego samego typu jak w przykladowej lista_3.
# 2pkt
lista_3 = [[{1: 'java', 0: ('python', 'R')}, 'c++'], ['word', 'excel']]

lista_3[0][0].update({0: ('python', 'JS')})
w_3 = lista_3
print(w_3)

# 4. Jakiego typu dane z poniższych nie mogą być kluczami słownika?
# boolean,float,int,string,tuple,list,set. Odpowiedź umieśc w stringu w_4
# 1 pkt

w_4 = "list, tuple, set"
print(w_4)

# 5. Dla stringa wypisz
# ile razy pojawił się dany znak, w kolejności alfabetycznej.
# Użyj słownika - wynik również ma być słownikiem
# 2 pkt

s_5 = "ala ma kota imie ma macko"
charcounter = {}

for char in s_5:
    if char not in charcounter:
        charcounter[char] = s_5.count(char)

w_5 = {}

for key in sorted(charcounter.keys()):
    value = charcounter[key]
    w_5[key] = value

print(w_5)

# 6. Napisz kod który sprawdzi, czy w poprzednim stringu s_5,
# jakikolwiek znak wystąpił dokładnie 3 razy. Wyświetl Tak jeżeli wystąpił,
# Nie jeżeli nie wystąpił.
# 1 pkt

w_6 = "NIE"

for key in w_5.keys():
    if w_5[key] == 3:
        w_6 = "TAK"
        break
print(w_6)


# 7. Napisz funkcję sprawdzającą czy podane słowa/zdania są palindromem
# i zwróci True lub False ( jest/ nie jest)
# pomiń znaki nie będące literami.
# 3pkt

def palindrom(s):

    lowerString = re.sub(r'[^a-zA-Z]', '', s.lower())

    for i in range(0, len(lowerString) // 2):
        if lowerString[i] != lowerString[len(lowerString) - 1 - i]:
            return False

    return True


s_7_1 = "Nowy Targ, góry, Zakopane – na pokazy róg, graty won"
print(palindrom(s_7_1))


# 8. Napisz funkcję, która wyświetli
# wszystkie liczby od 1 do n, jednak jeżeli liczba jest podzielna przez:
# trzy – wypisze „Fizz”,
# pięć – wypisze „Buzz”,
# trzy i pięć wypisz „FizzBuzz”.
# wszystkie liczby/słowa mają zostać wyświetlone w jednej linii, oraz być rozdzielone przecinkiem
# BEZ spacji
# 2 pkt

def fizzbuzz(n):
    returnString = ""
    for i in range(1, n + 1):
        returnString += f"{i}"
        fizzString = ""

        if i % 3 == 0:
            fizzString += "Fizz"

        if i % 5 == 0:
            fizzString += "Buzz"

        if fizzString != "" and i != n:
            fizzString += ","
        if i != n:
            returnString += ','

        returnString += fizzString

    return returnString


n_8 = 16
print(fizzbuzz(n_8))

# 9. Napisz funkcję zwracającą n-ty element ciągu Fibonacciego
# bez rekurencji:
# 3 pkt

n_9 = 6


def fibonacci(n):
    pass


print(fibonacci(n_9))


# 10. Napisz funkcję, która dla podanej posortowanej listy
# zwróci index wyszukiwanego elementu za pomocą wyszkukiwania binarnego,
# lub zwróci None gdy nie ma elementu w liscie:
# 3 pkt


def binary_search(lista, e):
    pass


l_10 = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]
print(binary_search(l_10, 2))
