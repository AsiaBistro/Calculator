def nacti_cislo(text_zadani, text_chyba):
    spatne = True
    while spatne:
        try:
            cislo = float(input(text_zadani))
            spatne = False
        except ValueError:
            print(text_chyba)
        else:
            return cislo


def dalsi_priklad():
    nezadano = True
    while nezadano:
        odpoved = input("Přeje si zadat další příklad? [ y/n ]: ")
        if odpoved == "y" or odpoved == "Y":
            return True
        elif odpoved == "n" or odpoved == "N":
            return False
        else:
            pass


def volba(prvni_cislo, druhe_cislo):
    print("1 - Sčítání")
    print("2 - Odečítání")
    print("3 - Násobení")
    print("4 - Dělení")
    print("5 - Umocňování")
    cislo_operace = nacti_cislo("Zadej volbu: ", "Neplaté zadání\n")
    if cislo_operace == 1:
        print("{0} + {1} = {2}".format(prvni_cislo, druhe_cislo, prvni_cislo + druhe_cislo))
    elif cislo_operace == 2:
        print("{0} - {1} = {2}".format(prvni_cislo, druhe_cislo, prvni_cislo - druhe_cislo))
    elif cislo_operace == 3:
        print("{0} * {1} = {2}".format(prvni_cislo, druhe_cislo, prvni_cislo * druhe_cislo))
    elif cislo_operace == 4:
        mezivysledek = 0
        try:
            mezivysledek = prvni_cislo / druhe_cislo
            print("{0} / {1} = {2}".format(prvni_cislo, druhe_cislo, mezivysledek))
        except ZeroDivisionError:
            print("Dělení nulou!")
    elif cislo_operace == 5:
        print("{0} ** {1} = {2}".format(prvni_cislo, druhe_cislo, prvni_cislo ** druhe_cislo))
    else:
        print("Neplatná volba!")


def main():
    print("Kalkulačka\n")
    pokracovat = True
    while pokracovat:
        prvni_cislo = nacti_cislo("Zadej první číslo:", "Neplatné číslo\n")
        druhe_cislo = nacti_cislo("Zadej druhé číslo:", "Neplatné číslo\n")
        volba(prvni_cislo, druhe_cislo)
        if dalsi_priklad():
            pass
        else:
            pokracovat = False
    input("\nStiskněte libovolnou klávesu.")


main()
