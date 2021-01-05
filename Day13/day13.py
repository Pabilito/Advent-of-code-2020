#Part 1
import re

f = open("text.txt", "r")

num = int(f.readline())
line2 = f.readline()
line2t1 = (re.findall('([0-9]+)', line2))

waitTime = 1000
winner = 0

for x in line2t1:
    time = int(x)-num%int(x)
    if  time < waitTime:
        waitTime = time
        winner = int(x)
    
print(waitTime*winner)
#Answer is 246
#----------------------
#Part 2
line2t2 =(re.findall('([0-9]+|x)', line2))

coefficient = int(line2t2[0])
finish = True
value = 939490236001475
#brute force, I overestimated power of my computer
while True:
    i=0
    value-=coefficient
    finish = True
    for x in line2t2:
        if x!="x":
            if (value+i)%int(x) != 0:
                finish = False
                continue
        i+=1
    if finish:         
        break

value = 0
myarr = []
i=0
N=1
#bi is myarr[?][1]
for x in line2t2:
    if x!="x":
        myarr.append([int(x),i%int(x)])
        N*=int(x)
    i+=1

Ni=[]
xi=[]
for x in myarr:
    Ni.append(N/x[0])
    for y in range(1, x[0]):
        if 1 == (y*N/x[0])%x[0]:
            xi.append(y)

for x in range(0, len(Ni)):
    value+=Ni[x]*xi[x]*myarr[x][1]

value = value%N

#print(myarr, N, Ni, xi, value)
print(int(N-value))
#too high 939490236001475
#too low  839490236001475

#Answer is 
