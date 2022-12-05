import threading
import turtle
import time
from functools import partial
screen_width = 600
screen_height = 500

def sound():
	from playsound import playsound
	playsound('klaxon.wav')

def test2(name):
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

        def update(self):
            if time.time() - self.blink_timer > 0.5:
                self.blink_timer = time.time()
                self.is_cursor_visible = not self.is_cursor_visible

        def draw(self):
            self.pen.clear()
            self.active
            if self.is_cursor_visible:
                text = name
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

if __name__ =="__main__":
    answer = input("what is your favorite animal?")
    list = ["cat", "dog", "bird", "fish"]
    if answer in list:         
        t1 = threading.Thread(target=sound)
        t2 = threading.Thread(target=test2, args=(answer,))
    
        t1.start()
        t2.start()
    
        t1.join()
        t2.join()
    elif (answer not in list) and (answer != "capybara"):
        print("incorrect, try again")
    elif answer == "capybara":
        print("that is correct")