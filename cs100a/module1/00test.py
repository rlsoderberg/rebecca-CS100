#oh, i know, i need to write a mug cake program...

valid = False
while valid == False:
    try:
        mugnum = int(input('how many mugs? '))
        valid = True
    except ValueError:
        print('invalid input!')

recipe = [(1, 'tbsp', 'butter'),(2, 'tbsp', 'sugar'), 
          (3, 'tbsp', 'milk'), (2, 'tbsp', 'lemon juice'), 
          (4, 'tbsp', 'flour'), (0.5, 'tsp', 'baking soda'),
          (0.125, 'tsp', 'salt')]

for x in recipe:
    newnum = (mugnum * x[0])
    newmsr = x[1]
    if newmsr == 'tbsp':
        if newnum >= 16:
            newnum = (newnum/16)
            newmsr = 'cups'
    elif newmsr == 'tsp':
        if newnum >= 48:
            newnum = (newnum/48)
            newmsr = 'cups'
        elif newnum >= 3:
            newnum = (newnum/3)
            newmsr = 'tbsp'
    print(f'{newnum} {newmsr} {x[2]}')
