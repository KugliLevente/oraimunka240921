# A program két beolvasott számot összehasonlítva írja közéjük a megfelelő relációs jelet (<, >, =)!

first_inputFromUser = float(input("Add meg az első számot: "))
second_inputFromUser = float(input("Add meg a második számot: "))

if first_inputFromUser > second_inputFromUser:
    print(str(first_inputFromUser) + " > " + str(second_inputFromUser))
elif first_inputFromUser < second_inputFromUser:
    print(str(first_inputFromUser) + " < " + str(second_inputFromUser))
else:
    print(str(first_inputFromUser) + " = " + str(second_inputFromUser))
    
    