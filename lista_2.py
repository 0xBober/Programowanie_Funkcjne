import random
import math

def zadanie_1():
    print("""\nZadanie 1 \nPewien sklep prowadzi sprzedaż i wprowadził promocję. Klient dostaje 10%
zniżki na zakupy o wartości 100 zł lub niższej i 20% zniżki na zakupy większe niż 100
zł. Napisz program, który poprosi o cenę zakupów i wyświetli uzyskany rabat oraz
ostateczną cenę za zakupy.""")
    print("################################################################################")
    cena = float(input("Prosze podać cenę: "))
    if(cena <= 100):
        print(f"Uzyskujesz rabat 10%, ostateczna cena towaru wynosi: {cena * 0.9}")
    else:
        print(f"Uzyskujesz rabat 20%, ostateczna cena towaru wynosi: {cena * 0.8}")
    return 0

def zadanie_2():
    print("""\nZadanie 2 \nNapisz prosty program symulujący procedurę logowania do komputera.
Wykorzystaj konstrukcje˛ rozgałęziającą if ... else. Oto przykładowe sesje z programem:
\nWitaj w systemie logowania komputera!
Podaj hasło dostępu: programowanie
Logowanie zakończyło się sukcesem!
—————————
Witaj w systemie logowania komputera!
Podaj hasło dostępu: hasło
Błędne hasło! Odmowa dostępu!""")
    print("################################################################################")
    print("Witaj w systemie logowania komputera!")
    password = input("Podaj hasło dostepu: ")
    if password == "programowanie":
        print("Logowanie zakończyło si˛e sukcesem!")
    else:
        print("Błędne hasło! Odmowa dostępu!")
    return 0

def zadanie_3():
    print("""\nZadanie 3 \nDrużyna piłkarska szuka dziewczyn w wieku od 10 do 12 lat, aby grać w drużynie.
Napisz program, który pyta o wiek użytkownika oraz o to czy jest to mężczyzna
czy kobieta (używając "M" lub "K"). Program powinien wyświetlać komunikat
wskazujący, czy dana osoba może grać w zespole. Program powinien pytać o wiek tylko
w przypadku gdy użytkownik jest dziewczyną.""")
    print("################################################################################")
    plec = input("Proszę podać swoją płeć (M-mężczyzna lub K-Kobieta?): ")
    if(plec == 'K' or plec == 'k'):
        wiek = int(input("Prosze podać swój wiek: "))
        if(10 <= wiek <= 12):
            print("Nadajesz się do drużyny!")
        else:
            print("Niestety nie nadajesz się do drużyny! ):")
    else:
        print("Niesetety poszukujemy tylko kobiety, więc nie nadajesz się do drużyny! ):")

    return 0

def zadanie_4():
    print("""\nZadanie 4 \nRok jest przestępny, jeżeli jest podzielny przez 4. Od tej reguły jest jednak
wyjątek. Jeżeli jest on jednocześnie podzielny przez 100 to nie jest przestępny – chyba,
że jest podzielny przez 400. Napisz program, który sprawdza czy podany przez użytkownika
rok jest rokiem przestępnym.""")
    print("################################################################################")
    rok = int(input("Prosze podać rok do sprawdzenia: "))
    if((rok % 4 == 0 and rok % 100 != 0)or rok % 400 == 0):
        print(f"{rok} jest przystępny")
    else:
        print(f"{rok} nie jest przystępny")
    return 0

def zadanie_5():
    print("""Zadanie 5 Poniżej znajduje się uproszczona wersja skali Beauforta, służąca do szacowania
siły wiatru.
Napisz program, który będzie wymagał od użytkownika wprowadzenia siły wiatru w
węzłach, a następnie wyświetli odpowiadającą jej wartość skali opisowej.

Preśdkość wiatru (węzły) | Opis
        poniżej 1        | Cisza
        1-3              | Zefir
        4-27             | Bryza
        28-47            | Wichura
        48-63            | Sztorm
        powyżej 63       | Huragan
""")
    print("################################################################################")
    speed = float(input("Proszę podać wartość prędkośći w węzłach: "))
    if(speed<1):
        print("Cisza")
    elif(1<=speed<=3):
        print("Zefir")
    elif(4<=speed<=27):
        print("Bryza")
    elif(28<=speed<=47):
        print("Wichura")
    elif(48<=speed<=63):
        print("Sztorm")
    else:
        print("Huragan")
    return 0

def zadanie_6():
    print("""\nZadanie 6 \nZa pomocą instrukcji if...elif...else zamień ocenę wyrażoną w punktach
na ocenę w stopniach. Przyjmij następująca skalę ocen: A = 90 − 100 punktów,
B = 80 − 89 punktów, C = 70 − 79 punktów, D = 60 − 69 punktów, E = 0 − 59 punktów.
Jeżeli liczba punktów jest większa niż 100 lub mniejsza od zera, program powinien
wypisać komunikat o błędzie.""")
    print("################################################################################")
    ocena = int(input("Prosze podać % uzyskany: "))
    if(0<=ocena<=59):
        print(f"Wynik {ocena}% to ocena stopnia E")
    elif(60<=ocena<=69):
        print(f"Wynik {ocena}% to ocena stopnia D")
    elif(70<=ocena<=79):
        print(f"Wynik {ocena}% to ocena stopnia C")
    elif(80<=ocena<=89):
        print(f"Wynik {ocena}% to ocena stopnia B")
    elif(90<=ocena<=100):
        print(f"Wynik {ocena}% to ocena stopnia A")
    else:
        print("Wystąpił błąd, ocena jest mniejsza od 0% lub więkdza od 100%")

    return 0

def zadanie_7():
    print("""\nZadanie 7 \nNapisz program, który wyświetli następujący wzór:
*
**
***
****
*****
Wykorzystaj pętlę while i operator * w kontekście ciągów tekstowych (replikacja).""")
    print("################################################################################")
    max_base = int(input("Prosze podać wartość długośći podstawy tego wzoru: "))
    x = 1
    while(x <= max_base):
        print('*'* x)
        x += 1
    return 0

def zadanie_8():
    print("""\nZadanie 8 \nNapisz program, który pobierze od użytkownika liczbę nieujemną n,
a następnie obliczy i wyświetli wartość sumy liczby od 1 do n.Wykorzystaj pętlę while.""")
    print("################################################################################")
    x = 0
    sum_total = 0
    n = int(input("Proszę podać wartość nie ujemnną dla wartości n: "))
    while(x <= n):
        sum_total += x
        x += 1
    print(f"Suma liczb w przedziala (0,n) wynosi: {sum_total}")
    return 0

def zadanie_9():
    print("""\nZadanie 9 \nNapisz program który prosi o podanie liczby całkowitej n (n > 0) i oblicza
sumę kwadratów pierwszych n liczb całkowitych. Wykorzystaj dwukrotnie pętle while
– po raz pierwszy aby „wymusić” na użytkowniku podanie liczby dodatniej, po raz
drugi aby wyznaczyć szukaną sume""")
    print("################################################################################")
    x = 1
    sum_total = 0

    while(True):
        n = int(input("Proszę podać wartość nie ujemnną dla wartości n: "))
        if(n>0):
            break

    while(x <= n):
        sum_total += x**2
        x += 1
    print(f"Suma kwadratów pierwszych {n} liczb całkowitych wynosi: {sum_total}")

    return 0

def zadanie_10():
    print("""\nZadanie 10 \nZmodyfikuj program z zadania 2 tak aby użytkownik był proszony o podanie
hasła aż do skutku. Wykorzystaj nieskończoną pętlę while przerywaną instrukcją break.""")
    print("################################################################################")
    print("Witaj w systemie logowania komputera!")
    while(True):
        password = input("Podaj hasło dostepu: ")
        if password == "programowanie":
            print("Logowanie zakończyło si˛e sukcesem!")
            break
        else:
            print("Błędne hasło! Odmowa dostępu!")
            continue

    return 0

def zadanie_11():
    print(("""\nZadanie 11 \nNapisz program, który pobiera dwie liczby n (n > 2) i k (k < n). Program
powinien wyświetlić wszystkie liczby od 1 do n z pominięciem liczb podzielnych przez
k. Wykorzystaj instrukcję continue."""))
    print("################################################################################")
    while(True):
        n = int(input("Podaj wartość n (n>2): "))
        k = int(input("Podaj wartość k (k<n): "))
        if(k<n):
            break
        else:
            print("BŁĄD. k musi być mniejszy od n. Spróbój ponownie")
            continue
    x = 1
    table = []
    while(x <= n):
        if(x % k != 0):
            x += 1
            continue
        else:
            table.append(x)
            x += 1
    print(table)
    return 0

def zadanie_12():
    print("""\nZadanie 12 \nNapisz program, który sprawdzi czy podana przez użytkownika liczba jest
pierwsza. Program powinien sprawdzać kolejne liczby (większe od 1) dopóki użytkownik je podaje.""")
    print("################################################################################")
    def is_prim(x):
        for i in range(2,round(x/2)):
            if(x % i == 0):
                return(False)
            else:
                continue
        return True

    while(True):
        UserInput = input("Proszę podać wartość do srpawdzenia lub wciśnij Enter aby zakonczenia: ")
        if(UserInput != ''):
            if(int(UserInput) <= 1):
                continue
            else:
                print(is_prim(int(UserInput)))
        else:
            break

    return 0

def zadanie_13():
    print("""\nZadanie 13 \nNapisz gre˛ „Zgadnij jaką liczbę mam na myśli”, która polega na tym, iż
komputer losuje liczbę z zakresu 1 − 100 a użytkownik musi odgadnąć jaka to liczba.
Program powinien podpowiadać użytkownikowi czy podana liczba jest mniejsza czy
też większa od liczby którą wylosował komputer. Program powinien zliczać ilość prób
potrzebną do odgadnięcia liczby przez użytkownika.""")
    print("################################################################################")
    proby = 1
    zgadnij_liczbe = random.randint(1,100)
    while(True):
        UserInput = int(input("Zgadnij wylosowaną liczbę: "))
        if(UserInput == zgadnij_liczbe):
            print(f"Trafiłeś w liczbę! Zajęło ci to tylko {proby} prób")
            break
        elif(UserInput < zgadnij_liczbe):
            print(("Nie trafiłeś. Liczba jest większa."))
            proby += 1
            continue
        elif(UserInput > zgadnij_liczbe):
            print("Nie trafiłeś. Liczba jest mniejsza.")
            proby += 1
            continue
    return 0

def zadanie_14():
    print("""\nZadanie 14 \nNapisz modyfikację gry „Zgadnij jaką liczbę mam na myśli”. Tym razem
to użytkownik ma pomyśleć liczbę z zakresu od 1 do 100 a komputer podjąć próbę
jej odgadnięcia. Program powinien pozwolić podpowiadać komputerowi czy podana
liczba jest mniejsza czy też większa od liczby którą wybrał użytkownik. Przyjmij, że
użytkownik nie oszukuje.""")
    print("################################################################################")
    proby = 1
    zgadnij_liczbe = int(input("Podaj liczbę w przedziale (1,100)"))
    CompInput = random.randint(1,100)
    min_num = 1
    max_num =100
    while(True):
        if(CompInput == zgadnij_liczbe):
            print(f"Trafiłeś w liczbę {zgadnij_liczbe}! Zajęło ci to tylko {proby} prób")
            break
        elif(CompInput < zgadnij_liczbe):
            print((f"Nie trafiłeś. Liczba jest większa od {CompInput}."))
            min_num = CompInput + 1
            CompInput = random.randint(CompInput+1,max_num)
            proby += 1
            continue
        elif(CompInput > zgadnij_liczbe):
            print(f"Nie trafiłeś. Liczba jest mniejsza {CompInput}.")
            max_num = CompInput - 1
            CompInput = random.randint(min_num, CompInput-1)
            proby += 1
            continue
    return 0

def zadanie_15():
    print("""\nZadanie 15 \nNapisz program, który będzie wyświetlał następujący wzór:
       *
      ***
     *****
    *******
   *********
  ***********
 *************
***************
Wykorzystaj pętle zagnieżdżone for i nie używaj replikacji ciągów tekstowych. Liczba
wierszy powinna być określona przez użytkownika.""")
    print("################################################################################")
    base = int(input("Proszę podać wyskość trójkąta: "))
    stars = '*'

    for i in range(0,base):
        spaces = ''
        for j in range(i,base-1):
            spaces += ' '
        print(spaces + stars)
        stars += '**'
    return 0

def zadanie_16():
    print("""\nZadanie 16 \nJaka jest różnica pomiędzy wywołaniami funkcji range(10), range(0, 10)
i range(0,10,1).""")
    print("################################################################################")
    print("funkca range(10)")
    for i in range(10):
        print(f"Hello World nr {i}!")

    print("################################################################################")
    print("funkca range(0,10)")
    for j in range(0,10):
        print(f"Hello World nr {j}!")

    print("################################################################################")
    print("funkca range(0,10,1)")
    for k in range(0,10,1):
        print(f"Hello World nr {k}!")

    print("""Różnica pomiędzy wywołaniami funkcji range(10), range(0, 10) i range(0, 10, 1) dotyczy sposobu, w jaki podawane są argumenty, ale efekty działania tych trzech wywołań są takie same.

    range(10):
        To wywołanie przyjmuje tylko jeden argument, który określa górną granicę przedziału (ale nie włączając tej wartości). Zakłada się, że start wynosi 0, a krok wynosi 1.
        Oznacza to, że generuje liczby od 0 do 9.
        Wynik: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

    range(0, 10):
        Tutaj podajesz dwa argumenty: początkową wartość (0) i górną granicę (10). Górna granica, podobnie jak wcześniej, nie jest włączona.
        Domyślny krok wynosi 1.
        Wynik również to liczby od 0 do 9.
        Wynik: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

    range(0, 10, 1):
        W tym wywołaniu podajesz trzy argumenty: początkową wartość (0), górną granicę (10) i krok (1).
        Efekt jest taki sam jak w poprzednich przypadkach, ponieważ krok wynosi 1.
        Wynik: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

Podsumowanie:

Wszystkie trzy wywołania generują dokładnie taki sam ciąg liczb: od 0 do 9. Różnica polega jedynie na ilości i sposobie podawania argumentów.""")

    return 0

def zadanie_17():
    print("""\nZadanie 17 \nNapisz program, który symuluje 100 – krotny rzut monetą, a następnie podaje
użytkownikowi liczbę orłów i reszek.""")
    print("################################################################################")

    orzel = 0
    reszka = 0
    for i in range(0,100):
        coin_flip = random.randint(1,100)
        if(coin_flip%2==0):
            orzel += 1
        else:
            reszka += 1

    print(f"Orzeł: {orzel}")
    print(f"Reszka: {reszka}")
    return 0

def zadanie_18():
    print(("""\nZadanie 18 \nNapisz program, który symuluje 1000 – krotny rzut sześcienną kostką,
a następnie podaje użytkownikowi ile razy wypadła dana ścianka kostki."""))
    print("################################################################################")

    oczko_1 = 0
    oczko_2 = 0
    oczko_3 = 0
    oczko_4 = 0
    oczko_5 = 0
    oczko_6 = 0

    for i in range(0,1000):
        dice_roll = random.randint(1,6)
        if (dice_roll == 1):
            oczko_1 += 1
            continue
        elif(dice_roll == 2):
            oczko_2 += 1
            continue
        elif (dice_roll == 3):
            oczko_3 += 1
            continue
        elif (dice_roll == 4):
            oczko_4 += 1
            continue
        elif (dice_roll == 5):
            oczko_5 += 1
            continue
        elif (dice_roll == 6):
            oczko_6 += 1
            continue

    print(f"""
1 OCZKO: {oczko_1}
2 OCZKA: {oczko_2}
3 OCZKA: {oczko_3}
4 OCZKA: {oczko_4}
5 OCZKA: {oczko_5}
6 OCZKA: {oczko_6}
""")
    return 0

def zadanie_19():
    print("""\nZadanie 19 \nNapisz program, który wyświetla miesięczny kalendarz. Użytkownik powinien
podać liczbę dni w miesiącu i dzień tygodnia, od którego zaczyna się miesiąc.
Przykładowe wykonanie programu:

Podaj liczbę dni w miesiącu: 31
Podaj początkowy dzień miesiąca (1-Nie, 7-Sob): 4
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
""")
    print("################################################################################")

    days_in_month = int(input("Podaj liczbę dni w miesiącu: "))
    starting_day_of_month = int(input("Podaj początkowy dzień miesiąca: "))
    table = []

    for i in range(1,starting_day_of_month): #dodawanie puste dni
        table.append('  ')

    for j in range(1,days_in_month+1):  #dodawanie dni do tabeli
        if(j < 10):
            table.append(' ' + str(j))
        else:
            table.append(str(j))

    for k in range(0,42-len(table)):    #uzupełnienie tabeli pustymi dniami
        table.append('  ')

    a = 0
    b = 7
    while(True):
        print(*table[a:b])
        if(b==42):
            break
        a += 7
        b += 7

    return 0

def zadanie_20():
    print("""\nZadanie 20 \nNapisz program, który oblicza sumę 1, 2, 3, 4 itd. (aż do pewnej granicy)
wyrazów następujących ciągów:
+1.0/2.0 + 1.0/3.0 + 1.0/4.0 + ...
-1.0/2.0 + 1.0/3.0 - 1.0/4.0 + ...
Maksymalna liczba wyrazów sumowania powinna być określana przez użytkownika.
Przyjrzyj się sumom dla 10, 100 i 1000 wyrazów. Czy coś zauważyłeś?
Wskazówka: −1 pomnożone przez siebie nieparzysta˛ ilość razy jest równe −1, natomiast
parzysta˛ ilość razy +1.""")
    print("################################################################################")

    finalValue = int(input("Prosze podać maksymalną liczbę wyrazów: "))
    suma_1 = 0
    suma_2 = 0

    for i in range(2,finalValue+1):
        suma_1 += 1/i

    for j in range(2,finalValue+1):
        if(j % 2 == 0):
            suma_2 -= 1/i
        else:
            suma_2 += 1/i

    print(f"Suma Pierwszego Ciągu wynosi: {suma_1}\nSuma Drugiego Ciągu wynosi: {suma_2}")
    print("################################################################################")
    print("""Można zauważyć, że suma ciąków przy maksymalnej wartości 10^n, że suma jest równa -1/10^n""")
    return 0

def zadanie_21():
    print("""\nZadanie 21 \nKorzystając z pętli while i for (tj. na dwa sposoby) wykonaj nastepujące
zadania:
a) wypisz n kolejnych liczb naturalnych począwszy od 1 (dla n > 1 podanego przez użytkownika);
b) wypisz kolejne liczby naturalne od n do 1 (dla n > 1 podanego przez użytkownika);
c) wypisz wszystkie liczby naturalne parzyste i mniejsze od n (dla n > 1 podanego przez użytkownika);
d) wypisz n kolejnych liczb nieparzystych pocza˛wszy od n (dla n > 1 podanego przez użytkownika);
e) wypisz n kolejnych wyrazów ciągu arytmetycznego: 1, 4, 7, 10, 13, . . . (dla n > 1 podanego przez użytkownika);
f) wypisz 12 kolejnych silni liczb naturalnych tj. 12 początkowych wyrazów ciągu:1, 1 · 2 , 1 · 2 · 3, 1 · 2 · 3 · 4, . . . ;
g) wypisz n kolejnych wyrazów ciągu: a_n = 1/n (dla n > 1 podanego przez użytkownika);
h) wypisz 17 kolejnych wyrazów ciągu zdefiniowanego rekurencyjnie: a_1 = 3, a_n = 6 · a_n−1 − 13/2 ;
i) wypisz 31 kolejnych wyrazów ciągu danego rekurencyjnie (pierwszym wyrazem jest a_0): a_0 = 0, a_n = 2 · a_n−1 + 1 (dla n > 1)^2;
j) wypisz sumę n kolejnych kwadratówliczb naturalnych tj. sumeę 1^2+2^2+3^2+· · ·+n^2 (dla n > 1 podanego przez użytkownika).
k) wypisz wartość sumy 2+4+6+· · ·+2n (dla n > 1 podanego przez użytkownika);
l) wypisz wartość sumy 1 + 3 + 5 + · · · + (2n + 1) (dla n > 1 podanego przez użytkownika);
m) wypisz ile jest liczb parzystych i nieparzystych w podanym przez użytkownika ciągu n liczb naturalnych(dla n > 1 podanego przez użytkownika);
n) wypisz ile jest liczb ujemnych i dodatnich w podanym przez użytkownika ciągu n liczb całkowitych (dla n > 1 podanego przez użytkownika);
o) wypisz ile jest liczb podzielnych przez 3 w podanym przez użytkownika ciągu n liczb całkowitych (dla n > 1 podanego przez użytkownika);
p) wypisz ile jest liczb podzielnych przez 5 w podanym przez użytkownika ciągu n liczb całkowitych (dla n > 1 podanego przez użytkownika);
q) wypisz wartość sumy (1/1)+(1/2)+(1/3)+...+(1/n) (dla n >1 podanego przez użytkownika);
r) wypisz wartość sumy (1/1^2)+(1/2^2)+(1/3^2)+...+(1/n^2) (dla n > 1 podanego przez użytkownika).
""")
    #delikatnie będę leniwy i będę na zmianę używać while i for loopy :)

    print("================ZADANIE A================")
    n = int(input("Proszę podać wartość n > 0: "))
    line = ''
    i = 1
    while(i<=n):
        line += str(i)+ ' '
        i +=1
    print(line)

    print("================ZADANIE B================")
    line = ''
    j = n
    for i in range(0,n):
        line += str(j) + ' '
    j-=1
    print(line)

    print("================ZADANIE C================")
    line = ''
    i = 1
    while(i < n):
        if(i%2==0):
            line += str(i) + ' '
        i += 1
    print(line)

    print("================ZADANIE D================")
    line = ''
    for i in range (1,n+1):
        if(i % 2 == 1):
            line += str(i) + ' '
    print(line)

    print("================ZADANIE E================")
    line = ''
    i = 1
    while(i<=n):
        line += str(i) + ' '
        i += 3
    print(line)

    print("================ZADANIE F================")
    line = ''
    total = 1
    for i in range(1,13):
        for j in range(1,i+1):
            total *= j
        line += str(total) + ' '
        total = 1

    print(line)

    print("================ZADANIE G================")
    line = ''
    i = 1
    while(i<=n):
        line += str(1/i) + ' '
        i += 1
    print(line)

    print("===LUB===")

    line = ''
    i = 1
    while (i <= n):
        line += f'1/{i} '
        i += 1
    print(line)

    print("================ZADANIE H================")
    line = 'a_1 = 3 '
    x = 3
    for i in range(2,18):
        x = 6 * x - (13/2)
        line += f'| a_{i} = {x} '

    print(line)

    print("================ZADANIE I================")
    line = 'a_0=0 '
    x = 0
    i = 1
    while(i<32):
        x = 2 * x + 1
        line += f'| a_{i} = {x} '
        i += 1

    print(line)

    print("================ZADANIE J================")
    suma = 0
    for i in range(1,n+1):
        suma += pow(i,2)

    print(suma)

    print("================ZADANIE K================")
    suma = 0
    i = 1
    while(i <= n):
        suma += i*2
        i += 1

    print(suma)

    print("================ZADANIE L================")
    suma = 0
    i = 1
    while (i <= n):
        suma += (i * 2)+1
        i += 1

    print(suma)

    print("================ZADANIE M================")
    liczby_parzyste = 0
    liczby_nieparzyste = 0
    i = 1
    while(i<=n):
        if(i%2 ==0):
            liczby_parzyste += 1
        else:
            liczby_nieparzyste += 1
        i += 1

    print(f"Liczby Parzyste: {liczby_parzyste}\nLiczby Nieparzyste: {liczby_nieparzyste}")

    print("================ZADANIE N================")
    #aby to zrobić urzytkownik musiałby podać włąsny ciąg liczb zatem muszę dodatkowo pobrać jakić ciąg liczb albo wygeneruje se ich losowo dla przykładu :)
    lista_liczb = []
    for i in range (10):
        lista_liczb.append(random.randint(-100,100))

    liczba_dodatnia = 0
    liczba_ujemna = 0
    for i in lista_liczb:
        if(i < 0):
            liczba_ujemna += 1
        elif(i>0):
            liczba_dodatnia += 1
        else:
            continue

    print(f"Ciąg(powiedzmy){lista_liczb}\nIlość liczb dodatnich:{liczba_dodatnia}\nIlość liczb ujemnych: {liczba_ujemna}")

    print("================ZADANIE O================")
    i = 1
    total = 0
    while(i <=n):
        if(i%3 == 0):
            total += 1
        i+=1

    print(total)

    print("================ZADANIE P================")
    total = 0
    for i in range(1,n+1):
        if (i % 3 == 0):
            total += 1

    print(total)

    print("================ZADANIE Q================")
    i = 1
    total = 0
    while(i<=n):
        total += (1/i)
        i += 1

    print(total)

    print("================ZADANIE R================")
    total = 0
    for i in range(1,n+1):
        total += 1/(pow(i,2))

    print(total)

    return 0

def zadanie_22():
    print("""\nZadanie 22 \nProfesor Popularny dołączył do serwisu społecznościowego. Początkowo
miał pięciu znajomych. Zauważył, że liczba znajomych zmienia się zgodnie
z następującą regułą: pierwszego dnia odpadł jeden znajomy, a liczba pozostałych znajomych
podwoiła się.W drugim tygodniu odeszło dwóch znajomych, a pozostali znów
podwoili swoją liczbę. Ogólnie w n-tym tygodniu odpadło n przyjaciół, pozostali "mnożyli
się" dwukrotnie. Napisz program, który obliczy i wypisze liczbę znajomych profesora
po kolejnych tygodniach. Program powinien przeliczać kolejne tygodnie dopóty,
dopóki liczba znajomych nie przekracza tzw. liczby Dunbara. Liczba Dunbara to szacunkowa liczba maksymalnej liczności spójnej grupy społecznej, w której każdy ze
znajomych zna wszystkich innych znajomych i zna relacje pomiędzy pozostałymi znajomymi
(w przybliżeniu jest to 150 osób).
6""")

    print("################################################################################")

    ilosc_znajomych = 5
    max_ilosc_znajomych = 150
    tydzien = 1
    while(ilosc_znajomych < 150):
        print(f"{tydzien} Tydzień ilość znajomych wynosiło {ilosc_znajomych}")
        ilosc_znajomych = (ilosc_znajomych-tydzien)*2
        tydzien += 1
    return 0

def execute_task(task_number):
    match task_number:
        case '1':
            zadanie_1()
        case '2':
            zadanie_2()
        case '3':
            zadanie_3()
        case '4':
            zadanie_4()
        case '5':
            zadanie_5()
        case '6':
            zadanie_6()
        case '7':
            zadanie_7()
        case '8':
            zadanie_8()
        case '9':
            zadanie_9()
        case '10':
            zadanie_10()
        case '11':
            zadanie_11()
        case '12':
            zadanie_12()
        case '13':
            zadanie_13()
        case '14':
            zadanie_14()
        case '15':
            zadanie_15()
        case '16':
            zadanie_16()
        case '17':
            zadanie_17()
        case '18':
            zadanie_18()
        case '19':
            zadanie_19()
        case '20':
            zadanie_20()
        case '21':
            zadanie_21()
        case '22':
            zadanie_22()
        case _:
            print("Task not found.")
    return 0

def main():

    UserInput = ' '

    while(UserInput != 'x'):
        UserInput = str(input("Podaj numer Zadania lub napisz 'x' aby zakończyć program: "))
        execute_task(UserInput)

    return 0

main()
