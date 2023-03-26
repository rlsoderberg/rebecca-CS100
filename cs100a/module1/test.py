import sys
sys.path.append('../..')

from i import input_function

import random
from sympy import symbols, Eq, solve

prob_num = 0
abc = []
#is there a better way to do this than sympy?????
prob_strings = ["2*x + yz = ","z - y - x = ","x * y * z","(x+y)/z","(y-z)%x","x**z+y**z"]
x, y, z = symbols('x y z')
prob_eqs = [(x + y + x),(z - y - x),(x * y * z),((x+y)/z),((y-z)%x),(x**z+y**z)]
op_names = ["Addition", "Subtraction","Multiplication","Division","Modulo","Exponent"]
total_questions = 6 

expr = prob_eqs[prob_num]
x, y, z = symbols('x y z')
solution = expr.subs(x, 1).subs(y, 1).subs(z,1)


print("Problem "+str(prob_num + 1)+": "+op_names[prob_num])
print(str(prob_strings[prob_num]) + " = "+ str(solution))