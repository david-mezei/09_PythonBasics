"""
Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot! 
Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt"
számmal, vagy annál kisebb, illetve nagyobb.
"""

import random

gondolt_szam = random.randint(1,5)

# felhasználói hiba kezelése

try: 
    user_szam = int(input("Kérek egy számot! "))
except ValueError:
    print("Kérlek számot írj be!")
    exit()

if gondolt_szam == user_szam:
    print(f"Eltaláltad a számot! A gondolt szám {gondolt_szam} volt.")
elif gondolt_szam > user_szam:
    print("A gondolt szám nagyobb!")
else:
    print("A gondolt szám kisebb!")