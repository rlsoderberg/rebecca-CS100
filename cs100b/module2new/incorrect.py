#oooops, see, i come back after weeks and i'm like, ohhh not only have i been slacking, i also need to do examples and typing
#therefore i need to make up for it by doing all the things i don't know how to do
#so here i am trying to do all the things, and make an incorrect sound like in QI
#doesn't work, breaks after second 'incorrect answer'
#oh well!!! i will leave it i guess

import winsound
import turtle
import time
from functools import partial
import keyboard

screen_width = 600
screen_height = 500

screen = turtle.Screen()
screen.setup(screen_width, screen_height)
screen.tracer(0)
screen.title('Incorrect')
screen.bgcolor('#111111')
#make window
class TextBox:
    def __init__(self, x=-150, y=75, w=300, h=50, drawing_pen: turtle.Turtle = None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        winsound.PlaySound('klaxon.wav', winsound.SND_ASYNC)
        if drawing_pen is not None:
            self.pen = drawing_pen
        else:
            self.pen = turtle.Turtle()
            self.pen.hideturtle()
            self.pen.penup()
            self.pen.color('white')
        self.text = ''
        self.text_size = int(self.h * 0.4)
        self.blink_timer = time.time()
        self.is_cursor_visible = True
        self.active = False

    def change_active_state(self, x, y):
        self.active = True
#timer??? time is weird and i don't really get time
    def update(self):
        if time.time() - self.blink_timer > 0.5:
            self.blink_timer = time.time()
            self.is_cursor_visible = not self.is_cursor_visible
#drawing the two bloops
    def draw(self, answer):
        self.pen.clear()
        self.active
        if self.is_cursor_visible:
            text = ""
        else:
            text = answer
        self.pen.penup()
        self.pen.write(text, align='center', font=('consolas', self.text_size, 'normal'))
#here is where the action happens
def drawstuff(answer):
    text_box = TextBox()
    #to make it a little less awkward, i cut it off at 4 seconds
    timeout = time.time() + 4
    while True:
        text_box.update()
        text_box.draw(answer)
        screen.update()
        #what the heck is time sleep doing? it seems to be important
        time.sleep(0.01)
        #i found some code to stop the loop and close the turtle window, and it kind of works
        test = 0
        if test == 5 or time.time() > timeout:
            break
        test = test - 1