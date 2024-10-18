import math #przyda się do zadań matematycznych :)

def zadanie_1():
    print("Zadanie 1\nW powłoce interaktywnej (w konsoli) wpisz następujące wyrażenia wciskając klawisz Enter po każdym z nich:")
    print("a) 1 + 2 + 3 + 4 + 5")
    print("b) 7 * 12")
    print("c) 2 + 4 * 2")
    print("d) (2 + 4) * 2")
    return 0

def zadanie_2():
    print("\nZadanie 2\nPrzetestuj działanie operatorów jednoargumentowych + i - obliczając wartości poniższych wyrażeń w powłoce interaktywnej:")
    print("a) 4 + +3")
    print("b) 4 + -3")
    print("c) 4 - -3")
    print("d) -2 ** 4")
    return 0

def zadanie_3():
    print("\nZadanie 3\nW powłoce interaktywnej przeanalizuj na kilku przykładach wyrażenie b * (a // b) + a % b, wykorzystuja˛c w miejscu a oraz b dowolne liczby. Czy coś zauważyłeś?")
    a = 2
    b = 3
    wynik = b * (a // b) + a % b
    print("b * (a // b) + a % b = " + str(wynik))
    return(0)

def zadanie_4():
    print("\nZadanie 4 \nW powłoce interaktywnej oblicz wartość temperatury 212°F w skali Celsjusza. Wykorzystaj zależność:")
    temperatura_F = 212
    temperatura_C = (temperatura_F - 32)*5/9
    print(f"Temperatura 212°F jest równa {str(temperatura_C)}°C")
    return (0)

def zadanie_5():
    print("\nZadanie 5 \nWykorzystując funkcję wbudowana˛ typedef() sprawdź w kosoli interaktywnej jakiego typu są obiekty:")
    print(f"a) 5 = {type(5)}")
    print(f"b) 13.67 = {type(13.67)}")
    print(f"c) True = {type(True)}")
    print(f"d) 'kot' = {type('kot')}")
    return (0)

def zadanie_6():
    print("\nZadanie 6\nWykorzystując funkcje str(), int(), float() oraz bool dokonaj konwersji poznanych typów obiektów. W szczególność")
    print(f"a) skonwertuj 5.6 na typ int = {int(5.6)}")
    print(f"b) skonwertuj 8 na typ float = {float(8)}")
    print(f"c) skonwertuj '-5.5' na typ float = {float(-5.5)}")
    print(f"d) skonwertuj '-5' na typ int = {int(-5)}")
    #print(f"e) skonwertuj 'a' na typ int = {int('a')}") to jest nie wykonalne dlatego jest komentarz :)
    print(f"f) skonwertuj '5' na typ bool = {bool(5)}")
    print(f"g) skonwertuj '-7.5' na typ bool = {bool(-7.5)}")
    print(f"h) skonwertuj 0 na typ bool = {bool(0)}")
    print(f"i) skonwertuj '' na typ bool = {bool('')}")
    print(f"j) skonwertuj 'kot' na typ bool = {bool('kot')}")
    print(f"k) skonwertuj dowolny typ liczbowy na typ str = {str(123.456)}")
    return (0)

def zadanie_7():
    print("\nZadanie 7 \nW powłoce interaktywnej spróbuj wykonać nastepujące działania:")
    print(f"a) 'kot' + 'pies' = {'kot'+'pies'}")
    #print(f"b) 'kot' + 5 = {'kot'+5}") nie można konkantynować string z intem
    print(f"c) 'kot' * 5 = {'kot'*5}")
    print(f"d) 5 * 'ala' = {5*'ala'}")
    #print(f"e) 'kot' * '2' = {'kot' * '2'}") #TypeError: can't multiply sequence by non-int of type 'str'
    #print(f"f) 'kot' * 2.5 = {'kot' * 2.5}") #TypeError: can't multiply sequence by non-int of type 'float'
    return (0)

def zadanie_8():
    print("\nZadanie 8 \nZałóżmy, że zmienna temp przechowuje temperature˛ w stopniach Celsjusza. Utwórz instrukcję przypisania, która zmieni wartość zmiennej temp na temperaturę w skali Fahrenheita, wykorzystując jej dotychczasową wartość. Po wykonaniu polecenia sprawdź typ zmiennej temp. Wykonaj zadanie w powłoce interaktywnej.")
    temp = 1000 #tymczasowo w stopni celciusza
    print(f"Aktualna wartość temp: {1000}°C")
    temp = (9/5 * temp) - 32
    print(f"Nowa wartość temp: {temp}°F")
    return 0

def zadanie_9():
    print("""\nZadanie 9 \nNapisz program, który wyświetli Twoje imię i nazwisko oraz napis "Programowanie funkcyjne 2024/2025".Na ekranie powinien pojawić się tekst w następującym formacie:
\nIMIĘ NAZWISKO\n"Programowanie funkcyjne 2024/2025"
    """)

def zadanie_10():
    print("\nZadanie 10 \nNapisz program, który przeliczy Twój wiek w latach na wiek w dniach. Nie uwzględniaj ułamków lat oraz lat przestępnych.")
    wiek = int(input("Podaj swój wiek w latach: "))
    wiek_w_dni = wiek * 365
    print(f"Twój wiek to {wiek} lat, czyli {wiek_w_dni} dni")
    return 0

def zadanie_11():
    print("\nZadanie 11 \nZmodyfikuj program z zadania 10 tak aby to użytkownik mógł podać z klawiatury potrzebną ilość lat. Program powinien działać następująco:")
    print("\nPodaj swój wiek w latach: 10")
    print("Twój wiek to 10 lat, czyli 3650 dni.")
    print("Wykorzystam funkcje z poprzedniego zadania bo to jest to samo :)")
    zadanie_10()
    return 0

def zadanie_12():
    print("\nZadanie 12 \nNapisz program, który dla podanych wartości długości podstawyi wysokości (opuszczonej na daną podstawę) trójkąta oblicza jego pole. Przykładowo na ekranie powinien pojawić się tekst w następującym formacie: \nPole trójkąta o podstawie a = 5 cm i wysokości h = 6 cm wynosi 15.0 cm2.")
    base = float(input("Podaj długość podstawy trójkąta: "))
    height = float(input("Podaj długość wysokości trójkąta: "))
    area = (base*height)/2
    print(f"Pole trójkąta o podstawie a = {base} cm i wysokości h = {height} cm wynosi {area} cm2.")
    return 0

def zadanie_13():
    print("\nZadanie 13 \nZmodyfikuj program z zadania 12 tak aby to użytkownik mógł podawać potrzebne dane. Program powinien działać następująco:")
    print("\nPodaj długość podstawy trójkąta: 5.5")
    print("Podaj długość wysokości trójkąta: 6")
    print("Pozwole sobie wykorzystać ponownie funkcję zadania 12 :)")
    zadanie_12()
    return()

def zadanie_14():
    print("\nZadanie 14 \nNapisz interaktywny program, który przelicza podany czas w sekundach na czas podany w godzinach, minutach i sekundach. Przykładowe działanie programu:")
    print("\nPodaj czas w sekundach: 3700")
    print("Podany czas wynosi: 3700 sekund czyli:")
    print("1h 1min i 40s")

    print("#############################################################################################")
    input_value = int(input("Podaj czas w sekundach: "))
    hours = input_value // 3600
    minutes = (input_value - (hours * 3600))//60
    seconds = (input_value - (hours * 3600)) - (minutes*60)
    print(f"Podany czas wynosi: {input_value} sekund czyli: {hours}h {minutes}min i {seconds}s")


def zadanie_15():
    print("\nZadanie 15 \nWykorzystując ciągi potrójnie cytowane wykonaj proste rysunki w w technologii ASCII-art i wyświetl je. Przykładowe działanie programu mogłoby wyglądać następująco:")
    print("""Moje ulubione zwierzę to:
    (\ /)
    ( ..)
    c(")(")
    
    Mieszkam w mieście:
    _ ______ _ _ __ ____ __
| |/ / _ \ / \ | |/ //_/\ \ / /
| ’ /| |_) | / _ \ | ’ // _ \ \ \ /\ / /
| . \| _ < / ___ \| . \ |_| |\ V V /
|_|\_\_| \_\/_/ \_\_|\_\___/ \_/\_/
    """)

def zadanie_16():
    print("\nZadanie 16 \nNapisz interaktywny program, który obliczy pole i obwód trapezu równoramiennego dla podanych długości podstaw i wysokości.")
    print("##############################################################################")
    print("Dla ładnego wyniku polecam spróbować wartości a:10 b:4 oraz h:4")
    base_a = float(input("Podaj podstawę a(większa): "))
    base_b = float(input("Podaj podstawę b(mniejsza): "))
    height = float(input("Podaj wysokość h: "))
    area = ((base_a  + base_b)*height)/2
    print(f"Pole równoramiennego trapezu o podstawie {base_a}cm i {base_b}cm oraz wysokości {height}cm wynosi {area}cm^2")
    dlugosc_ramiona = math.sqrt(((base_a - base_b)/2)**2 + height**2)
    print(f"Długość ramiona wynosi {dlugosc_ramiona}")
    obw = base_a + base_b + 2*dlugosc_ramiona
    print(f"Obwód tego trapezu wynosi {obw}")

def zadanie_17():
    print("\nZadanie 17 \nNapisz interaktywny program obliczający objętość kuli dla podanego promienia (skorzystaj z predefiniowanej stałej π z modułu math).")
    print("######################################################")
    radius = float(input("Podaj promień kuli: "))
    volume_of_spheare = 4/3 * math.pi * (radius ** 3)
    print(f"Objętość kuli o promienu {radius}cm wynosi: {volume_of_spheare}cm^3")

def zadanie_18():
    print("""\nZadanie 18 \nNapisz program Sprzedawca samochodów, w którym użytkownik wprowadza
podstawowa˛ cene˛ samochodu. Program powinien dodać szereg dodatkowych
opłat, takich jak podatek, opłate˛ rejestracyjną, prowizją dealera, opłatą za dostarczenie.
Oblicz podatek i opłatę rejestracyjną jako pewien procent ceny podstawowej. Pozostałe
opłaty powinny mieć stałe wartości. Wyświetl cene˛ samochodu po doliczeniu wszystkich
opłat.
    """)
    print("#########################################################################")
    podatek = 0.23 #23%
    oplata_rej = 0.05 #5%
    prowizja_dealera = 500
    oplata_za_dostarczenie = 1500
    cena_samochodu = float(input("Wprowadź podstawową cenę samochodu: "))
    nowa_cena = round(cena_samochodu + (cena_samochodu * podatek) + (cena_samochodu* oplata_rej) + prowizja_dealera + oplata_za_dostarczenie, 2)
    print(f"Nowa cena po wliczeniu wszystkie opłaty wynosi {nowa_cena}zł")

def zadanie_19():
    print("""\nZadanie 19 \nW latach siedemdziesiątych producenci dóbr szybko zbywalnych
w USA i Kanadzie zaczęli znakować swoje towary używając kodów kreskowych. Taki
kod kreskowy albo inaczej UPC (universal product code) identyfikuje zarówno producentą
jak i konkretny produkt. Każdy kod kreskowy jest reprezentowany przez
dwunastocyfrową liczbę (wpisaną zresztą najczęściej pod kodem kreskowym). Oto
przykładowy kod kreskowy: 9 87654 32109 8\n\n""")
    print("""Cyfry: 9 87654 32109 8 są jawnie wypisane pod właściwym kodem kreskowym.
Pierwsza z nich określa typ towaru. Pierwsza grupa pięciu cyfr identyfikuje producenta
towaru. Druga grupa pięciu cyfr jest identyfikatorem produktu. Ostatnia cyfra pełni
funkcję cyfry kontrolnej, której jedynym zadaniem jest weryfikacja poprawności kodu
kreskowego (tj. poprawności poprzednich cyfr). Kiedy taki kod zostanie niepoprawnie
zeskanowany, cyfra kontrolna nie zgadza się z pozostałymi cyframi, więc skaner
kasowy odrzuca kod. Oto jedna z metod obliczania cyfry kontrolnej kodu kreskowego
UPC:""")
    print("""
    *dodaj liczby złożone z cyfry: pierwszej, trzeciej, piątej, siódmej, dziewiątej i jedenastej;
    *dodaj liczby złożone z cyfry: drugiej, czwartej, szóstej, ósmej i dziesiątej;
    *pomnóż pierwszą sumę przez 3 i dodaj ją drugiej sumy;
    *od wyniku odejmij 1;
    *oblicz resztę z dzielenia pomniejszonego wyniku przez 10;
    *odejmij otrzymaną resztę od liczby 9.
""")
    def weryfikacja(liczba):
        table_liczba = list(str(liczba))

        krok1 = 0
        for i in range(0,len(table_liczba),2):
            krok1 += int(table_liczba[i])

        krok2 = 0
        for i in range(1,len(table_liczba),2):
            krok2 += int(table_liczba[i])

        krok3 = (krok1 * 3)+krok2
        krok4 = krok3 - 1
        krok5 = krok4 % 10
        krok6 = 9 - krok5

        return(krok6)

    a = weryfikacja('98765432109')
    b = weryfikacja('01380015173')
    c = weryfikacja('05150024128')
    d = weryfikacja('03120001005')

    print(f"a)9 87654 32109 {a}")
    print(f"b)0 13800 15173 {b}")
    print(f"c)0 51500 24128 {c}")
    print(f"d)0 31200 01005 {d}")

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