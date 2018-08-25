import random
maxLastAnswer = 0
minLastAnswer = 0
def again(nextGame):
	if nextGame == "t":
		nextGame = "n"
		game()
def guess(number,attempt,advice="None"):
	global maxLastAnswer
	global minLastAnswer
	if int(attempt) == 0:
		maxLastAnswer = number
		minLastAnswer = 1
		number = number/2
	else:
		if advice==1:
			if minLastAnswer<number:
				minLastAnswer = number
		else:
			if maxLastAnswer>number:
				maxLastAnswer = number
		number = random.randint(minLastAnswer,maxLastAnswer)
	return number
def game():
	attempt = 0
	maxNumber = int(input("Od 1 do ilu mam zgadywac liczbe?\n"))
	userAnswer = 0

	answer = guess(maxNumber,attempt)
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
			answer = guess(answer,attempt,userAnswer)
	nextGame = input("Czy chcesz zagrac jeszcze raz?(t/n)")
	again(nextGame)
game()
