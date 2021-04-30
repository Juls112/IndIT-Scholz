# Schleifen- /Zählvariable: i, j, k
# Addieren Sie in einer Schleife(!) die Zahlen von 1 bis 100 und geben sie das Ergebnis aus

counter = 10
while counter >= 0:
    print(counter)
    counter = counter - 1 #alt.: counter -= 1
    
Summe = 0
counter = 0
while counter < 100:
    counter += 1
    print(counter)
    summe += counter
print("Summe", Summe)

