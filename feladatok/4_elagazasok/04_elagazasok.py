"""
Ha a bevitt szám kisebb, mint 0: negatív; ha a bevitt szám 0: nulla; ha a bevitt szám nagyobb, mint 0: pozitív
"""

szam = int(input("Adj meg egy számot! "))

print("::::::::::::::::::::::::::::::::")

# Pozitív, negatív, nulla
if szam < 0:
    print("A megadott szám negatív.")
elif szam == 0: 
    print("A megadott szám nulla.")
else: 
    print("A megadott szám pozítív.")


# Paritás
if szam % 2 == 0 and szam != 0:
    print("A megadott szám páros.")
elif szam % 2 == 1: 
    print("A megadott szám páratlan.")
else:
    print("A szám nulla.")