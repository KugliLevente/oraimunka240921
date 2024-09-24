# A program olvasson be a konzolról egy egész számot!
# Ha a szám pozitív, akkor legyen a beolvasott szám egy kocka élének hossza. 
# A program számítsa ki és írja ki a kocka felszínét, térfogatát a konzolra! 
# Ha a szám nem pozitív, akkor a program írja ki konzolra, hogy 
# "Hiba: a kocka élének hossza nem pozitív!"!

import math

inputFromUser = int(input("Adj meg egy számot: "))

if inputFromUser > 0:
    surfaceArea = math.pow(inputFromUser, 2) * 6
    volume = math.pow(inputFromUser, 3)
    print("A négyzet felszíne: " + str(surfaceArea) + "cm^2")
    print("A négyzet térfogata: " + str(volume) + "cm^3")
else:
    print("Hiba: a kocka élének hossza nem pozitív!")

