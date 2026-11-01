
import random
import math

# ZADANIE 1

print("\n========== ZADANIE 1 ==========")

print("1. 1 + 2 =", 1 + 2, type(1 + 2))
print("2. 1 + 4.5 =", 1 + 4.5, type(1 + 4.5))
print("3. 3 / 2 =", 3 / 2, type(3 / 2))
print("4. 4 / 2 =", 4 / 2, type(4 / 2))
print("5. 3 // 2 =", 3 // 2, type(3 // 2))
print("6. -3 // 2 =", -3 // 2, type(-3 // 2))
print("7. 11 % 2 =", 11 % 2, type(11 % 2))
print("8. 2 ** 10 =", 2 ** 10, type(2 ** 10))
print("9. 8 ** (1/3) =", 8 ** (1/3), type(8 ** (1/3)))

print(int(3.0))
print(float(3))
print(float("3"))
print(str(12.4))
print(bool(0))


# ZADANIE 2

print("\n========== ZADANIE 2 ==========")

uczelnia = "Studiuję na WSIiZ"

print(uczelnia)


# ZADANIE 3

print("\n========== ZADANIE 3 ==========")

imie = "Jan"
wiek = 20
wzrost = 178

print(f"Nazywam się {imie} i mam {wiek} lat.")
print(f"Mój wzrost to {wzrost} cm.")


# ZADANIE 4

print("\n========== ZADANIE 4 ==========")

Cena = 39.99
Rabat = 0.2

cena_koncowa = Cena * (1 - Rabat)

print(f"Cena produktu: {Cena:.2f} PLN")
print(f"Cena po rabacie: {cena_koncowa:.2f} PLN")


# ZADANIE 5

print("\n========== ZADANIE 5 ==========")

bok_a = float(input("Podaj długość pierwszego boku: "))
bok_b = float(input("Podaj długość drugiego boku: "))

pole = bok_a * bok_b
obwod = 2 * (bok_a + bok_b)

print(f"Pole prostokąta wynosi: {pole}")
print(f"Obwód prostokąta wynosi: {obwod}")


# ZADANIE 6

print("\n========== ZADANIE 6 ==========")

droga = random.randint(100, 1000)

spalanie = float(input("Podaj średnie spalanie: "))
cena_paliwa = float(input("Podaj cenę paliwa za litr: "))

zuzyte_paliwo = droga * spalanie / 100
koszt_podrozy = zuzyte_paliwo * cena_paliwa

print(f"Długość trasy: {droga} km")
print(f"Zużyte paliwo: {zuzyte_paliwo:.2f} litrów")
print(f"Koszt podróży: {koszt_podrozy:.2f} PLN")


# ZADANIE 7

print("\n========== ZADANIE 7 ==========")

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))

if a != 0:
    x = -b / a
    print(f"x = {x}")
elif b == 0:
    print("Nieskończenie wiele rozwiązań.")
else:
    print("Brak rozwiązań.")


# ZADANIE 8

print("\n========== ZADANIE 8 ==========")

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

if a == 0:
    print("To nie jest równanie kwadratowe.")
else:
    delta = b**2 - 4*a*c

    print(f"Delta = {delta}")

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)

        print(f"x1 = {x1}")
        print(f"x2 = {x2}")

    elif delta == 0:
        x = -b / (2*a)
        print(f"x = {x}")

    else:
        print("Brak rozwiązań rzeczywistych.")


# ZADANIE 9

print("\n========== ZADANIE 9 ==========")

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

print(f"Dodawanie: {a + b}")
print(f"Odejmowanie: {a - b}")
print(f"Mnożenie: {a * b}")

if b != 0:
    print(f"Dzielenie: {a / b}")
else:
    print("Nie można dzielić przez zero.")

print(f"Potęgowanie: {a ** b}")

print("\n========== KONIEC ==========")
