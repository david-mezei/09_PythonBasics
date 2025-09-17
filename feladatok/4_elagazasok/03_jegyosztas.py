"""
Kérj be egy pontszámot 0-100 között, és írd ki az érdemjegyet:
- 0-49: Elégtelen 
- 50-64: Elégséges
- 65-79: Közepes
- 80-89: Jó
- 90-100: Jeles
"""

pontszam = int(input("Adj meg egy pontszámot! [0-100] "))

if pontszam <= 49:
    print("Elégtelen")
elif pontszam <= 64:
    print("Elégséges")
elif pontszam <= 79:
    print("Közepes")
elif pontszam <= 89:
    print("Jó")
elif pontszam <= 100:
    print("Jeles")
else:
    print("Hibás számformátum! [0-100]")