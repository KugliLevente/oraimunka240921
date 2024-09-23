# A program számítsa ki egy beolvasott valós szám négyzetgyökét! 
# A program adjon hibaüzenetet, ha a felhasználó negatív számból akar gyököt vonni!

import math

inputFromUser = float(input("Adj meg egy valós számot: "))

if inputFromUser >= 0:
    print(math.sqrt(inputFromUser))
else:
    print("Hibás bemenet! Negatív számból nem lehet gyököt vonni!")