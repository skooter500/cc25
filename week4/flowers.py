import py5, math, random

cx = 0
cy = 0

def draw_flower(px, py):
    petals = 12

    py5.stroke(0, 255, 0)
    py5.stroke_weight(5)
    py5.line(px, py, px , py + 100)
    py5.fill(255, 255, 0)
    py5.circle(cx, cy,50)

    
    theta_inc = py5.TAU  / petals
    r = py5.mouse_x
    
    for i in range(petals):
        theta = i * theta_inc

        
        x = px + py5.sin(theta) * r
        y = py - py5.cos(theta) * r
        py5.stroke(0, 255, 0)
        py5.line(px, py, x, y)
        py5.fill(255)
        py5.no_stroke()
    
        py5.circle(x, y, 20)

def setup():
    global cx, cy
    py5.size(500,500)
    py5.background(0)
    cx = py5.width / 2
    cy = py5.height / 2
    t = 0
    # draw_flower(cx, cy)
    # draw_flower(50, 100)
    



    
def draw():
    global cx, cy
    py5.background(0)
    cx = py5.width / 2
    cy = py5.height / 2
    
    draw_flower(cx, cy)
    
py5.run_sketch()