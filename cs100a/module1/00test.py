import random 

#begin with scores
userscore = 0
compscore = 0

#introduce program
print('The Rock Paper Scissors Championship')
print('User VS. Computer')
print('7 Rounds, One Winner')
begin = input('Ready to begin? ')

#counting up to 7 in two parts!!!
while userscore < 4 and compscore < 4:
    print(f'User Score: {userscore} -- Computer Score: {compscore}')
    #what, you only play if there's a tie? i don't get this
    """
    tie = True
    while tie == True:
    """
    #get user and computer moves
    valid = False
    while valid == False:
        try:
            usermove = int(input('rock (1), paper(2), or scissors(3)? '))
            if usermove == "":
                raise ValueError('empty input')
            valid = True
        except ValueError:
            print('invalid input')
    
    compmove = random.randrange(1, 3)
    moves = [0, 'rock', 'paper', 'scissors']

    #calculate winner
    #oh!!! now, putting all the possible combinations on one line, that is the way to do it!
    #and with all that room, we can combine with the next chunk down
    win = ''
    if (usermove == 1 and compmove == 3) or (usermove == 2 and compmove == 1) or (usermove == 3 and compmove == 2):
        win = 'u'
        print(f'user({moves[usermove]}) defeats computer({moves[compmove]})')
        userscore += 1
    #oh, remember to make this elif, not if, or else it messes it up!
    elif usermove == compmove:
        win = 't'
        print(f'user({moves[usermove]}) ties with computer({moves[compmove]})')
    else:
        win = 'c'
        print(f'user({moves[usermove]}) is defeated by computer({moves[compmove]})')
        compscore += 1

#print final score
print('FINAL SCORE:')
print(f'User: {userscore} -- Computer: {compscore}')

if userscore > compscore:
    print('User wins!')
else:
    print('Compuer wins!')
