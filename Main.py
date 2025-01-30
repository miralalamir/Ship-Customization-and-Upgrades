import turtle
import random
import time

class SpaceInvadersGame:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Turtle Space Invaders")
        self.screen.bgcolor("lightblue")
        self.screen.setup(width=800, height=600)

        self.ship = self.create_ship()
        self.obstacles = []
        self.score = 0

        self.setup_controls()
        self.create_obstacles(5)

    def create_ship(self):
        ship = turtle.Turtle()
        ship.shape("triangle")
        ship.color("darkblue")
        ship.penup()
        ship.goto(0, -250)
        ship.setheading(90)
        return ship

    def create_obstacle(self):
        obs = turtle.Turtle()
        obs.shape("circle")
        obs.color("green")
        obs.penup()
        obs.speed(0)
        obs.goto(random.randint(-350, 350), random.randint(100, 250))
        self.obstacles.append(obs)

    def create_obstacles(self, count):
        for _ in range(count):
            self.create_obstacle()

    def move_left(self):
        x = self.ship.xcor()
        x -= 15
        if x < -350:
            x = -350
        self.ship.setx(x)

    def move_right(self):
        x = self.ship.xcor()
        x += 15
        if x > 350:
            x = 350
        self.ship.setx(x)

    def move_up(self):
        y = self.ship.ycor()
        y += 15
        if y > 250:
            y = 250
        self.ship.sety(y)

    def move_down(self):
        y = self.ship.ycor()
        y -= 15
        if y < -250:
            y = -250
        self.ship.sety(y)

    def setup_controls(self):
        self.screen.listen()
        self.screen.onkey(self.move_left, "Left")
        self.screen.onkey(self.move_right, "Right")
        self.screen.onkey(self.move_up, "Up")
        self.screen.onkey(self.move_down, "Down")

    def check_collision(self):
        for obs in self.obstacles:
            if self.ship.distance(obs) < 20:
                return True
        return False

    def update_obstacles(self):
        for obs in self.obstacles:
            obs.sety(obs.ycor() - 5)
            if obs.ycor() < -300:
                obs.goto(random.randint(-350, 350), random.randint(100, 250))
                self.score += 1

    def run(self):
        while True:
            self.screen.update()
            self.update_obstacles()

            if self.check_collision():
                self.ship.goto(0, -250)
                self.score = 0
                time.sleep(1)

            self.ship.clear()
            self.ship.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

            time.sleep(0.02)

        self.screen.exitonclick()

if __name__ == "__main__":
    game = SpaceInvadersGame()
    game.run()