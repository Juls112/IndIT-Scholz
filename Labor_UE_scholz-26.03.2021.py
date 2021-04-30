# AUFGABE 1

# Schreiben Sie ein Python-Programm, dass
# 1) den Benutzer berüßt
# 2) eine erste Zahl entgegen nimmt
# 3) eine zweite Zahl entgegen nimmt
# 4) die Summe der beiden Zahlen berechnet und ausgibt
# 5) die Diffenenz der kleineren von der größeren Zahl berechnen
# 6) das Produkt der beiden Zahlen berechnet und ausgibt
# 7) den Quotient der kleineren Zahl durch die größere Zahl berechnet und ausgibt (inkl. Nachkommastellen)

Name = input("Bitte Geben sie ihren Namen ein")
print ("Hallo und herzlich willkommen", Name)

Zahl_1 = input ("Eingabe der Zahl_1:")
Zahl_1 = float (Zahl_1)
print ("Die Eingabe lautet:" , Zahl_1)
Zahl_2 = float (input ("Eingabe der Zahl_2:"))
Zahl_2 = float (Zahl_2)
print ("Die Eingabe lautet:" , Zahl_2)

Summe = Zahl_1 + Zahl_2
print("Summe", Summe)


if Zahl_1 > Zahl_2:
    Differenz = Zahl_1 - Zahl_2
    print("Differenz", Differenz)
    
elif Zahl_1 < Zahl_2:
    Differenz = Zahl_2 - Zahl_1
    print("Differenz", Differenz)

else:
    Differenz = Zahl_1 - Zahl_2
    print("Differenz", Differenz)
    
Produkt = Zahl_1 * Zahl_2
print("Produkt", Produkt)

if Zahl_1 > Zahl_2:
    Quotient = Zahl_2 / Zahl_1
    print("Quotient", Quotient)
    
elif Zahl_1 < Zahl_2:
    Quotient = Zahl_1 / Zahl_2
    print("Quotient", Quotient)
    
else:
    Quotient = Zahl_1 / Zahl_2
    print("Quotient", Quotient)
    
    
    


    