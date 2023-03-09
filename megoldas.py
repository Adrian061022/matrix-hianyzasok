#0. feladat a hianyzasok.txt beolvasása listában listákba

hianyzasok=[]
with open("./adatok/hianyzasok.txt","r",encoding="utf-8") as fm:
    for sor in fm:
        seged_lista=sor.strip().split(",")
        # l=[]
        # for szam in seged_lista:
        #     l.append(int(szam))
        # hianyzasok.append(l)
        hianyzasok.append(list(map(int, seged_lista)))
print("A beolvasott mátrix: ")
print(hianyzasok)

# 1. Hány óra hiányzás volt összesen?
osszeg=0
for het in hianyzasok:
    osszeg+=sum(het)

print(f"1. feladat: {osszeg} óra hiányzás volt összesen")


# 2. Volt-e olyan hét, amikor nem volt hiányzó?

ossz=0
for hiany in hianyzasok:
    if hiany!=0:
        ossz+=1
if ossz!=0:
    print("Volt olyan hét, amikor nem volt hiányzó")

# 3. Volt-e olyan hét, amikor ötnél kevesebb hiányzás volt
#3. feladat: Volt olyan hét, amikor ötnél kevesebb hiányzó volt

