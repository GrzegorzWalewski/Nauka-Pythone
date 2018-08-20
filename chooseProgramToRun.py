import os
def again(nextProgram):
	if nextProgram=="t":
		nextProgram="n"
		run_program()
def run_program():
	files=os.popen('ls').read()
	print("-"*40)
	my_list=files.split("\n")
	i=0
	lastElement=my_list[-1]
	for item in my_list:
		i+=1
		if lastElement!=item:
			print("{}{}{}".format(i,".",item))
		else:
			print("{}{}{}".format(i,".",item),end="")
	print("python3 console")
	print("*"*40)
	program=int(input("Wybierz ktory program chcesz uruchomic\n",))
	if i < program:
		print("*"*40)
		print("Program o tym numerze nie istnieje!")
		print("*"*40)
	else:
		print("*"*20,my_list[program-1],"*"*20)
		command='python3 '+my_list[program-1]
		os.system(command)
		print("*"*20,"END","*"*20)
	nextProgram=input("Czy chcesz uruchomic jeszcze jakis program?(t/n)")
	again(nextProgram)
run_program()
