"""
Kérj be egy évet, és írd ki, hogy szökőév-e.
(Szökőév, ha osztható 4-gyel, de nem 100-zal, kivéve ha 400-zal is osztható.)
"""

year = int(input("Adj meg egy évszámot, és a program megmondja, hogy szökőév-e: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} szökőév")
else: 
    print(f"{year} nem szökőév")