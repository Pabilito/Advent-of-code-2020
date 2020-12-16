#Part 1

f = open("text.txt", "r")
mylist = []

for x in f:
	a=x.split(" ")
	for y in a:
		mylist.append(y)
	mylist.append(False)	

mylistcopy = mylist.copy()
size = len(mylist) #1773

def do_magic(it, mylist, sum, task, size):
	biggest = 0
	while True:
		if it>=size:
			return sum
		elif mylist[it+2]:
			if task == 1:
				return sum 
			else:
				return 1	
		else:
			mylist[it+2] = True
	
		if mylist[it] == "acc":
			sum+=int(mylist[it+1])
			it+=3
		elif mylist[it] == "jmp":
			it+=3*int(mylist[it+1])
		else:
			it+=3

print(do_magic(0, mylist, 0, 1, size))	
#Answer is 1420
#----------------------
#Part 2
for x in range(0, int(1773/3)):
	mylist = mylistcopy.copy()
	if mylist[3*x] == "jmp":
		mylist[3*x] = "nop"
	elif mylist[3*x] == "nop":
		mylist[3*x] = "jmp"
	sum = do_magic(0, mylist, 0, 2, size)
	if sum!=1:
		print(sum)
		break
#Answer is 1245
