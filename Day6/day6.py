#Part 1
from string import ascii_lowercase

f = open("text.txt", "r")

mylist = []
mylist2 = []
mylist3 = []

Sum = 0
Sum2 = 0
tmp = ""
i = 0

for x in f:
	mylist.append(x)

for x in mylist:
	if(x=="\n"):	
		mylist2.append(tmp)
		mylist3.append(i)
		i=0
		tmp = ""

	else:
		i+=1
		tmp+=x
		tmp = tmp.strip('\n')	


for x in mylist2:
	s=set(x)  
	l=len(s)
	Sum+=l
	for c in ascii_lowercase:
		if x.count(c) == mylist3[i]:
			Sum2+=1
	i+=1

print(Sum)

#Answer is 6775
#----------------------
#Part 2
print(Sum2)
#Answer is 3356