import random

def zadanie_1(): 
    print("\tZadanie 1: \nZdefiniuj funkcję square(), która obliczy wartość trójmianu ax^2 + bx + c w punkcie o wartości x. Argumentami funkcji powinny być kolejne wartości współczynników a, b, c oraz wartość x jako czwarty argument. Sprawdź, czy wartość trójmianu x^2 + 3x + 1 dla x = 2 jest równa 11.")

    def square(a, b, c, x):
        return a * x ** 2 + b * x + c
    
    input_string = input("Podaj współczynniki a, b, c oraz wartość x oddzielone spacją: ")
    a, b, c, x = map(int, input_string.split())

    wynik = square(a, b, c, x)

    print(f"Wartość trójmianu {a}x^2 + {b}x + {c} dla x = {x} wynosi {wynik}")
    
def zadanie_2():    
    print("""\tZadanie 2: \nZdefiniuj funkcję konwertującą temperaturę w skali Celsjusza na skalę Fahrenheita. Funkcja powinna przyjmować argument w postaci temperatury w skali Celsjusza, a zwracać wartość wyrażoną w stopniach Fahrenheita. Wykorzystaj zależność:
\n\tTFahrenheit = (9/5) * TCelsjusz + 32.\n
Następnie napisz program, który będzie konwertował podawane przez użytkownika temperatury dopóki będą one nie mniejsze niż zero bezwzględne (przyjmij, że zero bezwzględne to -273.15°C).""")
    
    def celsius_to_fahrenheit(celsius):
        return (9/5) * celsius + 32
    
    ZERO_BEZWZGLEDNE = -273.15

    while True:
        celsius = float(input("Podaj temperaturę w stopniach Celsjusza: "))
        if celsius < ZERO_BEZWZGLEDNE:
            print("Podana temperatura jest mniejsza niż zero bezwzględne. Koniec programu.")
            break
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} stopni Celsjusza to {fahrenheit} stopni Fahrenheita.")

def zadanie_3():
    print("""Zadanie 3: Zdefiniuj funkcję f(), która przyjmuje jako argumenty dwie liczby i nie
zwraca wartości. Zadaniem funkcji jest wyświetlenie komunikatu na wzór przykładu:
\n\tliczba 7 podzielona przez 3 daje 2 i resztę 1\n
gdy wywołamy f(7, 3). Przetestuj funkcję w prostym programie.""")

    def f(a, b):
        iloraz = a // b
        reszta = a % b
        print(f"liczba {a} podzielona przez {b} daje {iloraz} i resztę {reszta}")

    user_input = input("Podaj dwie liczby oddzielone spacją: ")
    a, b = map(int, user_input.split())
    f(a, b)

def zadanie_4():
    print("""\tZadanie 4: \nZdefiniuj funkcję, która przyjmuje cztery argumenty (dowolne liczby)
i zwraca średnią arytmetyczną trzech największych z nich. W definicji możesz skorzystać tylko z funkcji wbudowanych min(), max() i operatorów arytmetycznych. Nie możesz korzystać z pętli i instrukcji warunkowej. Przetestuj funkcję w prostym programie.""")

    user_input = input("Proszę podać 4 dowolne wartości: ")
    a, b, c , d = map(int, user_input.split())

    srednia = (a+b+c+d - min(a,b,c,d))/3

    print(f"Średnia artmetyczna wynosi: {srednia}")

def zadanie_5():
    print("\tZadanie 5: \nUtwórz funkcję o nazwie order_Tshirt, przyjmującą jako argumenty: wielkość koszulki (S, M, L, XL); kolor; oraz tekst, który ma być na niej nadrukowany. Funkcja powinna wyświetlać zdanie zawierające informacje dotyczące zamówionej koszulki: jej rozmiar, kolor i tekst nadruku. Napisz program, w którym 'zamawiasz' dwie koszulki. W trakcie pierwszego wywołania funkcji do przygotowania koszulki zastosuj argumenty pozycyjne. Natomiast w trakcie drugiego wywołania użyj argumentów w postaci słów kluczowych.")

    def order_Tshirt(size, color, text):
        print(f"Zamówiono koszulkę w rozmiarze {size}, kolorze {color} z nadrukiem: '{text}'")

    # Zamówienie koszulki za pomocą argumentów pozycyjnych
    order_Tshirt("M", "czerwony", "Hello World")

    # Zamówienie koszulki za pomocą argumentów słów kluczowych
    order_Tshirt(size="L", color="niebieski", text="Python is fun")

def zadanie_6():
    print("Zadanie 6: Zmodyfikuj funkcję order_Tshirt z zadania 5 tak, aby domyślnie były zamawiane czarne koszulki w rozmiarze M z nadrukowanym tekstem 'Uwielbiam Pythona'. Zamów koszulkę czarną w rozmiarze L i domyślnym nadrukiem, oraz czerwoną koszulkę o domyślnym rozmiarze i nadruku.")

    def order_Tshirt(size="M", color="czarny", text="Uwielbiam Pythona"):
        print(f"Zamówiono koszulkę w rozmiarze {size}, kolorze {color} z nadrukiem: '{text}'")

    # Zamówienie koszulki czarnej w rozmiarze L i domyślnym nadrukiem
    order_Tshirt(size="L")

    # Zamówienie koszulki czerwonej o domyślnym rozmiarze i nadruku
    order_Tshirt(color="czerwony")

def zadanie_7():
    print("\tZadanie 7: \nNapisz funkcję o nazwie collatz, która pobiera tylko jeden argument o nazwie number. Jeżeli argument funkcji jest parzysty, funkcja powinna wyświetlić i zwrócić wartość number // 2. Jeżeli argument funkcji będzie nieparzysty, wtedy funkcja collatz powinna wyświetlić i zwrócić wartość 3 * number + 1. Napisz program, w którym użytkownik podaje pewną liczbę całkowitą n, a program oblicza wartość funkcji collatz(n) oraz wartości tej funkcji z kolejnych wartości zwracanych przez uprzednie wywołania funkcji collatz, aż do momentu, gdy wartością zwróconą będzie liczba 1. To zaskakujące, ale dla dowolnej liczby całkowitej n, wcześniej czy później otrzymana sekwencja zwracanych liczb zakończy się jedynką. Opisane zagadnienie nosi nazwę problemu Collatza i do dzisiaj nie jest to problem rozwiązany przez matematyków, tzn. nie ma dowodu, że rzeczywiście każda sekwencja liczb będzie kończyć się jedynką dla dowolnej liczby całkowitej n, będącej liczbą początkową sekwencji.")

    def collatz(number, sekwencja):
        if number % 2 == 0:
            result = number // 2
        else:
            result = 3 * number + 1
        print(f"Sekwencja {sekwencja}: {result}")
        return result
    
    x = 1
    n = int(input("Podaj liczbę całkowitą: "))
    while n != 1:
        n = collatz(n, x)
        x += 1

def zadanie_8(): 
    print("\tZadanie 8: \nNapisz program, który symuluje grę w kości. Aby wygrać, w pierwszym rzucie gracz musi wyrzucić na dwóch kościach sumę oczek równą 7 albo 11. Jeżeli wyrzuci sumę 2, 3 lub 12, przegrywa. Każdy inny wynik to tzw. 'punkt' zezwalający na kontynuację gry. W kolejnych rzutach gracz odnosi zwycięstwo, jeżeli ponownie wyrzuci 'punkt', a przegrywa przez wyrzucenie sumy 7. Na końcu każdej gry program ma zapytać użytkownika, czy gra jeszcze raz. Gdy użytkownik zdecyduje o zakończeniu rozgrywki, program ma wypisać liczbę przegranych i wygranych gier i zakończyć działanie. Program powinien wykorzystywać następujące funkcje: funkcja throw() - zwracająca wyniki rzutu dwoma kośćmi, funkcja single_game() - powinna obsługiwać pojedynczą grę poprzez wywołanie funkcji throw() dla określenia wyników kolejnych rzutów, a także wyświetlać przebieg gry i zwracać True gdy gra zakończy się wygraną gracza lub False gdy gracz przegra, funkcja get_answer() powinna pobierać prawidłową odpowiedź (tak lub nie) i ją zwracać, funkcja game() powinna realizować całą rozgrywkę wywołując odpowiednio funkcje single_game() i get_answer() oraz zliczać liczbę wygranych i przegranych gracza.")

    def throw():
        return random.randint(1, 6) + random.randint(1, 6)

    def single_game():
        first_throw = throw()
        punkty = 0
        print(f"Pierwszy rzut: {first_throw}")
        if first_throw in [7, 11]:
            print("Wygrana!")
            return True
        elif first_throw in [2, 3, 12]:
            print("Przegrana!")
            return False
        else:
            punkty += 1
            print("Kontynuacja gry...")
            while True:
                next_throw = throw()
                print(f"Kolejny rzut: {next_throw}")
                if next_throw == 7:
                    print("Przegrana!")
                    return False
                elif next_throw == first_throw:
                    print("Wygrana!")
                    return True

    def get_answer():
        while True:
            answer = input("Czy chcesz zagrać jeszcze raz? (y/n): ")
            if answer.lower() in ['y', 'n']:
                return answer.lower() == 'y'
            print("Nieprawidłowa odpowiedź. Spróbuj ponownie.")

    def game():
        wins = 0
        losses = 0
        while True:
            if single_game():
                wins += 1
            else:
                losses += 1
            if not get_answer():
                break
        print(f"Wygrane: {wins}, Przegrane: {losses}")

    game()


def zadanie_9():
    print("\tZadanie 9: \nNapisz program, który poprosi użytkownika o podanie dowolnego ciągu tekstowego, a następnie wypisze ten ciąg w odwrotnej kolejności.")

    user_input = input("Podaj dowolny ciąg tekstowy: ")

    print(f"Ciąg w odwrotnej kolejności: {user_input[::-1]}")

def zadanie_10():
    print("\tZadanie 10: \nNapisz funkcję is_palindrome(), która zwraca wartość True lub False w zależności od tego, czy argument funkcji (ciąg tekstowy) jest palindromem czy nie.")

    def is_palindrome(text):
        return text == text[::-1]

    user_input = input("Podaj dowolny ciąg tekstowy: ")
    print(f"Czy ciąg jest palindromem? {is_palindrome(user_input)}")

def zadanie_11():
    print("\tZadanie 11: \nNapisz program, który poprosi użytkownika o podanie ciągu tekstowego, a następnie wyświetli ten ciąg bez samogłosek. Wykorzystaj pętlę for.")

    def remove_vowels(text):
        samogloski = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
        new_text = ""
        for letter in text:
            if letter not in samogloski:
                new_text += letter
        return new_text 

    user_input = input("Podaj dowolny ciąg tekstowy: ")
    print(f"Ciąg bez samogłosek: {remove_vowels(user_input)}")
    

def zadanie_12():
    print("\tZadanie 12: \nNapisz program, który zliczy ile razy dana litera pojawia się w podanym przez użytkownika ciągu tekstowym. Program powinien wypisać informacje o liczbie wystąpień każdej litery alfabetu. Program można napisać wykorzystując listy lub, jeszcze prościej, wykorzystując słowniki. Tu wykorzystaj metody ciągów tekstowych, a wyników nigdzie nie musisz zapamiętywać - wystarczy je wyświetlić.")

    letter_count = {}

    user_input = input("Podaj dowolny ciąg tekstowy: ")


    for letter in user_input:
        if letter == " ":
            continue
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    
    letter_count = dict(sorted(letter_count.items()))

    for letter, count in letter_count.items():
        print(f"{letter}: {count}")

    

def zadanie_13():
    print("\tZadanie 13: \nNapisz program, w którym zdefiniowane będą dwie krotki zawierające symbole pierwiastków. Pierwsza krotka powinna zawierać symbole: Li, Na, K, a druga symbole: F, Cl, Br. Program powinien wypisywać związki chemiczne powstałe z połączenia kolejnych symboli pierwiastków z pierwszej krotki z kolejnymi symbolami pierwiastków z drugiej krotki (LiF, LiCl itd.). Użyj dwóch pętli zagnieżdżonych for. Powstałe symbole związków chemicznych są jak najbardziej poprawne (są to halogenki, fluorki, chlorki i bromki).")

    def generate_chemical_compounds():
        alkali_metals = ("Li", "Na", "K")
        halogens = ("F", "Cl", "Br")
        
        for metal in alkali_metals:
            for halogen in halogens:
                print(f"{metal}{halogen}")

    generate_chemical_compounds()

def zadanie_14():
    print("\tZadanie 14: \nNapisz grę 'Przestawione litery'. Gra polega na tym, że komputer wybiera losowo słowo z pewnej grupy słów i tworzy jego 'przestawioną wersję', w której litery występują w przypadkowej kolejności. Użytkownik (gracz), aby wygrać musi podać oryginalne słowo.")

    def shuffle_word(word):
        letters_list = word.split()

        random.shuffle(letters_list)

        return "".join(letters_list)
    
    tries = 0

    words = ["kot", "pies", "samochód", "rower", "telefon", "komputer", "programowanie", "python", "java", "javascript"]

    word = random.choice(words)

    shuffled_word = shuffle_word(word)

    while True:
        print(f"Przestawione słowo: {shuffled_word}")
        user_input = input("Jakie to słowo? ")
        if user_input == word:
            print("Brawo! Zgadłeś!")
            break
        else:
            print("Niepoprawna odpowiedź. Spróbuj ponownie.")
            tries += 1

    print(f"Zgadłeś w {tries} próbach.")

def zadanie_15(): #hangman
    print('\tZadanie 15: \nNapisz grę "Zgadnij jakie to słowo". Gra polega na tym, że komputer wybiera losowo słowo z pewnej grupy słów. Komputer informuje gracza ile liter posiada dane słowo. Następnie gracz otrzymuje pięć szans na zadanie pytania komputerowi, czy jakaś litera jest zawarta w tym słowie. Komputer może odpowiadać tylko "TAK" lub "NIE".')

    words = ["kot", "pies", "samochód", "rower", "telefon", "komputer", "programowanie", "python", "java", "javascript"]

    word = random.choice(words)

    guessed_word = ["_" for _ in word]

    tries = 5

    print(f"Słowo ma {len(word)} liter.")

    while tries > 0:
        print(" ".join(guessed_word))
        letter = input("Podaj literę: ")
        if letter in word:
            print("TAK")
            for i in range(len(word)):
                if word[i] == letter:
                    guessed_word[i] = letter
        else:
            print("NIE")
            tries -= 1

        if "_" not in guessed_word:
            print("Brawo! Zgadłeś słowo!")
            break
    else:
        print(f"Nie udało się zgadnąć słowa. Prawidłowe słowo to {word}")

def zadanie_16():
    print("\tZadanie 16: \tUtwórz listę z dowolnymi napisami. Następnie wygeneruj na jej podstawie listę, która zawiera pierwsze znaki napisów zawartych w Twojej liście.")

    def first_characters(strings):
        return [s[0] for s in strings if s]

    strings = ["apple", "banana", "cherry", "date", "elderberry"]
    first_chars = first_characters(strings)
    print(f"Lista pierwszych znaków: {first_chars}")

def zadanie_17(): 
    
    print("\tZadanie 17: \nNapisz program, który utworzy listę kwadratów liczb całkowitych od 0 do 9. Wykorzystaj pętlę for oraz metodę append(). Następnie zmodyfikuj program poprzez zdefiniowanie funkcji, która przyjmie jako argument listę zawierającą liczby, a następnie zwróci listę odpowiadających im kwadratów. Np. dla [-1, 2, -6, 9] funkcja powinna zwrócić listę [1, 4, 36, 81].")

    lista = [i for i in range(-9, 10)]

    print(f"Lista: \t{lista}")

    kwadraty = [i ** 2 for i in lista]

    print(f"Kwadraty: \t{kwadraty}")


def zadanie_18():
    print("\tZadanie 18: \nNapisz program, który pozwoli na przechowywanie w liście pięciu najlepszych wyników gracza. Program powinien, poprzez wyświetlenie odpowiedniego menu, dać możliwość wykonywania operacji na liście wyników np. dodawanie wyników, usuwanie wyników, sortowanie itp. Program powinien także umożliwiać użytkownikowi zakończenie pracy z listą wyników. Na początku lista wyników powinna być pusta, a w trakcie działania programu powinna przechowywać maksymalnie 5 najlepszych wyników (jeżeli zostanie dodany 6 wynik to z listy powinien zniknąć aktualnie najgorszy wynik).")

    def add_score(score):
        for i in range(len(scores[1])):
            if score >= scores[1][i]:
                scores[1].insert(i, score)
                scores[1].pop()
                break

    def remove_score(score_number):
            scores[1][score_number - 1] = 0
            scores[1].sort(reverse=True)

    def display_scores():
        print("+-------------------+")
        print("|  Nr  |   Wynik    |")
        print("+-------------------+")
        for i in range(len(scores[0])):
            print(f"|  {scores[0][i]:<3} |   {scores[1][i]:<7} |")
        print("+-------------------+")

    def exit_program():
        print("Zakończono program.")
        return False


    scores = [[1, 2, 3, 4, 5], [0, 0, 0, 0, 0]]

    Warunek = True

    while Warunek == True:
        print("1. Dodaj wynik")
        print("2. Usuń wynik")
        print("3. Wyświetl wyniki")
        print("4. Zakończ program")
        choice = input("Wybierz opcję: ")

        match choice:
            case "1":
                score = int(input("Podaj wynik: "))
                add_score(score)
            case "2":
                score_number = int(input("Podaj numer wyniku do usunięcia: "))
                remove_score(score_number)
            case "3":
                display_scores()
            case "4":
                Warunek = exit_program()
            case _:
                print("Nieprawidłowa opcja. Spróbuj ponownie.")


def zadanie_19():
    print("\tZadanie 19: \nNapisz program 'Generator obelg', który będzie w wyrafinowany sposób obrażał osobę podaną przez użytkownika. Program powinien prosić o podanie imienia i wieku 'ofiary'. W programie powinny być zadeklarowane dwie listy z przymiotnikami i rzeczownikami (na początku dwuelementowe). Program powinien umożliwić dodawanie i usuwanie przymiotników/rzeczowników z list (na listach zawsze powinny być minimum dwa słowa), a także umożliwić zakończenie programu. W zależności od wieku program powinien dobierać jeszcze jeden przymiotnik aby obelga była bardziej dopasowana np. nieopierzony, stary, zgrzybiały itp.")

    adjectives = ["głupi", "brzydki"]
    nouns = ["osioł", "bałwan"]

    def generate_insult(name, age):
        age_adj = ""
        if age < 18:
            age_adj = "nieopierzony"
        elif age < 50:
            age_adj = "stary"
        else:
            age_adj = "zgrzybiały"
        insult = f"{name}, ty {age_adj} {random.choice(adjectives)} {random.choice(nouns)}!"
        print(insult)

    def add_word(word_list, word):
        if len(word_list) < 2:
            word_list.append(word)
        else:
            word_list.append(word)

    def remove_word(word_list, word):
        if len(word_list) > 2:
            word_list.remove(word)
        else:
            print("Na liście muszą być minimum dwa słowa.")

    while True:
        print("1. Wygeneruj obelgę")
        print("2. Dodaj przymiotnik")
        print("3. Dodaj rzeczownik")
        print("4. Usuń przymiotnik")
        print("5. Usuń rzeczownik")
        print("6. Zakończ program")
        choice = input("Wybierz opcję: ")

        if choice == "1":
            name = input("Podaj imię ofiary: ")
            age = int(input("Podaj wiek ofiary: "))
            generate_insult(name, age)
        elif choice == "2":
            word = input("Podaj przymiotnik do dodania: ")
            add_word(adjectives, word)
        elif choice == "3":
            word = input("Podaj rzeczownik do dodania: ")
            add_word(nouns, word)
        elif choice == "4":
            word = input("Podaj przymiotnik do usunięcia: ")
            remove_word(adjectives, word)
        elif choice == "5":
            word = input("Podaj rzeczownik do usunięcia: ")
            remove_word(nouns, word)
        elif choice == "6":
            break
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")



def zadanie_20():
    print("\tZadanie 20: \nNapisz grę 'Wisielec'. W grze komputer wybiera ukryte słowo, a zadaniem gracza jest próba jego stopniowego odgadnięcia litera po literze. Za każdym razem, gdy litera podana przez gracza jest niepoprawna (nie ma jej w słowie), komputer pokazuje nowy rysunek wieszanej postaci. Jeżeli gracz nie odgadnie słowa w porę, ludzik z rysunku traci życie.")

    def display_hangman(lives): # funkcja wyświetlająca rysunek wieszaka, kod pochodzi z https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c, hope u dont mind, just was to lazy to draw it myself :P 
        hangman = [
            "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
            "  +---+\n  |   |\n      |\n      |\n      |\n      |\n========="
        ]
        print(hangman[lives])

    def display_word(word, guessed_letters):
        for letter in word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")

        print()
        

    def hangman():
        words = ["python", "javascript", "java", "ruby", "csharp", "swift", "kotlin", "php", "html", "css"]
        word = random.choice(words)
        guessed_letters = []
        lives = 6

        while True:
            display_hangman(lives)
            display_word(word, guessed_letters)
            if all(letter in guessed_letters for letter in word):
                print("Brawo! Zgadłeś słowo!")
                break
            if lives == 0:
                print(f"Nie udało się zgadnąć słowa. Prawidłowe słowo to {word}")
                break
            letter = input("Podaj literę: ")
            if letter in guessed_letters:
                print("Ta litera już była.")
                continue
            guessed_letters.append(letter)
            if letter not in word:
                lives -= 1

    hangman()

def execute(task_number):
    match task_number:
        case "1":
            zadanie_1()
        case "2":
            zadanie_2()
        case "3":
            zadanie_3()
        case "4":
            zadanie_4()
        case "5":
            zadanie_5()
        case "6":
            zadanie_6()
        case "7":
            zadanie_7()
        case "8":
            zadanie_8()
        case "9":
            zadanie_9()
        case "10":
            zadanie_10()
        case "11":
            zadanie_11()
        case "12":
            zadanie_12()
        case "13":
            zadanie_13()
        case "14":
            zadanie_14()
        case "15":
            zadanie_15()
        case "16":
            zadanie_16()
        case "17":
            zadanie_17()
        case "18":
            zadanie_18()
        case "19":
            zadanie_19()
        case "20":
            zadanie_20()
        case _:
            print("Invalid task number")

def main():
    while True:
        user_input = input("Wybierz nr zadania (1-20) lub 'x' aby zakończyć: ")
        if user_input.lower() == 'x':
            break
        execute(user_input)

if __name__ == "__main__":
    main()
