# 2.	MegelőzőKövetkezőSzám: A program kérjen be a konzolról egy egész számot! Ha a szám egyjegyű, akkor a program írja ki a konzolra a számot megelőző és követő egész számot, egyébként ne írjon ki semmit!


inputFromUser = int(input("Adj meg egy egyjegyű számot: "))

if inputFromUser > -10 and inputFromUser < 10:
    print("A(z) " + str(inputFromUser) + " szám megelőző értéke " + str(inputFromUser - 1) + ", következő szám értéke " + str(inputFromUser + 1))