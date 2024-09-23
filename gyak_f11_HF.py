# A program kérjen be egy évszámot a felhasználótól! 
# Ha ez 1900 és 2099 közé esik, akkor a program írja ki, hogy az adott évben melyik napra esik húsvét vasárnap! 
# A kiszámítás algoritmusát megtalálja a Wikipedia-ban Gauss módszer néven.


inputFromUser = int(input("Adj meg egy évszámot: "))

if inputFromUser >= 1900 and inputFromUser <= 2099:
    a = inputFromUser % 19
    b = inputFromUser % 4
    c = inputFromUser % 7
    
    d = (19 * a + 24) % 30
    e = ((2 * b) + (4 * c) + (6 * d) + 5) % 7
    
    if (d + e) < 10:
        print(str(inputFromUser) + "-ban/ben a hústvét március " + str(d + e + 22) + "-ra/re esik.")
    else:
        if (d + e - 9) == 26:
            print(str(inputFromUser) + "-ban/ben a húsvét április 19-re esik.")
        elif (d + e - 9) == 25 and d == 28 and e == 6 and a < 10:
            print(str(inputFromUser) + "-ban/ben a húsvét április 18-ra esik.")
        else:
            print(str(inputFromUser) + "-ban/ben a hústvét április " + str(d + e - 9) + "-ra/re esik.")
else:
    print("Hibás évszám!")