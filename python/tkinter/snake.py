import tkinter as tk
import random

# Game settings
GAME_WIDTH = 600
GAME_HEIGHT = 400
SNAKE_SIZE = 20
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"
SNAKE_SPEED = 100  # milliseconds per move

# Global variables
score = 0
direction = "down"


# Snake class
class Snake:
    def __init__(self):
        self.body_size = 3
        self.coordinates = []
        self.squares = []

        for i in range(0, self.body_size):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


# Food class
class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SNAKE_SIZE) - 1) * SNAKE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SNAKE_SIZE) - 1) * SNAKE_SIZE

        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill=FOOD_COLOR, tag="food")


# Functions for game mechanics
def next_turn(snake, food):
    global score

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SNAKE_SIZE
    elif direction == "down":
        y += SNAKE_SIZE
    elif direction == "left":
        x -= SNAKE_SIZE
    elif direction == "right":
        x += SNAKE_SIZE

    snake.coordinates.insert(0, [x, y])

    square = canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        score += 1
        label.config(text="Score: {}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SNAKE_SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction

    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction


def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():
    canvas.delete(tk.ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")


# Main game setup
window = tk.Tk()
window.title("Snake Game")
window.resizable(False, False)

# Score label
label = tk.Label(window, text="Score: {}".format(score), font=('consolas', 40))
label.pack()

# Canvas for game window
canvas = tk.Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

# Starting position for game window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Starting snake and food
snake = Snake()
food = Food()

# Control key bindings
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

# Start the game
next_turn(snake, food)

window.mainloop()