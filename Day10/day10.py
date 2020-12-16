#Part 1

f = open("text.txt", "r")
mylist = []

for x in f:
	mylist.append(int(x))

mylist.sort()

c1 = 1
c2 = 1
for x in range(0, len(mylist)-1):
	if mylist[x+1]-mylist[x] == 1:
		c1+=1
	elif mylist[x+1]-mylist[x] == 3:
		c2+=1
print(c1*c2)

#Answer is 2484
#----------------------
#Part 2
combo = 1
lenOf1 = 1
last = 1

def mult(n) : 
    if (n == 0 or n == 1 or n == 2) : 
        return 0
    elif (n == 3) : 
        return 1
    else : 
        return (mult(n - 1) + 
                mult(n - 2) +
                mult(n - 3)) 
          

		
	
def multfrom2(l):
	return mult(l)+mult(l-1)

for x in range(0, len(mylist)-1):
	if mylist[x+1]-mylist[x] == 1:
		lenOf1+=1	
		last = 1
	elif mylist[x+1]-mylist[x] == 2 :
		if last == 1:
			combo*=(multfrom2(lenOf1+2)+multfrom2(lenOf1+1)+multfrom2(lenOf1+0))
		lenOf1=0
		last = 2
	else:
		if lenOf1>0:
			combo *= (mult(lenOf1+2)+mult(lenOf1+1)+mult(lenOf1+0))
		lenOf1=0
		last = 3
combo *= (mult(lenOf1+2)+mult(lenOf1+1)+mult(lenOf1+0))
print(combo)	
#Answer is 15790581481472

