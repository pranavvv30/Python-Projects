import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

sc = turtle.Screen()
sc.bgcolor("lightblue")
sc.title("Snake Game")
sc.setup(width=600, height=600)
sc.tracer(0)

head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
countdown_time = 10
head.goto(0, 0)
head.direction = "Stop"

food_timer = []
food = turtle.Turtle()
colors = random.choice(['red', 'grey', 'black'])
shapes = random.choice(['square', 'circle', 'triangle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)
food_timer.append(10)

"""food2 = turtle.Turtle()
colors = random.choice(['red', 'grey', 'black'])
shapes = random.choice(['square', 'circle', 'triangle'])
food2.speed(0)
food2.shape(shapes)
food2.color(colors)
food2.penup()
food2.goto(random.randint(-290, 290), random.randint(-290, 290))

food3 = turtle.Turtle()
colors = random.choice(['red', 'grey', 'black'])
shapes = random.choice(['square', 'circle', 'triangle'])
food3.speed(0)
food3.shape(shapes)
food3.color(colors)
food3.penup()
food3.goto(random.randint(-290, 290), random.randint(-290, 290))

food4 = turtle.Turtle()
colors = random.choice(['red', 'grey', 'black'])
shapes = random.choice(['square', 'circle', 'triangle'])
food4.speed(0)
food4.shape(shapes)
food4.color(colors)
food4.penup()
food4.goto(random.randint(-290, 290), random.randint(-290, 290))"""

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score : 0  High Score : 0", align="center", font=("Candara", 24, "bold"))

timer_pen = turtle.Turtle()
timer_pen.speed(0)
timer_pen.shape("square")
timer_pen.color("red")
timer_pen.penup()
timer_pen.hideturtle()
timer_pen.goto(0, 230)


def goup():
    if head.direction != "down":
        head.direction = "up"


def godown():
    if head.direction != "up":
        head.direction = "down"


def goleft():
    if head.direction != "right":
        head.direction = "left"


def goright():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

sc.listen()
sc.onkeypress(goup, "Up")
sc.onkeypress(godown, "Down")
sc.onkeypress(goleft, "Left")
sc.onkeypress(goright, "Right")


def crosswalls():
    if head.xcor() > 290:
        y = head.ycor()
        head.goto(-290, y)
    if head.xcor() < -290:
        y = head.ycor()
        head.goto(290, y)
    if head.ycor() > 290:
        x = head.xcor()
        head.goto(x, -290)
    if head.ycor() < -290:
        x = head.xcor()
        head.goto(x, 290)


segments = []
countdown_time = 10


def update_time():
    global countdown_time
    global score
    minutes = countdown_time // 60
    seconds = countdown_time % 60
    timer_string = f"Time:{minutes}:{seconds}"
    timer_pen.clear()
    timer_pen.write(timer_string, align="center", font=("Candara", 24, "bold"))
    countdown_time -= 1
    if countdown_time >= 0:
        sc.ontimer(update_time, 1000)
    else:
        time.sleep(delay)
        head.direction = "Stop"
        head.goto(0, 0)
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        countdown_time = 10
        pen.clear()
        pen.write(f"Score:{score}  High Score:{high_score}", align="center", font=("Candara", 24, "bold"))
        timer_pen.clear()
        timer_pen.write("Time's Up", align="center", font=("Candara", 24, "bold"))
        game_over()
def reset_timer():
    global countdown_time
    global score
    countdown_time = 10
    score = 0
    update_time()

def game_over():
    global game_running
    game_running = False

def start_game():
    global game_running
    game_running = True
    reset_timer()


game_running = False
while True:
    if not game_running:
        start_game()

    sc.update()
    crosswalls()
    """if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:"
       time.sleep(1)
        head.direction = "Stop"
        head.goto(0, 0)
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        pen.clear()
        score = 0
        pen.write(f"Score:{score}  High Score:{high_score}", align="center", font=("Candara", 24, "bold"))"""

    if head.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        countdown_time = 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f"Score:{score}  High Score:{high_score}", align="center", font=("Candara", 24, "bold"))

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.direction = "Stop"
            head.goto(0, 0)
            countdown_time = 0
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            pen.clear()
            pen.write(f"Score:{score}  High Score:{high_score}", align="center", font=("Candara", 24, "bold"))
    time.sleep(delay)
sc.mainloop()
