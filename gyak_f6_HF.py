# A program  kérjen be a konzolról egy valós számot! 
# Ha ez a szám 0 és 360 közé esik, akkor legyen egy szög mértéke (pl. 60 fok), egyébként a program adjon hibaüzenetet! 
# Ha lehet, a program írja ki a szög mértéke alapján a szög típusát (pl.: 60 -> hegyesszög)!

inputFromUser = float(input("Adj meg egy valós számot: "))

if inputFromUser >= 0 and inputFromUser <= 360:
    if inputFromUser == 0:
        print("Nullszög!")
    elif inputFromUser > 0 and inputFromUser < 90:
        print("Hegyesszög!")
    elif inputFromUser == 90:
        print("Derékszög!")
    elif inputFromUser > 90 and inputFromUser < 180:
        print("Tompaszög!")
    elif inputFromUser == 180:
        print("Egyenesszög!")
    elif inputFromUser > 180 and inputFromUser < 360:
        print("Konkávszög!")
    elif inputFromUser == 360:
        print("Teljesszög!")
else:
    print("Hibás bement!")
        