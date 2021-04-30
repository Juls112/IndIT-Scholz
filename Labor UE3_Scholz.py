""" Pi näherungsweise berechnen durch Leibniz-Reihe """

N = input ("Eingabe n (Anzahl der Brüche):")
n = float (N)
Wert = input ("Eingabe des gewünschten Wertes:")
wert = float (Wert)
k = (0)
ergebnis = (0)

while k < n:
    ergebnis = ergebnis + (4*((-1)**k)/(2*k+1))
    k = k + 1
    if wert == k:
        print ("Zwischenergebnis:", k, "=", ergebnis)
    print ("Anzahl der berechneten Brüche:", k, "=", ergebnis)
                           