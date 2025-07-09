
#projekt_1.py: první projekt do Engeto online python Akademie
#
#author: Martina Farkavcová
#email: martinafarkavcova@gmail.com

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

user = ["bob", "ann", "mike", "liz"]
password = ["123", "pass123", "password123", "pass123"]
registrovany = dict(zip(user, password))

jmeno = input("Zadej jméno:")
heslo = input("Zadej heslo:")

if jmeno in registrovany and registrovany[jmeno] == heslo:
    print(f"Vítám tě v aplikaci, {jmeno}. \nMáme 3 texty k analýze.")
    cislo_textu = input("Zadej číslo textu od 1 do 3 k analýze:")
    if not cislo_textu.isdigit():
        print("Špatně zadané číslo.")
    else:
        cislo = int(cislo_textu)
        if 1 <= cislo <= 3:
            text = TEXTS[cislo - 1]
            print(f"Analyzuji text číslo {cislo}")

            slova = text.split()

            slova_pocet_all = len(slova)
            slova_prvni_velke = 0
            slova_vse_velke = 0
            slova_vse_male = 0
            slova_cisla = 0
            slova_cisla_soucet = 0

            for slovo in slova:
                ocisteno = slovo.strip(".,!?")

                if ocisteno.istitle():
                    slova_prvni_velke = slova_prvni_velke + 1
                elif ocisteno.isupper():
                    slova_vse_velke = slova_vse_velke + 1
                elif ocisteno.islower():
                    slova_vse_male = slova_vse_male + 1
                if ocisteno.isdigit():
                    slova_cisla = slova_cisla + 1
                    slova_cisla_soucet += int(ocisteno)
                

            print(f"Ve vybraném textu je {slova_pocet_all} slov.")
            print(f"Ve vybraném textu je {slova_prvni_velke} slov, která začínají velkým písmenem.")
            print(f"Ve vybraném textu je {slova_vse_velke} slov, která jsou psaná velkými písmeny.")
            print(f"Ve vybraném textu je {slova_vse_male} slov, která jsou psaná malými písmeny.")
            print(f"Ve vybraném textu je {slova_cisla} slov ve formátu čísel.")
            print(f"Ve vybraném textu je součet všech čísel {slova_cisla_soucet}.")

            print("Grafické znázornění délky slov v analyzovaném textu.")
            print(f"{'DÉLKA':<6} | {'GRAF':<20} | {'VÝSKYT':<7}")
            cetnost_znaku = {}

            for slovo in slova:
                ocisteno = slovo.strip(".,!?")
                delka = len(ocisteno)
                slova_pocet_all = slova_pocet_all + 1
                if delka in cetnost_znaku:
                    cetnost_znaku[delka] = cetnost_znaku[delka] + 1
                else: 
                    cetnost_znaku[delka] = 1

            for delka in sorted(cetnost_znaku):
                pocet = cetnost_znaku[delka]
                graf = "*" * pocet

                print(f"{delka:<6} | {graf:<20} | {pocet:<7}")

        else:
            print("Číslo není v zadaném rozmezí.")
else:
    print("Špatné jméno nebo heslo.")





