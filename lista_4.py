import random

def zadanie_1():
    print("""\tZadanie 1: \nWykorzystując listy składane rozwiąż następujące zadania (utwórz odpowiednie listy): 
          
          a) Utwórz 20-elementową listę L losowych liczb całkowitych z zakresu od 0 do 100. 
          
          b) Utwórz listę kwadratów liczb z listy L. 
          
          c) Utwórz listę liczb parzystych z listy L. 
          
          d) Utwórz listę liczb z listy L, ale zapisanych w zapisie binarnym (np. liczba 5 powinna być konwertowana na '101' (napis)). 
          
          e) Utwórz listę tylko tych liczb, które należą do przedziału [20, 50] z listy L. 
          
          f) Utwórz 20-elementową listę S1 losowych ciągów tekstowych składających się z małych liter alfabetu łacińskiego o losowej długości z zakresu 3 - 30. 
          
          g) Utwórz listę ciągów tekstowych, które nie zawierają samogłosek z listy S1. 
          
          h) Utwórz 20-elementową listę S2 losowych ciągów tekstowych składających się z małych liter alfabetu łacińskiego i cyfr o losowej długości z zakresu 3 - 30. 
          
          i) Na podstawie listy S2 utwórz listę z napisów oczyszczonych z cyfr. 
          
          j) Na podstawie listy S1 utwórz listę z napisów oczyszczonych z liter, następnie przekształć je na liczby całkowite (pamiętaj o konieczności odrzucenia łańcuchów pustych). 
          
          k) Utwórz 20-elementową listę K losowych krotek losowych liczb całkowitych z zakresu od 0 do 100 o losowej długości z zakresu 1 - 6. 
          
          l) Z podanej listy K utwórz listę krotek dwuelementowych. Odrzuć krótsze krotki, a dłuższe przytnij do pierwszych dwóch elementów. 
          
          m) Z podanej listy K utwórz listę krotek, których suma elementów jest nieparzysta. 
          
          n) Z podanej listy K utwórz listę krotek, których wszystkie elementy są podzielne przez 3. o) Z podanej listy K utwórz listę krotek, w których istnieje element podzielny przez 3.""")
    
    print("Punkt a:")
    L = [random.randint(0, 100) for _ in range(20)]
    print(L)

    print("Punkt b:")
    L_kwadraty = [x**2 for x in L]
    print(L_kwadraty)

    print("Punkt c:")
    L_parzyste = [x for x in L if x % 2 == 0]
    print(L_parzyste)

    print("Punkt d:")
    L_binarnie = [bin(x)[2:] for x in L]
    print(L_binarnie)

    print("Punkt e:")
    L_przedzial = [x for x in L if 20 <= x <= 50]
    print(L_przedzial)

    print("Punkt f:")
    S1 = [''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=random.randint(3, 30))) for _ in range(20)]
    print(S1)

    print("Punkt g:")
    S1_bez_samoglosek = [x for x in S1 if not any(c in x for c in "aeiouy")]
    print(S1_bez_samoglosek)

    print("Punkt h:")
    S2 = [''.join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=random.randint(3, 30))) for _ in range(20)]
    print(S2)

    print("Punkt i:")
    S2_bez_cyfr = [x for x in S2 if not any(c.isdigit() for c in x)]
    print(S2_bez_cyfr)

    print("Punkt j:")
    S1_bez_liter = [x for x in S1 if not any(c.isalpha() for c in x)]
    S1_bez_liter = [int(x) for x in S1_bez_liter if x]

    print("Punkt k:")
    K = [tuple(random.randint(0, 100) for _ in range(random.randint(1, 6))) for _ in range(20)]
    print(K)

    print("Punkt l:")
    K_dwie = [x[:2] for x in K if len(x) >= 2]
    print(K_dwie)

    print("Punkt m:")
    K_nieparzyste = [x for x in K if sum(x) % 2 != 0]
    print(K_nieparzyste)

    print("Punkt n:")
    K_podzielne_3 = [x for x in K if all(y % 3 == 0 for y in x)]
    print(K_podzielne_3)


def zadanie_2():
    print("\tZadanie 2: \nDana jest lista \n\n\tvec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]. \n\nUtwórz listę, w której wszystkie elementy list zagnieżdżonych w vec występują na pierwszym poziomie, tj. [1, 2, 3, 4, 5, 6, 7, 8, 9]. Przedstaw dwa rozwiązania: z zagnieżdżonymi pętlami for oraz z wykorzystaniem listy składanej.")

    vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print("Rozwiązanie z pętlami for:")
    vec_flatten_1 = []

    for sublist in vec:
        for element in sublist:
            vec_flatten_1.append(element)

    print(vec_flatten_1)

    print("Rozwiązanie z listą składaną:")
    vec_flatten_2 = [element for sublist in vec for element in sublist]

    print(vec_flatten_2)

def zadanie_3(): 
    print("""\tZadanie 3: 
          Dana jest lista reprezentująca macierz: 
          
          matrix = [
          [1, 2, 3, 4], 
          [5, 6, 7, 8], 
          [9, 10, 11, 12]
          ]. 
          
          Napisz program, który utworzy na jej podstawie listę reprezentującą macierz transponowaną: 
          
          [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]. 
          
          Wykorzystaj zarówno listy składane, jak i zagnieżdżone pętle (napisz co najmniej dwa różne programy). Napisz funkcję, która wyświetla macierz jak tablice (podobnie jak robimy to na matematyce) - argumentem wywołania powinna być lista reprezentująca macierz.""")
    
    matrix = [
        [1, 2, 3, 4], 
        [5, 6, 7, 8], 
        [9, 10, 11, 12]
    ]

    print("Rozwiązanie z listą składaną:")

    matrix_transposed_1 = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

    print(matrix_transposed_1)

    print("Rozwiązanie z pętlami for:")
    matrix_transposed_2 = []

    for i in range(len(matrix[0])):
        matrix_transposed_2.append([])
        for j in range(len(matrix)):
            matrix_transposed_2[i].append(matrix[j][i])

    print(matrix_transposed_2)


def zadanie_4():
    print("\tZadanie 4: \nNapisz funkcję anonimową (lambda), która podnosi liczbę do kwadratu. Następnie zastosuj tę funkcję do przetworzenia listy liczb [1, 2, 3, 4, 5, 6, 7], wykorzystując funkcję map(). Ostateczny wynik powinien być listą kwadratów liczb.")

    lista = [1, 2, 3, 4, 5, 6, 7]

    lambda_kwadrat = lambda x: x**2

    lista_kwadraty = list(map(lambda_kwadrat, lista))

    print(lista_kwadraty)

def zadanie_5():
    print("\tnZadanie 5: \nKorzystając z funkcji anonimowej (lambda) oraz funkcji wbudowanej filter(), odfiltruj z listy list(range(5, 100, 5)) tylko liczby, które są podzielne przez 10. Wynik przekształć na listę i wyświetl.")

    lista = [x for x in range(5, 100, 5)]

    lista_podzielne_10 = list(filter(lambda x: x % 10 == 0, lista))

    print(lista_podzielne_10)

def zadanie_6(): 
    print("\tZadanie 6: \nRozważmy listę krotek [(1, 'e'), (3, 'd'), (2, 'b'), (7, 'f'), (5, 'a'), (9, 'c')], użyj funkcji anonimowej (lambda) jako klucza sortującego w funkcji sorted(). Posortuj krotki według drugiego elementu w każdej z nich (czyli według litery). Wynik przypisz do nowej zmiennej i wyświetl.")

    lista = [(1, 'e'), (3, 'd'), (2, 'b'), (7, 'f'), (5, 'a'), (9, 'c')]

    sorted_lista = sorted(lista, key=lambda x: x[1], reverse=False)

    print(sorted_lista)

def zadanie_7():
    print("\tZadanie 7: \nMając listę napisów ['koza', 'koń', 'ćma', 'zebra', 'dąb', 'dach', 'ślimak'], użyj funkcji anonimowej (lambda) jako klucza sortującego w metodzie sort() listy. Posortuj napisy alfabetycznie (zgodnie z polskim alfabetem). Wyświetl tablicę po posortowaniu.")

    lista = ['koza', 'koń', 'ćma', 'zebra', 'dąb', 'dach', 'ślimak']  

    polski_alphabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"

    lista.sort(key=lambda x: [polski_alphabet.index(c) for c in x])
    print(lista)

def zadanie_8():
    print("\tZadanie 8: \nStwórz funkcję anonimową (lambda), która przyjmuje liczbę całkowitą i zwraca sumę jej cyfr. Następnie zastosuj tę funkcję do przetworzenia listy [1232, 456, 789, 5431, 74463], używając funkcji map(). Wynik przekształć na listę i wyświetl.")

    lista = [1232, 456, 789, 5431, 74463]

    lambda_suma_cyfr = lambda x: sum(int(c) for c in str(x))

    lista_suma_cyfr = list(map(lambda_suma_cyfr, lista))

    print(lista_suma_cyfr)

def zadanie_9():
    print("\tZadanie 9: \nUtwórz trzy różne funkcje anonimowe (lambda): \n\n\tPierwsza podnosi liczbę do kwadratu. \n\n\tDruga oblicza sześcian liczby. \n\n\tTrzecia oblicza odwrotność liczby (np. dla x = 2 wynik to 0.5). \n\nNastępnie zastosuj każdą z tych funkcji do liczby 2 i wyświetl ich wyniki. Możesz dodatkowo sprawdzić te funkcje na innych liczbach.")

    lambda_pow_2 = lambda x: x**2
    lambda_pow_3 = lambda x: x**3
    lambda_odwrotnosc = lambda x: 1/x

    print(f"Kwadrat liczby 2: {lambda_pow_2(2)}")
    print(f"Sześcian liczby 2: {lambda_pow_3(2)}")
    print(f"Odwrotność liczby 2: {lambda_odwrotnosc(2)}")

def zadanie_10():
    print("\tZadanie 10: \nMając listę liczb całkowitych [1, 2, 3, 4, 5], oblicz iloczyn wszystkich elementów w tej liście. Wykorzystaj do tego funkcję reduce() z modułu functools oraz funkcję anonimową (lambda). Dla tej samej listy znajdź: Sumę kwadratów elementów listy. Największą wartość na liście (również za pomocą reduce()).")

    from functools import reduce

    lista = [1, 2, 3, 4, 5]

    iloczyn = reduce(lambda x, y: x*y, lista)

    print(f"Iloczyn elementów listy: {iloczyn}")

def zadanie_11():
    print("\tZadanie 11: \nNapisz funkcję, która dla podanego jej jako argument ciągu tekstowego zliczy liczbę wystąpień poszczególnych liter w tym ciągu (inne znaki nie powinny być zliczane). Małe i duże litery powinny być traktowane jako te same litery. Wykorzystaj słownik by przechowywać informację o liczbie wystąpień danych liter w podanym tekście. Następnie wykorzystaj typ Counter z modułu collections aby wykonać to zadanie jeszcze prościej. Wyświetl informację o liczbie wystąpień w danej litery zgodnie z porządkiem alfabetycznym.")

    tekst = "Ala ma kota, a kot ma Alę."

    def zlicz_litery(tekst):
        zliczenia = {}
        for c in tekst:
            if c.isalpha():
                c = c.lower()
                if c in zliczenia:
                    zliczenia[c] += 1
                else:
                    zliczenia[c] = 1
        return zliczenia
    
    zliczenia = zlicz_litery(tekst)

    print(f"Tekst: {tekst}")
    print(f"Zliczenia: {zliczenia}")
    

def zadanie_12():
    print("\tZadanie 12: \nWyobraź sobie, że piszesz pewną grę RPG, w wyniku zabicia przeciwnika otrzymujesz listę łupów - być może na liście jest wiele łupów tego samego typu. Napisz funkcję, która konwertuje listę znalezionych łupów na słownik (lub inny obiekt typu odwzorowującego) reprezentujący twój ekwipunek, gdzie dla każdego przedmiotu podana jest jego ilość. Następnie napisz funkcję, która wyświetli zawartość ekwipunku w kolejności.")

    def loot_to_inventory(loot):
        inventory = {}
        for item in loot:
            if item in inventory:
                inventory[item] += 1
            else:
                inventory[item] = 1
        return inventory
    
    def display_inventory(inventory):
        for item, count in inventory.items():
            print(f"{item}: {count}")

    loot = ["miecz", "zbroja", "miecz", "zbroja", "zbroja", "zbroja", "hełm", "tarcza", "tarcza", "tarcza"]

    inventory = loot_to_inventory(loot)

    display_inventory(inventory)



def zadanie_13():
    print("\tZadanie 13: \nNapisz funkcję, która będzie zwracała wartość True, jeżeli przekazany jej ciąg tekstowy będzie zawierał zrównoważoną liczbę nawiasów tj. każdy otwarty nawias powinien być zamknięty. W przeciwnym wypadku funkcja powinna zwracać wartość False. Uwzględnij cztery rodzaje nawiasów: (), [], {} oraz <>. Wykorzystaj słowniki.")

    def balanced_parentheses(text):
        brackets = {
            "(": ")",
            "[": "]",
            "{": "}",
            "<": ">"
        }

        stack = []
        for c in text:
            if c in brackets:
                stack.append(c)
            elif c in brackets.values():
                if not stack or brackets[stack.pop()] != c:
                    return False
        return not stack
    
    print(f"Przykład () : {balanced_parentheses('()')}")
    print(f"Przykład ()() : {balanced_parentheses('()()')}")
    print(f"Przykład (()) : {balanced_parentheses('(())')}")
    print(f"Przykład ( : {balanced_parentheses('(')}")
    print(f"Przykład ) : {balanced_parentheses(')')}")
    print(f"Przykład (] : {balanced_parentheses('(]')}")
    print(f"Przykład ([)] : {balanced_parentheses('([)]')}")
    print(f"Przykład '' {balanced_parentheses('')}")
    tekst = "([{<>}])"
    print(f"Przykład {tekst} : {balanced_parentheses(tekst)}")

def zadanie_14():
    print("\tZadanie 14: \nNapisz program, który pobierze od użytkownika napis. Program powinien wyświetlić informację, z ilu różnych znaków składa się dany wyraz. Zadanie powinna realizować funkcja.")

    def count_unique_characters(text):
        return len(set(text))
    
    while True:
        text = input("Podaj napis(nic nie pisz to zakończy się program): ")
        if not text:
            break
        print(f"Ilość unikalnych znaków: {count_unique_characters(text)}")
        text = ""


def zadanie_15(): 
    print("""\tZadanie 15: 
          Wykorzystaj zbiory oraz działania na nich celem napisania programu, który pobierze od użytkownika dwa napisy, po czym wyświetli (wraz z odpowiednim komunikatem): 
          
          • wszystkie znaki, które znajdują się w jednym lub drugim napisie; 
          
          • wszystkie znaki, które występują w jednym napisie, a nie występują w drugim (osobno); 
          
          • znaki, które znajdują się zarówno w jednym, jak i w drugim napisie""")
    
    def suma_znakow(text1, text2):
        return set(text1) | set(text2)
    
    def roznica_znakow(text1, text2):
        return set(text1) - set(text2), set(text2) - set(text1)
    
    def czesc_wspolna_znakow(text1, text2):
        return set(text1) & set(text2)
    
    text1 = input("Podaj pierwszy napis: ")
    text2 = input("Podaj drugi napis: ")

    print(f"Wszystkie znaki: {suma_znakow(text1, text2)}")
    
    print(f"Znaki w pierwszym napisie, ale nie w drugim: {roznica_znakow(text1, text2)[0]}")

    print(f"Znaki w drugim napisie, ale nie w pierwszym: {roznica_znakow(text1, text2)[1]}")

    print(f"Znaki wspólne: {czesc_wspolna_znakow(text1, text2)}")

    
def zadanie_16():
    print("\tZadanie 16: \nNapisz program 'Prosta gra w statki', który w pewien sposób symuluje grę w statki. Program powinien tworzyć planszę (np. 10 na 10) na której umieszczone będą, w sposób losowy, statki (tylko jednomasztowce). Użytkownik powinien mieć możliwość kolejnego podawania współrzędnych pól w celu zatopienia wszystkich statków. Program powinien wykorzystywać następujące funkcje: funkcja set_ships() – losująca współrzędne statków (jednomasztowców) na planszy i zwracająca zbiór wylosowanych par współrzędnych, funkcja print_board() – wyświetlająca dany stan planszy, funkcja game() – realizująca całą rozgrywkę aż do zatopienia wszystkich statków.")

    def set_ships():
        ships_len = {1: 2, 2: 3, 3: 3, 4: 4, 5: 5} 
        bored = [[0 for _ in range(10)] for _ in range(10)]

        for ship_len in ships_len:
            for _ in range(ships_len[ship_len]):
                while True:
                    x, y = random.randint(0, 9), random.randint(0, 9)
                    if bored[x][y] == 0:
                        bored[x][y] = ship_len
                        break
        return bored
    
    def clean_board(bored):
        return [[0 if x != 0 else x for x in row] for row in bored]
    
    def print_board(bored):
        for row in bored:
            print(" ".join(str(x) for x in row))

    def game():
        bored = set_ships()
        bored_clean = clean_board(bored)
        while any(any(x != 0 for x in row) for row in bored):
            print_board(bored_clean)
            x, y = map(int, input("Podaj współrzędne (x, y): ").split())
            if bored[x][y] != 0:
                bored[x][y] = 0
                bored_clean[x][y] = "*"
            else:
                bored_clean[x][y] = "x"
        print("Wygrana!")

    game()


def zadanie_17():
    print("""Zadanie 17: Masz dwie listy:
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]
Wykonaj następujące operacje w jednym zadaniu:
1. Za pomocą słownika składnego, połącz klucze i wartości z powyższych list, aby
utworzyć słownik.
2. Dodaj do słownika nowy klucz 'e' z wartością będącą sumą wszystkich wartości
w słowniku.
3. Zaktualizuj słownik tak, aby każda wartość była podniesiona do kwadratu (po-
nownie używając słownika składnego).
4. Na koniec odfiltruj tylko te klucze, których wartości są większe niż 10, i utwórz
nowy słownik.""")

    keys = ['a', 'b', 'c', 'd']
    values = [1, 2, 3, 4]

    # 1. Połączenie kluczy i wartości w słownik
    slownik = {k: v for k, v in zip(keys, values)}
    print(f"Słownik: {slownik}")

    # 2. Dodanie nowego klucza 'e' z sumą wszystkich wartości
    slownik['e'] = sum(slownik.values())
    print(f"Słownik po dodaniu 'e': {slownik}")

    # 3. Aktualizacja słownika, aby każda wartość była podniesiona do kwadratu
    slownik = {k: v**2 for k, v in slownik.items()}
    print(f"Słownik po podniesieniu wartości do kwadratu: {slownik}")

    # 4. Filtrowanie kluczy, których wartości są większe niż 10
    slownik_filtered = {k: v for k, v in slownik.items() if v > 10}
    print(f"Słownik po odfiltrowaniu wartości większych niż 10: {slownik_filtered}")

def zadanie_18():
    print("""Zadanie 18: Masz następujący ciąg znaków:
text = "Trzeba być zawsze tylko sobą. Koń bez ułana jest
zawsze koniem. Ułan bez konia tylko człowiekiem."
Wykonaj następujące operacje w jednym zadaniu:
1. Utwórz słownik składany, w którym kluczami są unikalne słowa z tekstu, a wartościami liczba wystąpień każdego słowa (ignorując wielkość liter). W tym samym słowniku, jako wartości, przechowuj również długości słów w osobnym podkluczu, np. {'trzeba': {'count': 1, 'length': 6}, ...}.
2. Usuń z tego słownika wszystkie słowa, które występują tylko raz i mają mniej niż 5 znaków.
3. Posortuj słownik według długości słów (malejąco).""")

    text = "Trzeba być zawsze tylko sobą. Koń bez ułana jest zawsze koniem. Ułan bez konia tylko człowiekiem."

    # 1. Utworzenie słownika składanego
    words = text.lower().replace('.', '').split()
    word_dict = {word: {'count': words.count(word), 'length': len(word)} for word in set(words)}
    
    print(f"\n\nKrok 1:")
    for k, v in word_dict.items():
        print(f"{k}: {v}")

    # 2. Usunięcie słów, które występują tylko raz i mają mniej niż 5 znaków
    word_dict = {k: v for k, v in word_dict.items() if v['count'] > 1 and v['length'] >= 5}
    
    print(f"\n\nKrok 2: {word_dict}")

    # 3. Sortowanie słownika według długości słów (malejąco)
    sorted_word_dict = dict(sorted(word_dict.items(), key=lambda item: item[1]['length'], reverse=True))

    print(f"\n\nKrok 3: {sorted_word_dict}")

def zadanie_19():
    print("""Zadanie 19: Masz następujące dane:
L = list(range(1, 21))
text = "Ta kobieta była jak moneta, szła z ręki do ręki, ale nie straciła na wartości."
Wykonaj następujące kroki używając zbiorów składanych:
1. Utwórz zbiór wszystkich liczb z listy L, które są podzielne przez 3 lub przez 5.
2. Utwórz zbiór unikalnych długości słów w powyższym tekście (ignorując wielkość liter).
3. Utwórz nowy zbiór, który zawiera liczby wspólne dla zbioru z punktu 1 i długości słów z punktu 2.
4. Dodaj do wyniku z punktu 3 liczbę 42, ale tylko jeśli nie jest już w zbiorze.
Sprawdź, czy wynikowy zbiór jest podzbiorem zbioru {1, 2, 3, 5, 10, 15, 20, 42} i wyświetl wynik.
""")
    
    L = list(range(1, 21))
    text = "Ta kobieta była jak moneta, szła z ręki do ręki, ale nie straciła na wartości."

    # 1. Utworzenie zbioru liczb podzielnych przez 3 lub 5
    podzielne_przez_3_lub_5 = {x for x in L if x%3 == 0 or x%5 == 0}
    print(f"\n\nKrok 1: {podzielne_przez_3_lub_5}")

    # 2. Utworzenie zbioru unikalnych długości słów w tekście
    dlugosci_slow = {len(word) for word in text.lower().replace('.', '').split()}
    print(f"\n\nKrok 2: {dlugosci_slow}")

    # 3. Utworzenie zbioru liczb wspólnych dla zbioru z punktu 1 i długości słów z punktu 2
    czesc_wspolna = podzielne_przez_3_lub_5 & dlugosci_slow
    print(f"\n\nKrok 3: {czesc_wspolna}")

    # 4. Dodanie liczby 42, jeśli nie jest już w zbiorze
    if 42 not in czesc_wspolna:
        czesc_wspolna.add(42)
    print(f"\n\nKrok 4: {czesc_wspolna}")

    # Sprawdzenie, czy wynikowy zbiór jest podzbiorem zbioru {1, 2, 3, 5, 10, 15, 20, 42}
    zbior = {1, 2, 3, 5, 10, 15, 20, 42}
    print(f"\n\nCzy wynikowy zbiór({czesc_wspolna}) jest podzbiorem zbioru {zbior}: {czesc_wspolna.issubset(zbior)}")



def zadanie_20():
    print("""Zadanie 20: Masz dwa ciągi znaków:
text1 = "Python to język programowania. Python to język obiektowy."
text2 = "Programowanie w języku Python jest bardzo popularne. Python jest językiem interpretowanym."
Wykonaj następujące operacje:
1. Utwórz zbiory unikalnych słów z obu tekstów, ignorując wielkość liter.
2. Znajdź zbiór wspólnych słów w obu tekstach.
3. Utwórz zbiór słów występujących tylko w jednym z tekstów.
4. Utwórz zbiór długości wspólnych słów z punktu 2.
5. Posortuj wartości zbioru z punktu 4 i wyświetl je jako listę.""")

    text1 = "Python to język programowania. Python to język obiektowy."
    text2 = "Programowanie w języku Python jest bardzo popularne. Python jest językiem interpretowanym."

    # 1. Utworzenie zbiorów unikalnych słów z obu tekstów
    words1 = {word.lower() for word in text1.replace('.', '').split()}
    words2 = {word.lower() for word in text2.replace('.', '').split()}

    print(f"\n\nKrok 1: \nTekst 1: {words1}\nTekst 2: {words2}")

    # 2. Znalezienie zbioru wspólnych słów w obu tekstach
    wspolne_slowa = words1 & words2
    print(f"\n\nKrok 2: {wspolne_slowa}")

    # 3. Utworzenie zbioru słów występujących tylko w jednym z tekstów
    slowa_tylko_w_jednym = words1 ^ words2
    print(f"\n\nKrok 3: {slowa_tylko_w_jednym}")

    # 4. Utworzenie zbioru długości wspólnych słów
    dlugosci_wspolnych_slow = {len(word) for word in wspolne_slowa}

    print(f"\n\nKrok 4: {dlugosci_wspolnych_slow}")

    # 5. Posortowanie wartości zbioru z punktu 4 i wyświetlenie jako listy
    posortowane_dlugosci = sorted(dlugosci_wspolnych_slow)
    print(f"\n\nKrok 5: {posortowane_dlugosci}")

def zadanie_21():
    print("""Zadanie 21: Napisz program, który służy do symulacji tzw. problemu kolekcjonera kuponów.
Podstawowy wariant tego problemu można opisać następująco:
1. mamy n urn (niech n będzie ustalane przez użytkownika z zakresu 2 - 100);
2. do rozważanych urn wrzucamy kolejno kule;
3. wybór każdej urny jest jednakowo prawdopodobny oraz kolejne wybory są wykonywane niezależnie.
Należy wyznaczyć liczbę rzutów Tn, po której w każdej urnie znajdzie się co najmniej jedna kula. Program powinien umożliwiać wielokrotne przeprowadzanie symulacji.""")
    
    def simulation(n):
        urns = [0] * n
        t = 0
        while not all(urns):
            urns[random.randint(0, n-1)] = 1
            t += 1
        return t
    
    while True:
        n = int(input("Podaj liczbę urn (zakres 2-100): ")) or 0
        if not n:
            break
        if 2 <= n <= 100:
            t = simulation(n)
            print(f"Liczba rzutów T{n}, po której w każdej urnie znajdzie się co najmniej jedna kula: {t}")
        else:
            print("Nieprawidłowa liczba urn")


def zadanie_22():
    print("Zadanie 22: Napisz program, który symuluje spadanie kulki po desce Galtona (program powinien umożliwiać wybór liczby szeregów kołków od 1 do 12). Program powinien umożliwiać wielokrotne przeprowadzanie symulacji.")

#do zrobienia kiedys :PPPPP

    

def execute(choice):
    match choice:
        case 1:
            zadanie_1()
        case 2:
            zadanie_2()
        case 3:
            zadanie_3()
        case 4:
            zadanie_4()
        case 5:
            zadanie_5()
        case 6:
            zadanie_6()
        case 7:
            zadanie_7()
        case 8:
            zadanie_8()
        case 9:
            zadanie_9()
        case 10:
            zadanie_10()
        case 11:
            zadanie_11()
        case 12:
            zadanie_12()
        case 13:
            zadanie_13()
        case 14:
            zadanie_14()
        case 15:
            zadanie_15()
        case 16:
            zadanie_16()
        case 17:
            zadanie_17()
        case 18:
            zadanie_18()
        case 19:
            zadanie_19()
        case 20:
            zadanie_20()
        case 21:
            zadanie_21()
        case 22:
            zadanie_22()
        case _:
            print("Nieprawidłowy wybór")

def main():
    while True:
        try:
            choice = int(input("Podaj numer zadania (1-22) lub 0 aby zakończyć: "))
            if choice == 0:
                print("Koniec programu")
                break
            execute(choice)
        except ValueError:
            print("Proszę podać prawidłowy numer")

if __name__ == "__main__":
    main()
