imie=input("Jak masz na imie?\n")
print("Czesc",imie,"\nChcesz policzyc swoje BMI?(t/n)")
zgoda=input()
if zgoda=="t":
	waga=int(input("No to na poczatek podaj mi swoja wage\n"))
	wzrost=float(input("Teraz czas na wzrost w metrach\n"))
	BMI=waga/(wzrost**2)
	print("Moj jakze skomplikowany kalkulator obliczyl ze twoje BMI wynosi", round(BMI,6))
	input()
else:
	print("W takim badz razie zegnaj!")