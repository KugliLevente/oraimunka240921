# A program olvassa be a konzolról egy kör sugarát! 
# Ha a sugár nem pozitív, akkor a program írja ki konzolra, hogy 
# "Hiba: a kör sugara nem pozitív!"; 
# egyébként a program számítsa ki és írja ki a kör kerületét, területét a konzolra!

import math

inputFromUser = float(input("Add meg a kör sugarát: "))

if inputFromUser <= 0:
    input("Hiba: a kör sugara nem pozitív!")
else:
    circumference = inputFromUser * 2 * math.pi
    area = math.pow(inputFromUser, 2) * math.pi
    print("A kör kerülete: " + str(circumference) + "cm")
    print("A kör területe: " + str(area) + "cm^2")