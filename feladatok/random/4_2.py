"""
A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e! 
"""

import random

penzdobas = ["fej", "írás"]
sorsolas = random.choice(penzdobas)

print(f"A gép válasza: {sorsolas}")
user_valasztas = input("Fej vagy írás? ")

if user_valasztas.lower() != "fej" or "írás":
    print(f"Nem megfelelő adat!")
elif user_valasztas.lower() == sorsolas:
    print(f"Eltaláltad, a válasz {sorsolas} volt")
else:
    print("Sajnos nem sikerült! ")