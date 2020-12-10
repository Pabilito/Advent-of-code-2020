#Part 1

f = open("data5.txt", "r")

mylist = []

mylist2 = []

for x in range(0,933):
    mylist2.append(x)

max_val = 0

for x in f:
    mylist.append(x)

for x in mylist:
    rowAdd = 64
    columnAdd = 4
    row = 0
    column = 0
    for y in range(0, 7):
        if x[y]=="B":
            row +=rowAdd
        rowAdd = rowAdd/2
    for y in range(7, 10):
        if x[y]=="R":
            column +=columnAdd
        columnAdd = columnAdd/2
    #print(row, column, 8*row+column, max_val)
    current = 8*row+column
    if current in mylist2:
        mylist2.remove(current)
    if(current > max_val):
        max_val = current

print(max_val)
#Answer is 933
#----------------------
#Part 2

print(mylist2)

#Answer is 711






