import random
def again(nextGame):
	if nextGame == "t":
		nextGame = "n"
		game()
def guess(number,attempt,maxNumber,advice="None"):
	if int(attempt) == 0:
		number = number/2
	else:
		if advice==1:
			number = random.randint(number,maxNumber)
		else:
			number = random.randint(1,number)
	return number
def game():
	attempt = 0
	maxNumber = int(input("Od 1 do ilu mam zgadywac liczbe?\n"))
	userAnswer = 0
	answer = guess(maxNumber,attempt,maxNumber)
	while userAnswer!=3:
		print("Czy liczba o jakiej myslicz to {}?".format(answer))
		print("*"*10,"Wybierz opcje","*"*10)
		print("1. Jest wieksza")
		print("2. Jest mniejsza")
		print("3. Wlasnie o ta liczbe mi chodzilo :D")
		print("*"*25)
		userAnswer=int(input())
		attempt+=1
		if userAnswer==3:
			print("Super udalo mi sie zgadnac za {} proba".format(attempt))
		else:
			answer = guess(answer,attempt,maxNumber,userAnswer)
	nextGame = input("Czy chcesz zagrac jeszcze raz?(t/n)")
	again(nextGame)
game()