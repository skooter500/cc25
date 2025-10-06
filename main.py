import py5

def setup():
    py5.size(200, 200)
    py5.rect_mode(py5.CENTER)



def draw():
    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)
    py5.circle(100, 100, 80)
    py5.line(10, 10, 100, 100)
    py5.stroke(100, 0,0)
    py5.fill(100, 100,0)
    

py5.run_sketch()