#Part1
def find_pair(value):
  for x in mylist:
    a = value - x
    if a in mylist:
        return(a*x)
  return -1

f = open("data1.txt", "r")

mylist = []

for x in f:
    mylist.append(int(x))

mylist.sort()

print(find_pair(2020))

#Solution is: 800139

#------------------------------------------

#Part2
for x in mylist:
    val2 = find_pair(2020-x)
    if(val2 != -1):
        print(x*val2)
        break

#Solution is: 59885340
    
