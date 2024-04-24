from tkinter import *
import random

# constants kind of like the settings. Values we don't want to change


GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50 # lower the number the faster the game
SPACE_SIZE = 50
BODYPARTS = 3
SNAKECOLOR = "#0000FF"
FOODCOLOR = "#FF0000"
BACKGROUND = "#000000"

class Snake:
    def __init__(self):
        self.bodysize = BODYPARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODYPARTS):
            self.coordinates.append([0,0]) #snake in top right corner 

        for x, y, in self.coordinates:
            square = canvas.create_rectangle(x,y,x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKECOLOR, tag="snake")
            self.squares.append(square)
    pass
class Food:
    def __init__(self):

        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x,y]

        canvas.create_oval(x,y,x+ SPACE_SIZE, y + SPACE_SIZE, fill=FOODCOLOR, tag="food")
    pass

def nextTurn(snake, food):
    global score, direction, canvas

    x,y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x,y))

    square = canvas.create_rectangle(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKECOLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        score += 1

        label.config(text="Score:{}".format*(score))
        canvas.delete("food")

        food = Food()


    else:

        del snake.coordinates[-1] #last set of coordinates
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    window.after(SPEED, nextTurn, snake, food)

def changeDirection(newDirection):
    global direction

    if newDirection != 'left':
        if direction != 'right':
            direction = newDirection
    elif newDirection != 'right':
        if direction != 'left':
            direction = newDirection
    if newDirection != 'up':
        if direction != 'down':
            direction = newDirection
    if newDirection != 'down':
        if direction != 'up':
            direction = newDirection
    pass
def checkCollision():
    pass

def gameOver():
    pass

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = "down"

label = Label(window, text="Score:{}".format(score), font=('consolas', 14))
label.pack()

canvas = Canvas(window, bg=BACKGROUND, height=GAME_HEIGHT, width =GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width= window.winfo_screenwidth()
screen_height= window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: changeDirection('left'))
window.bind('<Right>', lambda event: changeDirection('right'))
window.bind('<Up>', lambda event: changeDirection('up'))
window.bind('<Down>', lambda event: changeDirection('down'))


snake = Snake()
food = Food()

nextTurn(snake, food)

window.mainloop()