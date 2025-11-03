import py5

from processing.sound import SoundFile
from processing.sound import Waveform
from processing.sound import Amplitude
from processing.sound import SinOsc
from processing.sound import SqrOsc


sine = None
square = None
square1 = None

def setup():
    global sine, square, square1
    py5.size(600, 400)
    sine = SinOsc(py5.get_current_sketch())
    sine.freq(440) # A4 note (440 Hz)
    sine.amp(0.5)

    square = SqrOsc(py5.get_current_sketch())
    square.freq(440) # A4 note (440 Hz)
    square.amp(0.5)
    square.play()

    square1 = SqrOsc(py5.get_current_sketch())
    square1.amp(0.5)
    square1.play()



    # 50% volume
def mouse_pressed():
    # sine.play() # Start oscillator
    square.play()
def mouse_released():
    # sine.stop()
    square.stop()
    

bryan = 0
def draw():
    py5.background(0)
    global bryan, square, square1
    bryan += 0.001
    n = py5.noise(bryan)
    n1 = py5.noise(bryan + 1000)
    
    square.freq(py5.remap(n, 0, 1, 20, 2000))
    square1.freq(py5.remap(n1, 0, 1, 2000, 100))

    x1 = py5.remap(n, 0, 1, 0, py5.width)
    y1 = py5.remap(n1, 0, 1, 0, py5.height)

    py5.ellipse(x1, y1, 50, 50)
# Stop oscillator

py5.run_sketch()