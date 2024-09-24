# A program döntse el és írja ki, hogy egy beolvasott egész szám kétjegyű-e!

inputFromUser = int(input("Adj meg egy számot: "))

if (inputFromUser >= 10 and inputFromUser <= 99) or (inputFromUser <= -10 and inputFromUser >= -99):
    print("A(z) " + str(inputFromUser) + " szám kétjegyű!")
else:
    print("A(z) " + str(inputFromUser) + " szám nem kétjegyű!")