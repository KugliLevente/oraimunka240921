inputFromUser = int(input("Add meg az osztályzatot: "))

if inputFromUser == 1:
    print("Elégtelen!")
elif inputFromUser == 2:
    print("Elégséges!")
elif inputFromUser == 3:
    print("Közepes!")
elif inputFromUser == 4:
    print("Jó!")
elif inputFromUser == 5:
    print("Jeles!")
else:
    print("Érvénytelen osztályzat!")