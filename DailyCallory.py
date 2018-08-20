imie=input("Jak masz na imie?\n")
if imie.endswith('a'):
	S=-161
else:
	S=5
waga=int(input("Teraz pare dokladnych danych ;)\nNa poczatek waga\n"))
wzrost=int(input("Teraz wzrost(w cm)\n"))
wiek=int(input("Czas na podanie wieku\n"))
skalaAktywnosc=int(input("W skali od 1 do 5 jak aktywnie spedzasz czas?\n"))

if skalaAktywnosc==1:
	aktywnosc=1.2
elif skalaAktywnosc==2:
	aktywnosc=1.4
elif skalaAktywnosc==3:
	aktywnosc=1.6
elif skalaAktywnosc==4:
	aktywnosc=1.8
elif skalaAktywnosc==5:
	aktywnosc=2


zapotrzebowanie = aktywnosc*(10*waga+6.25*wzrost+5*wiek+S)
print("Twoje dzienne zapotrzebowanie wynosi",zapotrzebowanie,"kcal")
input()