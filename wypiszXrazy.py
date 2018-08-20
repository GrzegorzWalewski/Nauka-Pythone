wyraz=input("Podaj jakis wyraz\n")
ile=int(input("Podaj ile razy mam go wypisac\n"))
for i in range(1,ile):
	print("{}{}{}".format(i,"."),wyraz)