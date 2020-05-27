"""
File: brickbreaker.py
----------------
YOUR DESCRIPTION HERE
"""

from tkinter import *
import time
import random
import os

# How big is the playing area?
CANVAS_WIDTH = 600  # Width of drawing canvas in pixels
CANVAS_HEIGHT = 700  # Height of drawing canvas in pixels

# Constants for the bricks
N_ROWS = 10  # How many rows of bricks are there?
N_COLS = 10  # How many columns of bricks are there?
SPACING = 5  # How much space is there between each brick?
BRICK_START_Y = 50  # The y coordinate of the top-most brick
BRICK_HEIGHT = 20  # How many pixels high is each brick
BRICK_WIDTH = (CANVAS_WIDTH - (N_COLS + 1) * SPACING) / N_COLS
SIZE = CANVAS_HEIGHT / N_ROWS - 1

# Constants for the ball and paddle
BALL_SIZE = 40
PADDLE_Y = CANVAS_HEIGHT - 80
PADDLE_WIDTH = 90
COUNT = 0


def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Brick Breaker')

    for row in range(N_ROWS):
        for col in range(N_COLS):
            x = (col) * 60
            y = (row + 5) * 13

            color = get_color(row, col)
            canvas.create_rectangle(x, y, x + 55, y + 7, fill=color, tags='brick')

    # button image
    img=PhotoImage(file=r"button.png")
    img1=img.subsample(8,7)

    paddle = canvas.create_rectangle(0, PADDLE_Y, PADDLE_WIDTH, CANVAS_HEIGHT - 70, tag="brick", fill='#ccb808')
    ball = canvas.create_oval(CANVAS_WIDTH / 2, 270, 330, 300, fill="#e8910e", outline="#e8910e")

    dx = 10
    dy = 7
    while True:
        mouse_x = canvas.winfo_pointerx()
        canvas.moveto(paddle, mouse_x, PADDLE_Y)
        canvas.move(ball, dx, dy)
        if hit_left_x(canvas, ball) or hit_right_x(canvas, ball):
            dx *= -1
        if hit_top_y(canvas, ball):  # hit_bottom_paddle(canvas,paddle)
            dy *= -1
        if ball_coll(canvas, ball, paddle) == 1:
            dy *= -1
        if canvas.coords(ball)[1] > 610:
            canvas.create_text(40, 400, anchor='w', font='trashco 82', text='Game Over!', fill='red')
            restart=Button(canvas,text="restart",padx=30,pady=5,command=restart_program)
            restart.config(image=img1,background='#022e15',activebackground='#022e15')
            restart.place(x=270,y=500)


        canvas.update()

        time.sleep(1 / 50.)



def ball_coll(canvas, ball, paddle):
    global COUNT
    ball_coords = canvas.coords(ball)
    x1 = ball_coords[0]
    y1 = ball_coords[1]
    x2 = ball_coords[2]
    y2 = ball_coords[3]
    colliding_list = canvas.find_overlapping(x1, y1, x2, y2)
    for object in colliding_list:
        if object == paddle or object == ball:
            return len(colliding_list) > 1

        else:
            canvas.delete(object)
            COUNT = COUNT + 1

            canvas.create_text(0, 20, anchor='w', font='Courier 22', tag='score', text='Score={}'.format(COUNT))
            canvas.delete("score")
            canvas.create_text(0, 20, anchor='w', font='URW_Chancery_L 22', tag='score', fill='yellow',text='Score={}'.format(COUNT))



def hit_left_x(canvas, ball):
    return get_left_x(canvas, ball) <= 0


def hit_right_x(canvas, ball):
    return get_right_x(canvas, ball) >= CANVAS_WIDTH


def hit_top_y(canvas, ball):
    return get_top_y(canvas, ball) <= 0


def get_left_x(canvas, object):
    return canvas.coords(object)[0]


def get_top_y(canvas, object):
    return canvas.coords(object)[1]


def get_right_x(canvas, object):
    return canvas.coords(object)[2]


def get_bottom_y(canvas, object):
    return canvas.coords(object)[3]


def get_color(row, col):
    # super slick trick
    if row <= 1:
        return 'red'
    if row <= 3:
        return '#ff9900'
    if row <= 5:
        return '#ffce08'
    if row <= 7:
        return '#0feb07'
    if row <= 9:
        return '#07d1fa'
    # color = random.choice(['blue', 'salmon', 'red', 'orange', 'plum','black'])
    # return color
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def make_canvas(width, height, title):
    """

    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    root = Tk()
    root.minsize(width=width, height=height)
    root.title(title)

    canvas = Canvas(root, width=width + 1, height=height + 1, bg='#022e15')


    canvas.pack()


    return canvas


if __name__ == '__main__':
    main()
