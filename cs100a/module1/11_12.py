#right, i was just looking at the example for conditionals, and yeah...
#i should make sure i always convert to int as soon as i get input

#let's see how my input function is doing today
#i forgot the parentheses!!! they kind of begged to be included though
def int_input_function():
    valid = False
    while valid == False:
        try: 
            result = int(input())
            #oh i'd better put in the empty string catcher
            #oh wait, there was an error when i said 'if not result', and i made one of the variables 0
            #so i think i prefer "if result == '' "???
            if result == '':
                raise ValueError('empty string')
            valid = True
        except ValueError:
            print('Invalid Input')
    return result

print('please give me two intergers.')
print('integer one:')
int1 = int_input_function()
print('integer two:')
int2 = int_input_function()
print('and, by the way, how old are you? (whole years only please)')
age = int_input_function()

#oh right, i should also comment more
#riiight, riiight, i'll do it
#but the question is, how much do i comment?
#do i comment EVERYTHING?

#identify operation
print('\noperation 1: addition')
print('int1 + int2 =')
print(f'that is, {int1} + {int2} = \n')
#calculating answer 
sum = int1 + int2
#press any key!!! remember, it's just plain old input
print('press any key to see the solution')
input()
#using groovy f string for string interpolation and formatting!!! yesss!!!
print(f'solution: {int1} + {int2} = {sum}')
#more press any key!!!
print('press any key to see the next operation')
input()

#now do i have to do ALL of these operations? can i just skip to the division one?

#identify operation
print('\noperation 2: division')
print('int1 / int2')
print(f'that is, {int1} / {int2} = \n')
#press any key
print('press any key to see the solution')
input()
#special case if int2 = 0
#well, i'm going to see if i can catch it with a try-except with ZeroDivisionError
valid = False
while valid == False:
    try:
        quotient = int1/int2
        print(f'solution: {int1} / {int2} = {quotient}')
        valid = True
    except ZeroDivisionError:
        print("int 2 = 0, and we cannot divide by zero")
        #we are avoiding infinite loop
        #let's give them some answer, at least
        print(f'solution: {int1} / {int2} = undefined')
        valid = True

#NUMBER 12
#we are putting the user's age in some sort of category, depending how big it is
#but first, we will introduce this section, and display the user's age
print(f"now, let's see what we can calculate based on your age of {age} years...")
if age < 0:
    print('invalid age')
if age >= 16:
    print('you can drive')
#now, is elif going to work here??? because if they're over 16, then they're ALSO over 18, right?
#what even is the deal with elif???
#should i organize these if statements backwards? brb
if age >= 18:
    print('you can vote')
#or ummm, let me try just if?
#well, that worked
#doesn't it feel so weird though??? having a ton of ifs in a row???
#oh, and i am totally not commenting correctly, come on thooo
if age >= 21:
    print('you can enjoy a beer')
#i don't entirely get beer? sorry? i like cider way better
if age >= 55:
    print('you get the senior discount')
#hey, isn't that a little young for a senior discount???





