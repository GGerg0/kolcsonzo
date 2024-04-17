class Kolcsonzes:
    def __init__(self,nev,azonosito,elora,elperc,visszaora,visszaperc):
        self.nev = nev
        self.azonosito = azonosito
        self.elora = elora
        self.elperc = elperc
        self.visszaora = visszaora
        self.visszaperc = visszaperc
    def __str__(self) -> str:
        return f"{adatok[szam].elora}:{adatok[szam].elperc}-{adatok[szam].visszaora}:{adatok[szam].visszaperc}"

def perc(ora,perc):
    return int(ora*60+perc)


f = open("kolcsonzesek.txt","rt",encoding="utf-8")

adatok = []

for sor in f:
    sor = sor.strip().split(";")
    adatok.append(Kolcsonzes(str(sor[0]),sor[1],sor[2],sor[3],sor[4],sor[5]))

print(f"5. feladat:\tNapi kölcsözések száma: {len(adatok)-1}")

innev = input("6. feladat:\tKérek egy nevet: ")
print(f"\t{innev} kölcsönzései:")
tmp = 0
for szam in range(1,len(adatok)):
    if adatok[szam].nev == innev:
        print(f"\t\t{adatok[szam]}")
        tmp += 1
    
if tmp == 0:
    print("\t\tNem volt ilyen nevű kölcsönző!")

ido = input("6. feladat:\tAdjon meg egy időpontot óra:perc alakban: ").split(":")


ido = perc(int(ido[0]),int(ido[1]))

for kolcson in range(1,len(adatok)):
    kezdet = perc(int(adatok[kolcson].elora),int(adatok[kolcson].elperc))
    veg = perc(int(adatok[kolcson].visszaora),int(adatok[kolcson].visszaperc))
    if ido >= kezdet and ido < veg:
        print(f"{adatok[kolcson]}\t:\t{adatok[kolcson].nev}")