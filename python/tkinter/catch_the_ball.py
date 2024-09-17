import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Catch the Ball")
root.resizable(False, False)

# Create canvas
canvas_width = 400
canvas_height = 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Create paddle
paddle_width = 80
paddle_height = 10
paddle_speed = 20
paddle = canvas.create_rectangle(0, canvas_height - paddle_height, paddle_width, canvas_height, fill='blue')

# Ball settings
ball_size = 10
ball_speed = 5

# Create balls
balls = []
ball_directions = []
for _ in range(3):
    ball = canvas.create_oval(0, 0, ball_size, ball_size, fill='red')
    ball_dx = random.choice([-ball_speed, ball_speed])
    ball_dy = ball_speed
    balls.append(ball)
    ball_directions.append((ball_dx, ball_dy))

# Scoring and game state
score = 0
missed = 0
max_missed = 5

# Create score text
score_text = canvas.create_text(10, 10, anchor='nw', text=f'Score: {score}', font=('Arial', 14))
missed_text = canvas.create_text(10, 30, anchor='nw', text=f'Missed: {missed}', font=('Arial', 14))

# Paddle movement
def move_paddle(event):
    paddle_pos = canvas.coords(paddle)
    if event.keysym == 'Left' and paddle_pos[0] > 0:
        canvas.move(paddle, -paddle_speed, 0)
    elif event.keysym == 'Right' and paddle_pos[2] < canvas_width:
        canvas.move(paddle, paddle_speed, 0)

root.bind('<Left>', move_paddle)
root.bind('<Right>', move_paddle)

# Ball movement and collision detection
def move_balls():
    global score, missed
    for i, ball in enumerate(balls):
        ball_dx, ball_dy = ball_directions[i]
        canvas.move(ball, ball_dx, ball_dy)
        ball_pos = canvas.coords(ball)
        paddle_pos = canvas.coords(paddle)

        # Ball hits side walls
        if ball_pos[0] <= 0 or ball_pos[2] >= canvas_width:
            ball_directions[i] = (-ball_dx, ball_dy)

        # Ball hits top wall
        if ball_pos[1] <= 0:
            ball_directions[i] = (ball_dx, -ball_dy)

        # Ball hits paddle
        if (paddle_pos[1] <= ball_pos[3] <= paddle_pos[1] + 5) and (paddle_pos[0] <= ball_pos[2] and paddle_pos[2] >= ball_pos[0]):
            ball_directions[i] = (ball_dx, -ball_dy)
            score += 1
            canvas.itemconfig(score_text, text=f'Score: {score}')

        # Ball falls down
        if ball_pos[3] >= canvas_height:
            missed += 1
            canvas.itemconfig(missed_text, text=f'Missed: {missed}')
            if missed >= max_missed:
                game_over()
                return
            else:
                reset_ball(i)

    root.after(50, move_balls)

# Reset ball after falling
def reset_ball(index):
    x = random.randint(0, canvas_width - ball_size)
    y = 0
    canvas.coords(balls[index], x, y, x + ball_size, y + ball_size)
    ball_dx = random.choice([-ball_speed, ball_speed])
    ball_dy = ball_speed
    ball_directions[index] = (ball_dx, ball_dy)

# Game over
def game_over():
    canvas.create_text(canvas_width / 2, canvas_height / 2, text="Game Over", font=('Arial', 24), fill='red')
    canvas.after(2000, root.destroy)

# Start ball movement
move_balls()

# Start the tkinter main loop
root.mainloop()