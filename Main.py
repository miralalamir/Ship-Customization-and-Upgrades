import turtle
import random
import time

screen = turtle.Screen()
screen.title("Turtle Space Invaders")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)

ship = turtle.Turtle()
ship.shape("triangle")
ship.color("darkblue")
ship.penup()
ship.goto(0, -250)
ship.setheading(90)

obstacles = []

def create_obstacle():
    obs = turtle.Turtle()
    obs.shape("circle")
    obs.color("red")
    obs.penup()
    obs.speed(0)
    obs.goto(random.randint(-350, 350), random.randint(100, 250))
    obstacles.append(obs)

def move_left():
    x = ship.xcor()
    x -= 15
    if x < -350:
        x = -350
    ship.setx(x)

def move_right():  
    x = ship.xcor()
    x += 15
    if x > 350:
        x = 350
    ship.setx(x)

def move_up():
    y = ship.ycor()
    y += 15
    if y > 250:
        y = 250
    ship.sety(y)

def move_down():
    y = ship.ycor()
    y -= 15
    if y < -250:
        y = -250
    ship.sety(y)

screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

for _ in range(5):
    create_obstacle()

def check_collision():
    for obs in obstacles:
        if ship.distance(obs) < 20:
            return True
    return False

score = 0

while True:
    screen.update()

    for obs in obstacles:
        obs.sety(obs.ycor() - 5)
        if obs.ycor() < -300:
            obs.goto(random.randint(-350, 350), random.randint(100, 250))
            score += 1
    
    if check_collision():
        ship.goto(0, -250)
        score = 0
        time.sleep(1)

    ship.clear()
    ship.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))   

    time.sleep(0.02)

screen.exitonclick()