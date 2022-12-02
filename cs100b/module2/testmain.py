'''
                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.
'''

from teacher import Teacher
from student import Student


def main():
    t = Teacher('smith')
    s = Student('jones')

    s.sleep()
    t.eat()
    
if __name__ == '__main__':
    main()