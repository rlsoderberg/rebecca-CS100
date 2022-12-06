import winsound
import turtle
import time
from functools import partial

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
        self.pen.goto(self.x + self.w // 2, self.y - self.h * 0.85)
        self.pen.write(text, align='center', font=('consolas', self.text_size, 'normal'))

def drawstuff(answer):
    text_box = TextBox()

    screen.onclick(text_box.change_active_state, 1)
    # adding key bindings
    # add more characters to the string to bind them as well
    for new_letter in 'abcdefghijklmnopqrstuvwxyz':
        func = partial(text_box.add_letter, new_letter)
        screen.onkeypress(func, new_letter)
        func = partial(text_box.add_letter, new_letter.upper())
        screen.onkeypress(func, new_letter.upper())
    screen.onkeypress(lambda: text_box.add_letter(' '), 'space')
    screen.onkeypress(text_box.remove_letter, 'BackSpace')
    screen.listen()

    while True:
        text_box.update()
        text_box.draw(answer)
        screen.update()
        time.sleep(0.01)

answer = "yeah we like waffles"
drawstuff(answer)
