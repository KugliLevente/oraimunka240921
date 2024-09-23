# A program olvasson be a konzolról egy egész számot! 
# A program döntse el, hogy a megadott számpáros vagy páratlan, és írja ki az eredményt a konzolra!

inputFromUser = int(input("Adj meg egy egész számot: "))

if inputFromUser % 2 is 0:
    print("Páros!")
else:
    print("Páratlan!")