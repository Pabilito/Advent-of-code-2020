#Part 1
import re 
dire = 1 #0,1,2,3 -> N,E,S,W

def rotate(initial, rotations, clockwise):                      
        if clockwise: #right
                return (initial+rotations)%4
        return (initial-rotations)%4

PosX=0
PosY=0

# N
#W E
# S

f = open("text.txt", "r")
mylist = []

for x in f:
        res = re.findall('([A-Z]+)([0-9]+)', x)
        mylist.append(res)

for x in mylist:
        if x[0][0] == "F":
                if dire == 0:
                        PosY+=int(x[0][1])        
                elif dire == 1:
                        PosX+=int(x[0][1])
                elif dire == 2:
                        PosY-=int(x[0][1])
                else:
                        PosX-=int(x[0][1])
        elif x[0][0] == "L":
                swaps = (int(x[0][1])%360)/90        
                dire = rotate(dire, swaps, False)        
        elif x[0][0] == "R":
                swaps = (int(x[0][1])%360)/90 
                dire = rotate(dire, swaps, True)          
        elif x[0][0] == "N":
                PosY+=int(x[0][1])                      
        elif x[0][0] == "E":
                PosX+=int(x[0][1])          
        elif x[0][0] == "S":
                PosY-=int(x[0][1])        
        else:
                PosX-=int(x[0][1])
                        


print(abs(PosX)+abs(PosY))
#Answer is 1838
#----------------------
#Part 2

#Answer is 
