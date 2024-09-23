months = ['Január', 'Február', 'Március', 'Április', 
          'Május', 'Júnis', 'Július', 'Augusztus',
          'Szeptember', 'Október', 'November', 'December']

inputFromUser = int(input("Adj meg egy egész számot: "))

if inputFromUser > 0 and inputFromUser < 13:
    print(months[inputFromUser - 1])
else:
    print("Hibás bemenet!")