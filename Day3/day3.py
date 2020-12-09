#31 symbols in each line

def go_right(coeff, step):
    count = 0
    row = 0 
    for x in mylist:
        if not(coeff/step*row).is_integer():
            row+=1
            continue
        pos = int((coeff/step*row)%31)
        if x[pos] == '#':
            count += 1   
        row += 1
    return count

#Part1

f = open("data3.txt", "r")

mylist = []

for x in f:
    mylist.append(x)
  
print(go_right(3, 1))

# Solution is: 203
# ----------------
# Part2

print(go_right(1, 1)*go_right(3, 1)*go_right(5, 1)*go_right(7, 1)*go_right(1, 2))

# Solution is: 3316272960
