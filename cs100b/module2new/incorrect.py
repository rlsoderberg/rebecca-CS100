import turtle
import time
from functools import partial
import winsound
#this is the only sound player that i can get to work!!! what the heck is wrong with my files!!!
winsound.PlaySound('C:/Windows/Media/notify.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
#i hacked up this nice code 
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

    def add_letter(self, letter: str):
        if not self.active:
            return
        if len(self.text) <= self.w // self.text_size:
            self.text += letter

    def remove_letter(self):
        if not self.active:
            return
        self.text = self.text[0: -1]

    def change_active_state(self, x, y):
        self.active = False
        if self.x <= x <= self.x + self.w:
            if self.y - self.h <= y <= self.y:
                self.active = True
                return

    def update(self):
        if time.time() - self.blink_timer > 0.5:
            self.blink_timer = time.time()
            self.is_cursor_visible = not self.is_cursor_visible

    def draw(self):
        self.pen.clear()
        self.active
        if self.is_cursor_visible:
            text = "apple"
        else:
            text = self.text + ' '
        self.pen.penup()
        self.pen.goto(self.x + self.w // 2, self.y - self.h * 0.85)
        self.pen.write(text, align='center', font=('consolas', self.text_size, 'normal'))


text_box = TextBox()


while True:
    text_box.update()
    text_box.draw()
    screen.update()
    time.sleep(0.01)