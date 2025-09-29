import py5

x = 0
y = 0
speed = 5
dx = speed
dy = speed
w = 50
r = w / 2

def setup():
    global x, y
    py5.size(500, 500)
    y = py5.height / 2
    x = py5.width / 2
    py5.background(0)
    py5.color_mode(py5.HSB)

def key_pressed():
    print(py5.key)
    if py5.key == "w":
        print("forward")

def draw():
    global x, y, dx, dy, r, w

    ## TRAILS
    ald = 20
    py5.color_mode(py5.RGB)
    py5.blend_mode(py5.SUBTRACT)
    py5.fill(255, ald)

    py5.rect(-py5.width * 5, -py5.height * 5, py5.width * 10, py5.height * 10);
    py5.blend_mode(py5.BLEND)
    py5.color_mode(py5.HSB)


    py5.no_stroke()
    py5.fill(x, 255, 255)
    py5.circle(x , y, x)
    x = x + dx
    y = y + dy
    if x > (py5.width - r):
        dx = -speed
    if (x < r):
        dx = speed
    if y > (py5.height - r):
        dy = -speed
    if (y < r):
        dy = speed  

    # count = int(1 + py5.mouse_x / 4)
    # w = py5.width / count
    # r = w/ 2
    # for i in range(count):
    #     cx = r + (i * w)
    #     cy = py5.height / 2
    #     py5.circle(cx, cy, w)


    count = int(1 + py5.mouse_x / 4)
    color_gap = 255 / count
    gap = py5.width / count
    for i in range(count):
        py5.fill(i * color_gap, 255, 355)
        py5.rect(i * gap, 0, gap, py5.height)

    py5.stroke(0)
    py5.line(50, 50, 50, 100)
    py5.line(100, 50, 100, 100)
    py5.line(150, 50, 150, 100)
    py5.line(200, 50,200, 100)
    py5.line(250, 50, 250, 100)

    for i in range(5):
        lx = 50 + (i * 50)
        py5.line(lx, 120, lx, 200)
    
    for xx in range(50, 300, 50):
        py5.line(xx, 300, xx, 500)
    
    


    py5.fill(0, 255, 255)
        
    # if py5.mouse_x < py5.width / 2:
    #     py5.rect(0, 0, py5.width / 2, py5.height)
    # else:
    #     py5.rect(py5.width / 2, 0, py5.width / 2, py5.height)
    
    #py5.fill(255, 0, 0)
    #py5.rect(10, 10, 30, 90)
    #py5.fill(0, 255, 0)
    #py5.rect(100, 10, 30, 90)

for i in range(10):
    print(i)
 
for i in range(5, 10):
    print(i)

for i in range(100, -1, -10):
    print(i)


 

py5.run_sketch()


