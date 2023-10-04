#it's really not liking what i'm doing with numbers here. i'm trying to make it simpler and simpler...

def display_loop(action, equations, x):
    for x in equations:
        action(equations, x)
        x=int(x)
        x+=1

#do i need to worry about unused arguments here?
def print_x(equations, x):
    print(f"x\n")

def display_equation(equations, x):
    print(f"x = {int}")
    print(f"equation {x}:")
    print(equations[x])
    print("solution:")
    print(eval(equations[x]))

rand_floats = [6.546, 77.017, 9.066]
equations = ["x^5", "2 % x", "x/2"]

ints = [int(rand_floats[0]), int(rand_floats[1]), int(rand_floats[2])]

x=0
print("modified ints: ")
display_loop(print_x, equations, x)
x=0
print("equations: ")
display_loop(display_equation, equations, x)





