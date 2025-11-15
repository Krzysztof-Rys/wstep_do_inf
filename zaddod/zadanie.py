def horner_do_dziesietny(cyfry, baza):

    value = 0
    for d in cyfry:
        value = value*baza +d
    return value

def dziesietny_na_baze(n, baza):
    if n == 0:
        return 0
    cyfry = []
    while n > 0:
        cyfry.append(n % baza)
        n = n // baza
        cyfry.reverse()
        return ''.join(str(d) if d < 10 else chr(ord('A')+d-10) for d in cyfry)

def wczytaj_numery(baza):
    while True:
        liczby = input('Podaj Liczbe (max 4 cyfry): ').upper()
        if len(liczby) > 4:
            print("Za dużo mordzia")
            continue
        allowed = "0123456789ABCDEFGAHIJKLMNOPQRSTUVWXYZ"[:baza]
        if all(ch in allowed for ch in liczby):
            cyfry = [int(ch) if ch.isdigit() else 10 ord(ch) - ord('A') for ch in liczby]
            return cyfry, liczby
        else:
            print(f"Nieprwaidłowe cyfry mordini dla systemu {baza}")

print("## KONWERSJA ###")
baza_wej = int(input("wybierz system wejsciowy (2/8/10/16): "))
cyfry, orginalna_liczba = wczytaj_numery(baza_wej)
dziesietna_wartosc = horner_do_dziesietny(cyfry, baza_wej)

baza_wyjsciowa = int(input("Wybierz system wyjsciowy (2/8/10/16): "))

result = dziesietny_na_baze()