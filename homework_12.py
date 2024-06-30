# Citeste de la tastatura o cifra(n) si apoi o lista de numere intr un fisier
# aranjeaza le in matrici de nXn si scrie le
# intr un alt fisier care sa se numeasca fisier_n unde n e cifra.
# Daca se termina numerele inainte de a se completa matricea este in regula.
#
# ex 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
# n=3
# 1 2 3
# 4 5 6
# 7 8 9
#
# 10 11 12
# 13 14 15
# 16 17
import sys
figure = int(input("Dati o cifra:"))
with open("numere.txt", "r") as file:
    numbers = file.read()
    numbers = numbers.split(", ")
with open("fisier_n.txt", "w") as f:
    x = 0
    k = 0
    for i in numbers:
        print(i, end=" ", file = f)
        x += 1
        if x % figure == 0:
            print(" ", file = f)
            k+=1
            if k % figure == 0:
                print(" ", file = f)












