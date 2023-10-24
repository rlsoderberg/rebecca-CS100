import random

#create dictionary
roster = {}
#create list of names
names = ['abner', 'benjamin', 'caleb', 'daniel', 'eli', 'fineas']

class Student():
    def __init__(self, ID, n):
        self.ID = ID
        self.n = n

#for loop assigning key & value to dictionary items... key is id, and value is n
for n in range (0, len(names)):
    #generate random ID
    ID = random.randrange(0,10000)
    roster[ID] = Student(ID, n)

#print roster IDs
print('here are the student IDs in your roster:')
for s in roster:
    print(s)

#initialize ID entry
i = 0
#ask user which student they would like to view
while i != 'x':
    i = input('which student would you like to view? enter ID, or press x to exit: ')
    if i != 'x':
        print('student ' + str(i) + ": " + names[roster[int(i)].n])




    

