# A program döntse el, hogy egy egész szám pozitív-e! Először tájékoztassa a felhasználót, hogy mire való a program! Az egész számot a konzolról kérje be! Ha a szám pozitív, akkor ezt írja ki a konzolra, egyébként ne írjon ki semmit!

inputFromUser = int(input("Adj meg egy egész számot: "))

if inputFromUser > 0:
    print("A szám " + str(inputFromUser) + " pozitív!")
