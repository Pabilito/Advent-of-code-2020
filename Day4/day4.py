#Part 1
import re 
f = open("data4.txt", "r")

mylist = []

cid = False
prev = False
count = 0
countEntry = 0
i=0
mini = 0
maxi = 0
confirmedCount=0

def confirm(start, end):
    for x in range(start, end):
        it = -1
        a=""
        a+=mylist[x]
        a = a.replace('\n', ' ')
        res = re.findall('\d+\.\d+|\d+|\w+|[^a-zA-Z\s]', a)
        for y in res:
            it+=1
            if y == "byr":
                if int(res[it+2]) < 1920 or int(res[it+2]) > 2002:
                    return 0 #197 
            elif y=="iyr":
                if int(res[it+2]) < 2010 or int(res[it+2]) > 2020:
                    return 0 #174
            elif y=="eyr":
                if int(res[it+2]) < 2020 or int(res[it+2]) > 2030:
                    return 0 #160
            elif y=="hgt":
                if it+3>len(res)-1:
                    return 0
                elif res[it+3] != "cm" and res[it+3] != "in":
                    return 0         
                elif res[it+3] == "in" and (int(res[it+2]) < 59 or int(res[it+2]) > 76):
                    return 0
                elif res[it+3] == "cm" and (int(res[it+2]) < 150 or int(res[it+2]) > 193):
                    return 0 #154
            elif y=="hcl":
                if it+3>len(res)-1:
                    return 0
                elif res[it+2] != "#": #151
                    return 0
                #elif len(res[it+3])!=6: #(wrong format)
                    #return 0
            elif y=="ecl":
                if not(res[it+2]=="amb" or res[it+2]=="blu" or res[it+2]=="brn" or res[it+2]=="gry" or res[it+2]=="grn" or res[it+2]=="hzl" or res[it+2]=="oth"):
                    return 0 #149
            elif y=="pid":
                if not (res[it+2]).isnumeric():
                    return 0
                elif(int(res[it+2]) > 999999999):
                    return 0 #147
    return 1

    #144 is too low, 147 too high
for x in f:
    mylist.append(x)

for x in mylist:
    if x=="\n" and not prev: #empty string
        maxi=i;
        prev = True
        if countEntry == 8 or (countEntry == 7 and not cid):
            count+=1
            confirmedCount+=confirm(mini, maxi)
        cid = False
        countEntry = 0
    else:
        if(prev):
            mini = i
            prev = False
        countEntry+=(len(re.findall(":", x)))
        if len(re.findall("cid", x)):
            cid = True
    i+=1

print(count+1) #forgot to consider last one
#Answer is 247
#----------------------
#Part 2
print(confirmedCount+1) #forgot to consider last one






