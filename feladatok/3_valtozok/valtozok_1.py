"""
1. Feladat
Készíts egy rövid programot, amely:
-    kommentként tartalmazza a program funkciójának leírását,
-    konstansként tárolja PI értékét,
-    egy másik változóban tárolja egy kör sugarának nagyságát (cm-ben megadva),
-    kiszámolja és a képernyőre kiírja a kör kerületét és területét!
"""
# A program kiszámolja a kör területét és kerületét a megadott sugár alapján, majd kiírja az eredményt.

PI = 3.14
r = int(input("Add meg a kör sugarát cm-ben: "))

circumference = 2 * r * PI
area = PI * r ** 2

print(f"A kör kerülete: {circumference} cm")
print(f"A kör területe: {area} cm²")