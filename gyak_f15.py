# A program olvasson be a konzolról két valós számot! 
# Ha mindkét szám pozitív, akkor legyenek a beolvasott számok egy téglalap oldalai. 
# A program számítsa ki a téglalap kerületét, területét, és írja ki két tizedesre kerekítve az eredményeket a konzolra! 
# Hiba esetén írja ki: "Hiba: a téglalap oldalai nem pozitívak!"!

first_inputFromUser = float(input("Add meg a téglalap egyik oldalának hosszát:"))
second_inputFromUser = float(input("Add meg a téglalap másik oldalának hosszát:"))

if first_inputFromUser > 0 and second_inputFromUser > 0:
    circumference = (2 * first_inputFromUser) + (2 * second_inputFromUser)
    area = first_inputFromUser * second_inputFromUser
    print("A téglalap kerülete: " + str(round(circumference, 2)))
    print("A téglalap területe: " + str(round(area, 2)))
else:
    print("Hiba: a téglalap oldalai nem pozitívak!")