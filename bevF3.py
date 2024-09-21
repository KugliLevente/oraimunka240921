# 3.	Osztályzat1: A program olvasson be a konzolról egy egész számot! Ha a szám 0 és 100 közötti, akkor legyen a beolvasott szám egy százalékérték! A program írja ki a konzolra a százalékban megadott értékelést szövegesen  (0%–59%-ig elégtelen, 60%–69%-ig elégséges,  70%–79%-ig közepes, 80%–89%-ig jó, 90%–100%-ig jeles)!

inputFromUser = int(input("Add meg a százalékos értéket: "))

if (inputFromUser >= 0) and (inputFromUser <= 59):
    print("A megadott " + str(inputFromUser) + "% " + "értékelés elégtelen!")
elif (inputFromUser >= 60) and (inputFromUser <= 69):
    print("A megadott " + str(inputFromUser) + "% " + "értékelés eléséges!")
elif (inputFromUser >= 70) and (inputFromUser <= 79):
    print("A megadott " + str(inputFromUser) + "% " + "értékelés közepes!")
elif (inputFromUser >= 80) and (inputFromUser <= 89):
    print("A megadott " + str(inputFromUser) + "% " + "értékelés jó!")
elif (inputFromUser >= 90) and (inputFromUser <= 100):
    print("A megadott " + str(inputFromUser) + "% " + "jeles!")
else:
    print("Hiba: érvénytelen százalék!")
