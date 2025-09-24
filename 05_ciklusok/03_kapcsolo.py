folytatja = True
while folytatja:
	print('Vidd ki a szemetet!')
	valasz = input('Mondjam még egyszer? (i/n) ')
	if valasz == 'n':
		folytatja = False
	elif valasz == 'igen' or 'nem':
		print("Más szerkezetet használj!! (Csak i/n)")
print('>> Program vége! <<')