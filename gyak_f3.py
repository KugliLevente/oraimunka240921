#A program  olvasson be a konzolról egy valós számot! 
#A program számítsa ki a szám abszolút értékét, és írja ki az eredményeket a konzolra! 
#A számításhoz a math.fabs() függvény helyett elágazást használjon!

inputFromUser = float(input("Adj meg egy valós számot: "))

if inputFromUser >= 0:
    print("|" + str(inputFromUser) + "| = " + str(inputFromUser))
else:
    print("|" + str(inputFromUser) + "| = " + str(-inputFromUser))