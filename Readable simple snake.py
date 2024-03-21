import random, keyboard, time

heading = [1,0]
appleCords = [5,5]
Snake = [[1,1],[1,1]]

while True:
    if heading != [0,1] and keyboard.is_pressed('Up'):
        heading = [0,-1]

    elif heading != [-1,0] and keyboard.is_pressed('Right'):
        heading = [1,0]

    elif heading != [0,-1] and keyboard.is_pressed('Down'):
        heading = [0,1]

    elif heading != [1,0] and  keyboard.is_pressed('Left'):
        heading = [-1,0]

    if Snake[0][0]+heading[0] != 10 and Snake[0][0]+heading[0] != -1 and Snake[0][1]+heading[1] != 10 and Snake[0][1]+heading[1] != -1:
        Snake[0] = [Snake[0][0] + heading[0], Snake[0][1] + heading[1]] 

    if Snake[0] in Snake[1:len(Snake)]:
        Snake = [Snake[0],Snake[1]]

    if Snake[0] == appleCords:
        Snake.insert(0,list(Snake[0]))

    else:
        Snake.pop(len(Snake) - 1)
        Snake.insert(1,list(Snake[0]))

    while appleCords in Snake: 
        if len(Snake) == 101:
            appleCords = [-1,-1] 

        else:
            appleCords = [random.randint(0,9),random.randint(0,9)]
        
    screen = ""

    for pos in range(100):
        if [pos % 10,(pos-(pos % 10))/10] in Snake:
            screen+="⬜"

        elif appleCords==[(pos % 10),(pos-(pos % 10))/10]:
            screen+="🍎"

        else:
            screen+="⬛"

        if pos % 10 == 9:
            screen+="\n"

    if keyboard.is_pressed('x'):
        exit()
    
    print(screen, end = "\r")
    time.sleep(0.175)