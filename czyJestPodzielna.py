podzielna=int(input("Podaj liczbe ktora chcesz podzielic\n"))
dzielnik=int(input("Podaj liczbe przez ktora chcesz dzielic\n"))
if dzielnik==0:
	print("Pamietaj nie dziel przez ZERO!")
	input()
	quit()
if podzielna%dzielnik>=1:
	print("{} nie jest podzielna przez {}".format(podzielna,dzielnik))
else:
	wynik=int(podzielna/dzielnik)
	print("Super! {} jest podzielna przez {}, a wynik tego dzielenia wynosi {}".format(podzielna,dzielnik,wynik))