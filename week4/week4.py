import py5
import math

for i in range(10):
    print(i)

for i in range(5, 10):
    print(i)

for i in range(10, -1, -1):
    print(i)

s = "I love Pythin"

print(s)
print(f"The value of s is {s}")

love = s[2:6]

print(love)

py = s[7:len(s)]

print(py)

py = s[7: 20]
print(py)

py = s[-6: len(s)]
print(py)

py =s[len(s) - 1: -6: -1] 
print(py)

def string_bits(str):
  s = ""
  for i in range(0, len(str), 2):
    print(i)
    s += str[i: i + 1]
  return s

def string_splosion(str):
  l = len(str)
  s = ""
  for i in range(0, l):
    s += str[0:i + 1]
  return s

print(string_bits("Hello"))

print(string_splosion("Code"))

def setup():
    global angle, hei, adj
    py5.size(500, 500)
    hei = math.sin(math.radians(angle)) * 65
    adj = math.cos(math.radians(angle)) * 65
    print(hei)
    py5.color_mode(py5.HSB)


str_len = 65
angle = 70
hei = 0
adj = 0



def draw():
    global adj, hei
    border = 50
    py5.background(0)
    py5.line(border, 100, border + adj, 100)
    py5.line(border, 100, border + adj, 100 - hei)
    py5.line(border + adj, 100 - hei, border + adj, 100)

    count = 10
    cx = py5.width / 2
    cy = py5.height / 2
    theta_inc = py5.TAU / count
    rad = 10
    px = cx
    py = cy
    c = 0
    for i in range(500):
       theta = theta_inc * i
       x = cx + math.sin(theta) * rad
       y = cy - math.cos(theta) * rad
       rad += 1
       py5.stroke(c, 255, 255)
       c = c + 1
       # py5.text(str(i + 1), x + 20, y)
       py5.line(px, py, x, y)
       px = x
       py = y

py5.run_sketch()

