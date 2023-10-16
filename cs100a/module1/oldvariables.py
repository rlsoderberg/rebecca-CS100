def display_loop(action, list):
    for x in (0, len(list)):
        action(list, x)
        x=int(x)
        x+=1
    x = 0

def print_x(equations, x):
    print(f"{x}\n")

def display_equation(equations, x):
    print(f"x = {int}")
    print(f"equation {x}:")
    print(equations[x])
    print("solution:")
    print(eval(equations[x]))

rand_floats = [6.546, 77.017, 9.066]
ints = [int(rand_floats[0]), int(rand_floats[1]), int(rand_floats[2])]
equations = ["4x", "5x", "6x"]

#equations that didn't work
#equations = ["x^5", "7 % x", "x/2"]


x = 0
print("floats: ")
display_loop(print_x, rand_floats)


print("modified ints: ")
display_loop(print_x, ints)

print("equations: ")
display_loop(display_equation, equations)





