# Funkcja wyświetlająca menu z dostępnymi operacjami
def pokaz_menu():
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

# Funkcja, która wykonuje operację kalkulacji na podstawie wyboru użytkownika
def kalkulator():
    pokaz_menu()  # Wyświetlamy menu z operacjami

    # Pobieramy wybór użytkownika
    wybor = input("Wprowadź numer operacji (1/2/3/4): ")

    # Sprawdzamy, czy użytkownik wybrał poprawną opcję
    if wybor in ['1', '2', '3', '4']:
        # Pobieramy od użytkownika dwie liczby do obliczeń
        liczba1 = float(input("Wprowadź pierwszą liczbę: "))
        liczba2 = float(input("Wprowadź drugą liczbę: "))

        # Sprawdzamy, jaka operacja została wybrana i wykonujemy odpowiednią kalkulację
        if wybor == '1':
            wynik = liczba1 + liczba2
            print(f"Wynik dodawania: {wynik}")
        elif wybor == '2':
            wynik = liczba1 - liczba2
            print(f"Wynik odejmowania: {wynik}")
        elif wybor == '3':
            wynik = liczba1 * liczba2
            print(f"Wynik mnożenia: {wynik}")
        elif wybor == '4':
            if liczba2 != 0:  # Sprawdzamy, czy nie dzielimy przez 0
                wynik = liczba1 / liczba2
                print(f"Wynik dzielenia: {wynik}")
            else:
                print("Nie można dzielić przez zero!")  # Komunikat o błędzie dzielenia przez 0
    else:
        print("Niepoprawny wybór, spróbuj ponownie.")  # Komunikat w przypadku błędnego wyboru

# Wywołanie funkcji kalkulatora, aby zacząć działanie programu
kalkulator()