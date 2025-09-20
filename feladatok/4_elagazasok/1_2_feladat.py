"""
Fejleszd tovább az első feladat programját úgy, 
hogy amennyiben a felhasználó nem a két lehetséges válasz (igen/nem) közül ad meg egyet, 
a gép kiírja: "Sajnos nem értem a válaszodat!"

"""

user_input = input("Jó napod van? ")

if user_input.lower() == "igen": # user error kezelés, kisbetűs szöveget ellenőrzöm
    print("Örömmel hallom!")
elif user_input.lower() == "nem":
    print("Sajnálom!")
else:
    print("Sajnos nem értem a válaszodat!")