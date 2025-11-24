import py5

def setup():
    py5.size(500, 500, py5.P3D)
    py5.color_mode(py5.HSB)

rot_x = 0
rot_y = 0

def draw():
    global rot_x, rot_y
    py5.background(0)
    py5.lights()
    py5.stroke(255)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.stroke(200, 255, 255)
    py5.stroke_weight(50)
    py5.fill(99, 255, 255)
    py5.rotate_x(rot_x)
    py5.rotate_y(rot_y)
    py5.box(200)

    rot_x += 0.01
    rot_y += 0.01

py5.run_sketch()