"""
Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e! 
A válasz kétféle lehet: igen vagy nem. A választól függően írjon ki üzenetet a gép!
"""

user_input = input("Jó napod van? ")

if user_input.lower() == "igen": # user error kezelés, kisbetűs szöveget ellenőrzöm
    print("Örömmel hallom!")
elif user_input.lower() == "nem":
    print("Sajnálom!")