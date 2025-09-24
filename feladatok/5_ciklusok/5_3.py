"""
Írj egy programot, amely kiírja a páratlan számokat csökkenő sorrendben 1 és 10 között! 
"""

for szam in range(10,0,-1):
    if szam % 2 != 0:
        print(szam)
