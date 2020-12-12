#Part 1
def find_other2(string1, string2):
	for x in mylist:
		a=x.split(" ")
		if a[0] == string1 and a[1] == string2:
			return find_other(a)


def find_other(lista):
	if lista[4] == "no":
		return False
	else:
		a = len(lista)
		for y in range(1,int(a/4)):
			if lista[4*y+1] =="shiny" and lista[4*y+2] =="gold":
				return True
			else:
				if find_other2(lista[4*y+1],lista[4*y+2]):
					return True
	return False

sum = 0
f = open("text.txt", "r")

mylist = []

for x in f:
	mylist.append(x)

for x in mylist:
	a=x.split(" ")
	if find_other(a): #Uncomment to run task 1
		sum+=1

print(sum)
	
#Answer is 229
#----------------------
#Part 2
def find_sub(string1, string2):
	suma = 0
	for x in mylist:
		a=x.split(" ")
		if a[0] == string1 and a[1] == string2:
			l = len(a)
			if a[4] == "no":
				return 0
			else:
				for y in range(1,int(l/4)):
					suma+=int(a[4*y])*(1+find_sub(a[4*y+1],a[4*y+2]))
	return suma

print(find_sub("shiny", "gold"))
		

#Answer is 6683
