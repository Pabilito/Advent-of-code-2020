#Part 1
import re 
f = open("data2.txt", "r")

mylist = []

for x in f:
    mylist.append(x)

j=0

for x in mylist:
    i=0
    res = re.findall('\d+\.\d+|\d+|\w+|[^a-zA-Z\s]', x)
    min = int(res[0])
    max = int(res[2])
    letter = res[3]
    for character in res[5]:
        if(letter == character):
            i+=1     
    if(i>=min and i<=max):
        j+=1

print(j)
#Answer is : 564
# ----------------------
#Part2

j=0

for x in mylist:
    res = re.findall('\d+\.\d+|\d+|\w+|[^a-zA-Z\s]', x)
    min = int(res[0])
    max = int(res[2])
   #if(max<=len(mylist) and min<=len(mylist)): Could be used for safety
    if(res[5][min-1] != res[3] and res[5][max-1] != res[3]):
        j+=1
    elif(res[5][min-1] == res[3] and res[5][max-1] == res[3]):
        j+=1
        
print(1000-j)
        
