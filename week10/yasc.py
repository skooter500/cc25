import py5
class Bullet:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = 0
        self.lifespan = 60  # Frames before disappearing
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.lifespan -= 1
    
    def is_dead(self):
        return self.lifespan <= 0
    
    def display(self):
        fx = py5.sin(self.angle)
        fy = - py5.cos(self.angle)
        py5.translate(self.x, self.y)
        py5.rotate(self.angle)
        py5.line(0, -5, 0, 5)



class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = py5.random(20, 50)
        self.vx = py5.random(-2, 2)  # Random velocity
        self.vy = py5.random(-2, 2)
        self.rotation = 0
        self.rotation_speed = py5.random(-0.1, 0.1)
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.rotation_speed
        
        # Wrap around screen
        if self.x > py5.width: self.x = 0
        elif self.x < 0: self.x = py5.width
        if self.y > py5.height: self.y = 0
        elif self.y < 0: self.y = py5.height
    
    def display(self):
        py5.push_matrix()
        py5.translate(self.x, self.y)
        py5.rotate(self.rotation)
        
        py5.fill(100)
        py5.stroke(150)
        py5.stroke_weight(2)
        
        # Draw irregular polygon
        py5.begin_shape()
        for i in range(8):
            angle = py5.TWO_PI / 8 * i
            r = self.size * py5.random(0.8, 1.2)
            px = py5.cos(angle) * r
            py5_y = py5.sin(angle) * r
            py5.vertex(px, py5_y)
        py5.end_shape(py5.CLOSE)
        
        py5.pop_matrix()

class Spaceship:
    def __init__(self, x, y):
        self.x = x          # Position
        self.y = y
        self.angle = 0      # Direction (radians)
        self.speed = 0      # Current speed
        self.size = 20      # Size of ship
        self.radius = self.size / 2
        self.rotation_speed = 0.1
    
    def display(self):
        py5.push_matrix()
        py5.translate(self.x, self.y)
        py5.rotate(self.angle)
        py5.line(-self.radius, self.radius, 0, -self.radius)
        py5.line(0, -self.radius, self.radius, self.radius)
        py5.line(self.radius, self.radius, 0, 0)
        py5.line(0, 0, -self.radius, self.radius)
        py5.pop_matrix()
        pass

    def rotate_left(self):
        self.angle -= self.rotation_speed
    
    def rotate_right(self):
        self.angle += self.rotation_speed

    def thrust(self):
        # Increase speed
        self.speed += 0.5
        # Limit maximum speed
        if self.speed > 5:
            self.speed = 5
    
    def reverse(self):
        # Decrease speed
        self.speed -= 0.5
        # Limit minimum speed
        if self.speed < -3:
            self.speed = -3

    def update(self):
        fx = py5.sin(self.angle)
        fy = - py5.cos(self.angle)
        
        self.x += fx * self.speed
        self.y += fy * self.speed

        self.speed *= 0.99



# Create a spaceship at center of screen
ship = Spaceship(400, 300)


asteroids = []

def setup():
    py5.size(500, 500)
    py5.smooth()

    for i in range(5):
        x = py5.random(py5.width)
        y = py5.random(py5.height)
        asteroids.append(Asteroid(x, y))

def draw():
    global ship
    py5.background(0)
    py5.stroke(255)

    if py5.is_key_pressed:
        if py5.key == 'w' or py5.key_code == py5.UP:
            ship.thrust()
        elif py5.key == 's' or py5.key_code == py5.DOWN:
            ship.reverse()
        
        if py5.key == 'a' or py5.key_code == py5.LEFT:
            ship.rotate_left()
        elif py5.key == 'd' or py5.key_code == py5.RIGHT:
            ship.rotate_right()

    for asteroid in asteroids:
        asteroid.update()
        asteroid.display()

    ship.update()
    ship.display()

py5.run_sketch()