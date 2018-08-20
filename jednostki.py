cm=float(input("Podaj dlugos w cm\n"))
m=cm/100
dm=cm/10
mm=cm*10
szer=34
print("-"*szer)
print("|  Metry  | Decymetry | Milimetry |")
print("*"*szer)
print("| {:7.4f} | {:9.4f} | {:10.4f}|".format(m,dm,mm))
print("-"*szer)