import math

inputFromUser = float(input("Adj meg egy valós számot: "))
result = math.fabs(inputFromUser)
print("|" + str(inputFromUser) + "| = " + str(result))