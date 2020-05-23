"""weź dowolną nieujemną i niezerową liczbę całkowitą i nadaj jej nazwę c0;
    jeżeli jest parzysta oblicz nową wartość dla c0 równą c0 ÷ 2;
    w przeciwnym razie, jeżeli liczba jest nieparzysta, oblicz nową wartość dla c0 równą 3 × c0 + 1;
    jeżeli c0 ≠ 1, przeskocz do punktu 2.

Hipoteza mówi, że niezależnie od początkowej wartości c0, wynik zawsze dąży do wartości 1.

Oczywiście niezwykle skomplikowanym zadaniem jest użycie komputera w celu udowodnienia tej hipotezy dla dowolnej liczby naturalnej (może to wymagać nawet pomocy sztucznej inteligencji), ale możesz użyć Pythona do sprawdzenia poszczególnych liczb. Może znajdziesz nawet taką liczbę, która obaliłaby powyższą hipotezę!

Napisz program, który czyta jedną liczbę naturalną i wykonuje powyższe kroki tak długo jak c0 pozostaje inny niż 1. Chcemy również, abyś policzył kroki potrzebne do osiągnięcia celu. Twój kod powinien wypisać wszystkie pośrednie wartości c0.

Podpowiedź: najważniejszą częścią problemu jest przekształcenie pomysłu Collatza w pętlę while - to jest klucz do sukcesu."""


c0 = int(input("wpisz swoja liczbe: "))

#c0 = nieujemna, niezerowa liczba calkowita
kolejny_krok = 0


while  c0 != 1:
    print("aktualnie c0 wynosi: ", c0)
    kolejny_krok = kolejny_krok + 1    
    
    if c0 %2 == 0:
        c0 = c0 / 2
    else:
        c0 = 3 * c0 + 1 
        
        
        
print("liczba krokow wyniosla: ", kolejny_krok)
print("na koniec c0 wynosi: ", c0)
    
    
