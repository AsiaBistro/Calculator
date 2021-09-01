"""print("Program zjistí z čeho se skládá slovo.")
slovo = input("Zadejte slovo:")
samohlasky = 0
souhlasky = 0
ostatni = 0
cisel = 0
for znak in slovo:
    if znak in "aáeéěiíoóuúů":
        samohlasky = samohlasky + 1
    elif znak in "bcčdďfghjklmnňpqrřsštťvwxzž":
        souhlasky = souhlasky + 1
    elif ord(znak) in range(48,58):
        cisel = cisel +1
    else:
        pass
print("slovo má: ")
print("samohlásek", samohlasky)
print("souhlásek", souhlasky)
print("čísel", cisel)
print("ostatní znaky", len(slovo) - samohlasky - souhlasky - cisel)
input("Aplikaci ukopnčíte stisknutím libovolné klávesy...\n")"""

"""print("Césarova šifra")
retezec = input("Zadej slovo: ")
posun = int(input("Zadejte posun:"))
print("Puvodni zprava:", retezec)
zprava = ""

for znak in retezec:
    i = ord(znak)
    i = i + posun
    if (i> ord("z")):
        i = i - 26
    znak = chr(i)
    zprava = zprava + znak
print("Zasirovana zprava:", zprava)
input()"""

