import turtle
import random
import time

class Ship:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.addshape("photos/ship.gif")  # Register the image shape
        self.ship = turtle.Turtle()
        self.ship.shape("photos/ship.gif")  # Set the ship's shape to the registered image
        self.ship.penup()
        self.ship.goto(0, -250)
        self.ship.setheading(90)
        self.health = 100

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

    def fire_bullet(self):
        bullets = []
        bullet = Bullet(self.ship.xcor(), self.ship.ycor())
        bullets.append(bullet)

class Obstacle:
    def __init__(self):
        self.obstacle = turtle.Turtle()
        self.screen = turtle.Screen()
        self.screen.addshape("Photos/Obstacle.gif")
        self.obstacle.shape("Photos/Obstacle.gif") 
        self.obstacle.color(random.choice(["darkred", "darkgreen", "darkorange"]))
        self.obstacle.penup()
        self.obstacle.speed(0)
        self.obstacle.goto(random.randint(-350, 350), random.randint(100, 250))

    def move(self):
        self.obstacle.sety(self.obstacle.ycor() - 5)
        if self.obstacle.ycor() < -300:
            self.obstacle.goto(random.randint(-350, 350), random.randint(100, 250))

class EnemyShip:
    def __init__(self):
        self.enemy = turtle.Turtle()
        self.screen = turtle.Screen()
        self.screen.addshape("Photos/EnemyShip.gif")
        self.enemy.shape("Photos/EnemyShip.gif")  # Set the enemy's shape to the registered image
        self.enemy.color("red")
        self.enemy.penup()
        self.enemy.goto(random.randint(-350, 350), random.randint(100, 250))
        self.enemy.setheading(random.randint(0, 360))

    def move(self):
        self.enemy.forward(2)
        if self.enemy.xcor() > 350 or self.enemy.xcor() < -350 or self.enemy.ycor() > 250 or self.enemy.ycor() < -250:
            self.enemy.setheading(random.randint(0, 360))

class Bullet:
    def __init__(self, x, y):
        self.bullet = turtle.Turtle()
        self.screen = turtle.Screen()
        self.screen.addshape("Photos/Bullet.gif")
        self.bullet.shape("Photos/Bullet.gif")  # Set the bullet's shape to the registered image
        self.bullet.penup()
        self.bullet.goto(x, y)
        self.bullet.setheading(90)

    def move(self):
        self.bullet.sety(self.bullet.ycor() + 20)

class Treasure:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.addshape("Photos/Treasure.gif")
        self.treasure = turtle.Turtle()
        self.treasure.shape("Photos/Treasure.gif")
        self.treasure.penup()
        self.treasure.goto(random.randint(-400,400),random.randint(-300,300))

class PowerUp:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.addshape("Photos/PowerUp.gif")
        self.powerup = turtle.Turtle()
        self.powerup.shape("Photos/PowerUp.gif")  # Set the power-up's shape to the registered image
        self.powerup.color("blue")
        self.powerup.shapesize(stretch_wid=1.5, stretch_len=1.5)  # Control the size of the power-ups
        self.powerup.penup()
        self.powerup.goto(random.randint(-350, 350), random.randint(100, 250))

class Particle:
    def __init__(self, x, y, color):
        self.particle = turtle.Turtle()
        self.particle.shape("circle")
        self.particle.color(color)
        self.particle.penup()
        self.particle.goto(x, y)
        self.particle.speed(0)
        self.particle.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.lifetime = 20

    def update(self):
        self.particle.sety(self.particle.ycor() + random.randint(-5, 5))
        self.particle.setx(self.particle.xcor() + random.randint(-5, 5))
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.particle.hideturtle()
            return False
        return True

class Background:
    def __init__(self, screen):
        self.screen = turtle.Screen()
        self.screen.addshape("photos/Background.gif")  # Register the image shape
        self.create_background = turtle.Turtle()
        self.create_background.shape("photos/Background.gif")
        self.bg_elements = []

    def create_background(self):
        for _ in range(20):
            element = turtle.Turtle()
            element.shape("circle")
            element.color("lightblue")
            element.penup()
            element.speed(0)
            element.goto(random.randint(-400, 400), random.randint(-300, 300))
            self.bg_elements.append(element)

    def update(self):
        for element in self.bg_elements:
            element.sety(element.ycor() - 2)
            if element.ycor() < -300:
                element.goto(random.randint(-400, 400), 300)

class OceanAdventureGame:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Turtle Ocean Adventure")
        self.screen.bgcolor("lightblue")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)

        self.background = Background(self.screen)
        self.ship = Ship()
        self.obstacles = [Obstacle() for _ in range(5)]
        self.enemy_ships = [EnemyShip() for _ in range(3)]
        self.treasure = Treasure()
        self.powerups = [PowerUp() for _ in range(2)]
        self.bullets = []
        self.particles = []  # List to store particles
        self.score = 0
        self.treasures_collected = 0
        self.level = 1
        self.health = 100
        self.score_display = self.create_score_display()
        self.health_display = self.create_health_display()

        self.setup_controls()
        self.show_start_screen()

    def create_score_display(self):
        score_display = turtle.Turtle()
        score_display.speed(0)
        score_display.color("black")
        score_display.penup()
        score_display.hideturtle()
        score_display.goto(0, 260)
        score_display.write("           | Treasures: 0 | Level: 1", align="center", font=("Courier", 24, "normal"))
        return score_display
    def create_health_display(self):
        health_display = turtle.Turtle()
        health_display.speed(0)
        health_display.color("red")
        health_display.penup()
        health_display.hideturtle()
        health_display.goto(-350, 260)
        health_display.write("Health: 100", align="left", font=("Courier", 24, "normal"))
        return health_display

    def update_score_display(self):
        self.score_display.clear()
        self.score_display.write(f"Score: {self.score} | Treasures: {self.treasures_collected} | Level: {self.level}", align="center", font=("Courier", 24, "normal"))

    def update_health_display(self):
        self.health_display.clear()
        self.health_display.write(f"Health: {self.ship.health}", align="left", font=("Courier", 24, "normal"))

    def setup_controls(self):
        self.screen.listen()
        self.screen.onkeypress(self.ship.move_left, "Left")
        self.screen.onkeypress(self.ship.move_right, "Right")
        self.screen.onkeypress(self.ship.move_up, "Up")
        self.screen.onkeypress(self.ship.move_down, "Down")
        self.screen.onkey(self.ship.fire_bullet, "space")
        self.screen.onkey(self.start_game, "s")

    def check_collision(self):
        for obs in self.obstacles:
            if self.ship.ship.distance(obs.obstacle) < 20:
                self.ship.health -= 10
                self.update_health_display()
                if self.ship.health <= 0:
                    return True
        for enemy in self.enemy_ships:
            if self.ship.ship.distance(enemy.enemy) < 20:
                self.ship.health -= 20
                self.update_health_display()
                if self.ship.health <= 0:
                    return True
        return False

    def check_treasure_collision(self):
        if self.ship.ship.distance(self.treasure.treasure) < 20:
            return True
        return False

    def check_powerup_collision(self):
        for powerup in self.powerups:
            if self.ship.ship.distance(powerup.powerup) < 20:
                self.ship.health = min(100, self.ship.health + 20)
                self.update_health_display()
                powerup.powerup.goto(random.randint(-350, 350), random.randint(-250, 250))

    def check_bullet_collision(self):
        for bullet in self.bullets:
            for obs in self.obstacles:
                if bullet.bullet.distance(obs.obstacle) < 20:
                    obs.obstacle.goto(random.randint(-350, 350), random.randint(-250, 250))
                    bullet.bullet.hideturtle()
                    self.bullets.remove(bullet)
                    self.score += 1
                    self.update_score_display()
                    self.create_particles(bullet.bullet.xcor(), bullet.bullet.ycor(), "orange")
            for enemy in self.enemy_ships:
                if bullet.bullet.distance(enemy.enemy) < 20:
                    enemy.enemy.goto(random.randint(-350, 350), random.randint(-250, 250))
                    bullet.bullet.hideturtle()
                    self.bullets.remove(bullet)
                    self.score += 5
                    self.update_score_display()
                    self.create_particles(bullet.bullet.xcor(), bullet.bullet.ycor(), "red")

    def create_particles(self, x, y, color):
        for _ in range(10):
            particle = Particle(x, y, color)
            self.particles.append(particle)

    def update_particles(self):
        for particle in self.particles:
            if not particle.update():
                self.particles.remove(particle)

    def update_obstacles(self):
        for obs in self.obstacles:
            obs.move()
            if obs.obstacle.ycor() < -300:
                self.score += 1
                self.update_score_display()

    def update_enemy_ships(self):
        for enemy in self.enemy_ships:
            enemy.move()

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.move()
            if bullet.bullet.ycor() > 300:
                bullet.bullet.hideturtle()
                self.bullets.remove(bullet)

    def show_start_screen(self):
        self.start_screen = turtle.Turtle()
        self.start_screen.speed(0)
        self.start_screen.color("black")
        self.start_screen.penup()
        self.start_screen.hideturtle()
        self.start_screen.write("Press 'S' to Start", align="center", font=("Courier", 24, "bold"))
        self.screen.update()

    def show_game_over_screen(self):
        game_over_screen = turtle.Turtle()
        game_over_screen.speed(0)
        game_over_screen.color("red")
        game_over_screen.penup()
        game_over_screen.hideturtle()
        game_over_screen.goto(0, 0)
        game_over_screen.write("Game Over", align="center", font=("Courier", 36, "bold"))
        self.screen.update()
        time.sleep(2)
        game_over_screen.clear()

    def show_treasure_collected_screen(self):
        treasure_collected_screen = turtle.Turtle()
        treasure_collected_screen.speed(0)
        treasure_collected_screen.color("black")
        treasure_collected_screen.penup()
        treasure_collected_screen.hideturtle()
        treasure_collected_screen.goto(0, 0)
        treasure_collected_screen.write("Treasure Collected!", align="center", font=("Courier", 36, "bold"))
        self.screen.update()
        time.sleep(2)
        treasure_collected_screen.clear()

    def start_game(self):
        self.start_screen.clear()
        self.run()

    def run(self):
        self.update()
        self.screen.ontimer(self.run, 20)  # Schedule the next update in 20 milliseconds

    def update(self):
        self.screen.update()
        self.background.update()
        self.update_obstacles()
        self.update_enemy_ships()
        self.update_bullets()
        self.update_particles()
        self.check_powerup_collision()
        self.check_bullet_collision()

        if self.check_collision():
            self.show_game_over_screen()
            self.ship.ship.goto(0, -250)
            self.score = 0
            self.treasures_collected = 0
            self.level = 1
            self.ship.health = 100
            self.update_score_display()
            self.update_health_display()
            time.sleep(1)

        if self.check_treasure_collision():
            self.show_treasure_collected_screen()
            self.treasures_collected += 1
            self.update_score_display()
            self.treasure.treasure.goto(random.randint(-300, 300), random.randint(-200, 200))
            if self.treasures_collected % 5 == 0:
                self.level += 1
                self.obstacles.append(Obstacle())
                self.enemy_ships.append(EnemyShip())
                self.update_score_display()

if __name__ == "__main__":
    game = OceanAdventureGame()
    turtle.mainloop()