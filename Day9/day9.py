#Part 1

def find_pair(it, mylist):
	for y in range(it-25, it):
		for z in range(y+1,it):
			if mylist[z]+mylist[y] == mylist[it]:
				return True
	return False

f = open("text.txt", "r")
mylist = []
i = 0

for x in f:
	mylist.append(int(x))

l = int(len(mylist)) #1000

t2 = 0
	
for x in range (0,l):
	if i>=25: 
		if not find_pair(i, mylist):
			t2 = mylist[i]
			print(t2)
			break
	i+=1

#Answer is 25918798
#----------------------
#Part 2
def find_sum(min, max, lista):
	val_min = lista[min]
	val_max = lista[min]
	for x in range(min+1, max+1):
		if(lista[x]>val_max):
			val_max = lista[x]
		elif(val_min>lista[x]):
			val_min = lista[x]	
	return val_min+val_max

for x in range (0,mylist.index(t2)):
	sum=0
	i=x
	while sum<t2:
		i+=1
		sum+=mylist[i]
	if sum==t2:
		min = x+1
		max = i
		print(find_sum(min,max, mylist))
		break

#Answer is 3340942

