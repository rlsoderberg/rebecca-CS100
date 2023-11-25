import random 

#start game loop
stop = 0
while stop == 0:
    #get user and computer moves
    usermove = int(input('rock (1), paper(2), or scissors(3)? '))
    compmove = random.randrange(1, 4)
    moves = [0, 'rock', 'paper', 'scissors']

    #calculate winner
    win = ''
    if usermove == 1:
        if compmove == 3:
            win = 'u'
        elif compmove == 2:
            win = 'c'
        elif compmove == 1:
            win = 't'
    elif usermove == 2:
        if compmove == 3:
            win = 'c'
        elif compmove == 2:
            win = 't'
        elif compmove == 1:
            win = 'u'
    elif usermove == 3:
        if compmove == 3:
            win = 't'
        elif compmove == 2:
            win = 'u'
        elif compmove == 1:
            win = 'c'

    #show results
    if win == 'u': 
        print(f'user({moves[usermove]}) defeats computer({moves[compmove]})')
    elif win == 'c':
        print(f'user({moves[usermove]}) is defeated by computer({moves[compmove]})')
    elif win == 't':
        print(f'user({moves[usermove]}) ties with computer({moves[compmove]})')

    #get user input to repeat/exit
    valid = False
    while valid == False:
        try:
            stop = int(input('press 1 to stop, or 0 to continue: '))
            if stop == "":
                raise ValueError('empty input')
            if stop > 1: 
                raise ValueError('input out of range')
            valid=True
        except ValueError:
            print('invalid input! ')