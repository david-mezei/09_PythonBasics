"""
Kérj be egy jelszót, és ha megegyezik a „titok” szóval, írd ki: „Belépés engedélyezve!”, különben „Helytelen jelszó!”.
"""

password = input("Adj meg egy jelszót: ")

if password == "titok":
    print("Belépés engedélyezve!")
else:
    print("Helytelen jelszó!")