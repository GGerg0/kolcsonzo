class Kolcsonzes:
    def __init__(self,nev,azonosito,elora,elperc,visszaora,visszaperc):
        self.nev = nev
        self.azonosito = azonosito
        self.elora = elora
        self.elperc = elperc
        self.visszaora = visszaora
        self.visszaperc = visszaperc

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
        print(f"\t\t{adatok[szam].elora}:{adatok[szam].elperc}-{adatok[szam].visszaora}:{adatok[szam].visszaperc}")
        tmp += 1
    
if tmp == 0:
    print("\t\tNem volt ilyen nevű kölcsönző!")
