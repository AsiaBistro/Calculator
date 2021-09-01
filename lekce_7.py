"""pokracovat = True
while pokracovat:
    slovo = input("Zadejte slovo, program zjistí, zda-li to je palindrom.\n")
    otocene_slovo = slovo[::-1]
    if slovo == otocene_slovo:
        print("Ano, {0} je palindrom.".format(slovo))
    else:
        print("Ne, {0} není palindrom.".format(slovo))
    nove_slovo = True
    while nove_slovo:
        odpoved =input("Přejete si zadat další slovo? y/n")
        if (odpoved == "y" or odpoved == "Y"):
            nove_slovo = False
        elif(odpoved == "n" or odpoved =="N"):
            nove_slovo = False
            pokracovat = False
        else:
            pass
input("Stisknete libivolnou klavesu")"""

"""print("ASCII Tabulka")
print("==================")
tabulka = 0

while tabulka < 256:
    print(tabulka, chr(tabulka), "\t" ,end="")
    tabulka = tabulka + 1
else:
    pass
input()"""

"""text = input("Slovo:")
heslo = input("Heslo: ")
vystup = ""


for i, znak in enumerate(text):
    if len(heslo) % len(text) > 1:
        heslo = heslo + heslo[i - len(heslo)]
    posun = ord(znak) + ord(heslo[i]) - 96 
    if posun > ord("z"):
        posun = posun - 26
    sifra = chr(posun)
    vystup = vystup + sifra

print("Původní zpráva:{0}".format(text))
print("Heslo:{0}".format(heslo))
print("Zašifrovaná zpráva:{0}".format(vystup))"""""




  
