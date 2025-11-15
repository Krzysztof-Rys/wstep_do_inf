def horner_to_decimal(digits, base):
    value = 0
    for d in digits:
        value = value * base + d
    return value

def decimal_to_base(n, base):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(n % base)
        n //= base
    digits.reverse()
    return ''.join(str(d) if d < 10 else chr(ord('A') + d - 10) for d in digits)

def read_number(base):
    while True:
        number = input("Podaj liczbę (max 4 cyfry): ").upper()
        if len(number) > 4:
            print("Za długa liczba! Maks. 4 cyfry.")
            continue

        allowed = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:base]
        if all(ch in allowed for ch in number):
            # zwracamy listę cyfr (dla Hornera)
            digits = [int(ch) if ch.isdigit() else 10 + ord(ch) - ord('A') for ch in number]
            return digits, number
        else:
            print(f"Niepoprawne cyfry dla systemu o podstawie {base}!")

print("## KONWERSJA LICZB ##")

base_in = int(input("Wybierz system wejściowy (2/8/10/16): "))
digits, original_number = read_number(base_in)


decimal_value = horner_to_decimal(digits, base_in)
print(f"\nWartość dziesiętna (Horner): {decimal_value}")

base_out = int(input("Wybierz system wyjściowy (2/8/10/16): "))

result = decimal_to_base(decimal_value, base_out)

print(f"\n== WYNIK ==")
print(f"Liczba {original_number} system {base_in}) → {result} (system {base_out})")


