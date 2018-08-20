import random
def again(nextGame):
	if nextGame=="t":
		nextGame="n"
		game()
def game():
	x=int(input("Od 1 do ilu chcesz zgadywac liczbe?\n"))
	attempt=0
	number=random.randint(1,x)
	answer=int(input("O jakiej mysle liczbie?\n"))
	while number!=answer:
		attempt+=1
		if answer>number:
			answer=int(input("Liczba o ktorej mysle jest mniejsza\n"))
		else:
			answer=int(input("Liczba o ktorej mysle jest wieksza\n"))
	else:
		attempt+=1
		print("Gratulacje chodzilo wlasnie o {}\n Udalo Ci sie odgadnac za {} razem!".format(number,attempt))
	nextGame=input("Czy chcesz zagrac jeszcze raz?(t/n)")
	again(nextGame)
game()
