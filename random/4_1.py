"""
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, 
majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal! 
Az összehasonlítás eredményéről tájékoztassa a felhasználót! 
"""

import random

veletlen_szam = random.randint(1, 3)
# print(f"Ezt gondolta a gép: {veletlen_szam}")
user_szam = int(input("Gondolj egy számra 1-3 között! "))


if veletlen_szam == user_szam:
    print("Eltaláltad!")
elif veletlen_szam < user_szam:
    print("Egy kicsit kisebbet! ;)")
else:
    print("Picit nagyobbat! :) ")