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

    def update(self):
        if time.time() - self.blink_timer > 0.5:
            self.blink_timer = time.time()
            self.is_cursor_visible = not self.is_cursor_visible

    def draw(self, answer):
        self.pen.clear()
        self.active
        if self.is_cursor_visible:
            text = ""
        else:
            text = answer
        self.pen.penup()
        self.pen.write(text, align='center', font=('consolas', self.text_size, 'normal'))

def drawstuff(answer):
    text_box = TextBox()
    timeout = time.time() + 4
    while True:
        text_box.update()
        text_box.draw(answer)
        screen.update()
        time.sleep(0.01)
        test = 0
        if test == 5 or time.time() > timeout:
            break
        test = test - 1
    

