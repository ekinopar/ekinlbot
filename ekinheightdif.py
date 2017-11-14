height = [ [0,1,1,0],[0,1,1,0], 
       [0,1,1,0], [0,1,1,0],
       [0,1,1,0] ] 

isBlue = [ [False,False,False,False], [False,False,False,False], 
        [False,False,False,False], [False,False,False,False],
        [False,False,False,True] ] 

isOn = [ [False,False,False,False], [False,False,False,False], 
        [False,False,False,False], [False,False,False,False],
        [False,False,False,True] ] 

# start by initializing the lightbot status variables
x = 0 # position x-coordinate
y = 0 # position y-coordinate
yon = 0 #which way our lbot is facing
direction = { 0:'north', 1:'east', 2:'south', 3:'west' }

maxX = len(height)-1 # max possible value of the x coordinate
maxY = len(height[0])-1 # max possible value of the y coordinate

komut = " " 
while komut != "q":
    print("Enter a command for lbot")
    komut = input()
    if komut=='<':
        print("I am turning left")
        yon = (yon-1)%4
    elif komut==">":
        print("I am turning right")
        yon = (yon+1)%4
    elif komut=="@":
        if ( isBlue[x][y] == True ): 
            print("I am switching on or off")
        
            if ( isOn[x][y] == True ):
                 isOn[x][y] = False 
            else:
                 isOn[x][y] = True 
        else:
             print("You are trying to light up a gray box.I can't do it")
            
    elif komut=="^": 
        if yon == 0:
            if y < maxY:
                y = y + 1
        if yon == 1:
            if  x < maxX:
                 x = x + 1
        if yon == 2:
            if y>0:
                y = y - 1 
        if yon == 3: 
            if x>0:
                x = x - 1 
    def heightDifferenceForward():
    if yon == 0 and y<maxY:
        return height[x][y+1] - height[x][y] 
     if yon == 1 and x<maxX:
        return height[x+1][y] - height[x][y] 
     if yon == 2 and y>0:
        return height[x][y-1] - height[x][y] 
     if yon == 3 and x>0:
        return height[x-1][y] - height[x][y] 
     return 0
    
    elif komut != "q":
        print("This command is not known")
print("As I exit now, my orientation is " , direction[yon])


