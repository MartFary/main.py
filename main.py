
#projekt_2.py: druhý projekt do Engeto Online Python Akademie
#
#author: Martina Farkavcová
#email: martinafarkavcova@gmail.com

import random

def uvitaci_zprava():    #program pozdraví uživatele a vypíše úvodní text.
    print("Hi there!")
    print("I've generated a random 4 digit number for you. \nLet's play a bulls and cows game.")
    print("Enter a number:")

def tajne_cislo():    #program vytvoří tajné 4 místné číslo (číslice musí být unikátní a nesmí začínat 0).
    seznam_cisel = list("0123456789")
    cislo = ""

    while True:
        cislo = "".join(random.sample(seznam_cisel, 4))
        if cislo[0] != "0":
            return cislo
        
# test funkce tajne_cislo for _ in range(4):        
#                            print(tajne_cislo())

def validni_cislo_uzivatele(uzivatel):    #Program uživatele upozorní na chybně zadané číslo
    if len(uzivatel) != 4:
        return False, "Zadej 4 čísla."
    if not uzivatel.isdigit():
        return False, "Neplatné znaky, zadej pouze čísla."
    if uzivatel[0] == "0":
        return False, "Číslo nesmí začínat nulou."
    if len(set(uzivatel)) != 4:
        return False, "Čísla se nesmí opakovat."
    return True, ""

# test ověření funkce hádání čísla uživatelem:
# uzivatel = input("Zadej číslo: ")
# validni, error = validni_cislo_uzivatele(uzivatel)
# if not validni:
#    print("Chyba:", error)

def vyhodnoceni_tipu_uzivatele(uzivatel, tajne_cislo):    # vyhodnotí tip od uživatele
    bulls = 0
    cows = 0

    for pozice in range(4):
        if uzivatel[pozice] == tajne_cislo[pozice]:
            bulls += 1
        elif uzivatel[pozice] in tajne_cislo:
            cows += 1

    return bulls, cows

def pluralize(word, count):    #ošetření gramatiky pomocí funkce pluralize
    if count == 1:
        return f"{count} {word}"
    else:
        return f"{count} {word}s"

# Spuštění celé hry + navíc jsem omezila počet pokusů na 10 a při prohře jsem chtěla vědět, 
# jaké bylo to hádané číslo, protože jsem to na 10 pokusů většinou neuhodla :-)

uvitaci_zprava()
hadane_cislo = tajne_cislo()
pokus = 0
max_pokusu = 10    #omezení počtu pokusů na 10

while True:
    if pokus >= max_pokusu:
        print(f"Vyčerpáno 10 pokusů. \nTajné číslo bylo: {hadane_cislo} \nZahraj si novou hru.")
        break

    uzivatel = input(">> ")
    validni, error = validni_cislo_uzivatele(uzivatel)

    if not validni:
        print("Chyba:", error)
        continue

    pokus += 1
    bulls, cows = vyhodnoceni_tipu_uzivatele(uzivatel, hadane_cislo)

    print(f"{pluralize('bull', bulls)}, {pluralize('cow', cows)}")

    if bulls == 4:
        print(f"Gratuluji k uhodnutí tajného čísla!")
        break
