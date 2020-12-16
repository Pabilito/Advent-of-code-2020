#Part 1
import copy

def noAdjecent(x,y,lista):
        lenx = len(lista)
        leny = len(lista[0]) - 1
        if x!=0:
                if lista[x-1][y] == "#": #left                       
                        return False
        if y!=0:
                if lista[x][y-1] == "#": #top
                        return False
        if x!=lenx-1:
               if lista[x+1][y] == "#": #right
                        return False
        if y!=leny-1:
                if lista[x][y+1] == "#": #bottom
                        return False 
        if x!=0 and y!=0: #top left
                if lista[x-1][y-1] == "#":
                        return False
        if x!=0 and y!=leny-1: #top right
                if lista[x-1][y+1] == "#":
                        return False
        if x!=lenx-1 and y!=0: #bottom left
                if lista[x+1][y-1] == "#":
                        return False
        if x!=lenx-1 and y!=leny-1: #bottom right
                if lista[x+1][y+1] == "#":
                        return False
        return True


def FourOrMoreOccupied(x,y,lista):
        suma = 0
        lenx = len(lista)
        leny = len(lista[0]) - 1
        if x!=0:
                if lista[x-1][y] == "#": #left
                        suma+=1
        if y!=0:
                if lista[x][y-1] == "#": #top
                        suma+=1
        if x!=lenx-1:
               if lista[x+1][y] == "#": #right
                        suma+=1
        if y!=leny-1:
                if lista[x][y+1] == "#": #bottom
                        suma+=1
        if x!=0 and y!=0: #top left
                if lista[x-1][y-1] == "#":
                        suma+=1
        if x!=0 and y!=leny-1: #top right
                if lista[x-1][y+1] == "#":
                        suma+=1
        if x!=lenx-1 and y!=0: #bottom left
                if lista[x+1][y-1] == "#":
                        suma+=1
        if x!=lenx-1 and y!=leny-1: #bottom right
                if lista[x+1][y+1] == "#":
                        suma+=1
        return suma>=4        
        
def shuffle(lista, copied):      
        changesMade = False;
        i = 0
        j = 0
        for x in lista:
                for y in x:
                        if y=="L" and noAdjecent(i,j, copied):
                                lista[i][j] = "#"
                                changesMade = True
                        elif y=="#" and FourOrMoreOccupied(i,j,copied):
                                lista[i][j] = "L"
                                changesMade = True
                        j+=1
                i+=1
                j=0
        return changesMade    

#------

f = open("text.txt", "r")
mylist = []

for x in f:
        a = list(x)
        mylist.append(a)
        
copied = copy.deepcopy(mylist)

finished = True

#Uncomment to do task 1
#while finished:
#        copied = copy.deepcopy(mylist)
#        finished = shuffle(mylist, copied)
#        #print(mylist, finished)
#
solutionA = 0
for x in mylist:
                for y in x:
                        if(y=="#"):
                                solutionA+=1
print(solutionA)
#Answer is 2494
#----------------------
#Part 2

def noAdjecentv2(x,y,lista):
        lenx = len(lista)
        leny = len(lista[0]) - 1
        xcopy = x
        ycopy = y
        
        while x!=0:
                x-=1
                if lista[x][y] == "#": #left                       
                        return False
                if lista[x][y] == "L":                     
                        break
        x = xcopy
        while y!=0:
                y-=1
                if lista[x][y] == "#": #left                       
                        return False
                if lista[x][y] == "L":                       
                        break
        y = ycopy       
        while x!=lenx-1:
                x+=1
                if lista[x][y] == "#": #right
                        return False
                if lista[x][y] == "L":                      
                        break
        x = xcopy       
        while y!=leny-1:
                y+=1
                if lista[x][y] == "#": #bottom
                        return False
                if lista[x][y] == "L":                       
                        break
        y = ycopy        
        while x!=0 and y!=0: #top left
                x-=1
                y-=1
                if lista[x][y] == "#":
                        return False
                if lista[x][y] == "L":                       
                        break
        y = ycopy
        x = xcopy
        while x!=0 and y!=leny-1: #top right
                x-=1
                y+=1
                if lista[x][y] == "#":
                        return False
                if lista[x][y] == "L":                       
                        break          
        y = ycopy
        x = xcopy
        while x!=lenx-1 and y!=0: #bottom left
                x+=1
                y-=1
                if lista[x][y] == "#":
                        return False
                if lista[x][y] == "L":                       
                        break
        y = ycopy
        x = xcopy
        while x!=lenx-1 and y!=leny-1: #bottom right
                x+=1
                y+=1
                if lista[x][y] == "#":
                        return False
                if lista[x][y] == "L":                       
                        break
        return True

def FiveOrMoreOccupied(x,y,lista):
        suma = 0
        lenx = len(lista)
        leny = len(lista[0]) - 1
        xcopy = x
        ycopy = y
        
        while x!=0:
                x-=1
                if lista[x][y] == "#": #left                       
                        suma+=1
                        break
                if lista[x][y] == "L":                     
                        break
        x = xcopy
        while y!=0:
                y-=1
                if lista[x][y] == "#": #left                       
                        suma+=1
                        break
                if lista[x][y] == "L":                       
                        break
        y = ycopy       
        while x!=lenx-1:
                x+=1
                if lista[x][y] == "#": #right
                        suma+=1
                        break
                if lista[x][y] == "L":                      
                        break
        x = xcopy       
        while y!=leny-1:
                y+=1
                if lista[x][y] == "#": #bottom
                        suma+=1
                        break
                if lista[x][y] == "L":                       
                        break
        y = ycopy        
        while x!=0 and y!=0: #top left
                x-=1
                y-=1
                if lista[x][y] == "#":
                        suma+=1
                        break
                if lista[x][y] == "L":                       
                        break
        y = ycopy
        x = xcopy
        while x!=0 and y!=leny-1: #top right
                x-=1
                y+=1
                if lista[x][y] == "#":
                        suma+=1
                        break
                if lista[x][y] == "L":                       
                        break          
        y = ycopy
        x = xcopy
        while x!=lenx-1 and y!=0: #bottom left
                x+=1
                y-=1
                if lista[x][y] == "#":
                        suma+=1
                        break
                if lista[x][y] == "L":                       
                        break
        y = ycopy
        x = xcopy
        while x!=lenx-1 and y!=leny-1: #bottom right
                x+=1
                y+=1
                if lista[x][y] == "#":
                        suma+=1
                        break
                if lista[x][y] == "L":                       
                        break
        return suma>=5 

def shufflev2(lista, copied):      
        changesMade = False;
        i = 0
        j = 0
        for x in lista:
                for y in x:
                        if y=="L" and noAdjecentv2(i,j, copied):
                                lista[i][j] = "#"
                                changesMade = True
                        elif y=="#" and FiveOrMoreOccupied(i,j,copied):
                                lista[i][j] = "L"
                                changesMade = True
                        j+=1
                i+=1
                j=0
        return changesMade    

finished = True

while finished:
        copied = copy.deepcopy(mylist)
        finished = shufflev2(mylist, copied)
        #print(mylist, finished)

solutionB = 0
for x in mylist:
                for y in x:
                        if(y=="#"):
                                solutionB+=1
print(solutionB)

#Answer is 2306
