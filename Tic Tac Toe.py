import turtle

win = turtle.Screen()
win.bgcolor("white")
win.setup(width=800, height=700)
win.tracer(0)

grid = turtle.Turtle()
grid.speed(0)
grid.color("black")
grid.pensize(5)

status = turtle.Turtle()
status.speed(0)
status.color("black")
status.penup()
status.goto(0, 300)
status.hideturtle()
status.write("Player X's Turn", align="center", font=("Courier", 22, "normal"))

reset_button = turtle.Turtle()
reset_button.speed(0)
reset_button.color("green")

reset_button.penup()
reset_button.goto(300, 320)
reset_button.write("Reset", align="center", font=("Courier", 20, "normal"))

reset_button.onclick(lambda x, y: reset_game())


def update_status(message):
    status.clear()
    status.write(message, align="center", font=("Courier", 22, "normal"))


for i in range(2):
    grid.penup()
    grid.goto(-300, 100 - (200 * i))
    grid.pendown()
    grid.forward(600)

grid.right(90)

for i in range(2):
    grid.penup()
    grid.goto(-100 + (200 * i), 300)
    grid.pendown()
    grid.forward(600)

grid.hideturtle()

player = "X"
board = [["" for _ in range(3)] for _ in range(3)]


def draw_x(x, y):
    draw = turtle.Turtle()
    draw.speed(0)
    draw.color("red")
    draw.pensize(5)

    draw.penup()
    draw.goto(x - 60, y - 60)
    draw.pendown()
    draw.goto(x + 60, y + 60)

    draw.penup()
    draw.goto(x + 60, y - 60)
    draw.pendown()
    draw.goto(x - 60, y + 60)

    draw.hideturtle()


def draw_o(x, y):
    draw = turtle.Turtle()
    draw.speed(0)
    draw.color("blue")
    draw.pensize(5)

    draw.penup()
    draw.goto(x, y - 70)
    draw.pendown()
    draw.circle(70)

    draw.hideturtle()


def check_win():
    global board
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return True

    if board[0][0] == board[1][1] == board[2][2] != "" or board[0][2] == board[1][1] == board[2][0] != "":
        return True

    return False


def check_tie():
    global board
    for row in board:
        for cell in row:
            if cell == "":
                return False

    return True


def click(x, y):
    global player
    col = int((x + 300) // 200)
    row = int((300 - y) // 200)
    if 3 > col > -1 and 3 > row > -1:
        if board[row][col] == "":
            if player == "X":
                draw_x(-200 + (col * 200), 200 - (row * 200))
                board[row][col] = "X"
                if check_win():

                    print("X wins")
                    win.onclick(None)
                    update_status("X Wins!")
                elif check_tie():
                    update_status("Its a Tie!")
                    win.onclick(None)
                else:
                    player = "O"
                    update_status("Player O's Turn")

            else:
                draw_o(-200 + (col * 200), 200 - (row * 200))
                board[row][col] = "O"
                if check_win():
                    update_status("O Wins!")
                    win.onclick(None)
                elif check_tie():
                    update_status("Its a Tie!")
                    win.onclick(None)
                else:
                    player = "X"
                    update_status("Player X's Turn")


def reset_game():
    global player, board
    player = "X"
    board = board = [["" for _ in range(3)] for _ in range(3)]
    win.clear()
    setup_game()


def setup_game():
    win = turtle.Screen()
    win.bgcolor("white")
    win.setup(width=800, height=700)
    win.tracer(0)

    grid = turtle.Turtle()
    grid.speed(0)
    grid.color("black")
    grid.pensize(5)

    for i in range(2):
        grid.penup()
        grid.goto(-300, 100 - (200 * i))
        grid.pendown()
        grid.forward(600)

    grid.right(90)

    for i in range(2):
        grid.penup()
        grid.goto(-100 + (200 * i), 300)
        grid.pendown()
        grid.forward(600)

    global status
    status = turtle.Turtle()
    status.speed(0)
    status.color("black")
    status.penup()
    status.goto(0, 300)
    status.hideturtle()
    status.write("Player X's Turn", align="center", font=("Courier", 22, "normal"))

    reset_button = turtle.Turtle()
    reset_button.speed(0)
    reset_button.color("green")

    reset_button.penup()
    reset_button.goto(300, 320)
    reset_button.write("Reset", align="center", font=("Courier", 20, "normal"))

    reset_button.onclick(lambda x, y: reset_game())

    win.listen()
    win.onclick(click)


win.listen()
win.onclick(click)
while True:
    win.update()

win.mainloop()
