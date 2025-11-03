import py5


from processing.sound import SoundFile
from processing.sound import Waveform
from processing.sound import Amplitude
from processing.sound import SinOsc
from processing.sound import SqrOsc

sine = None
square = None

def setup():
    global sine, square
    py5.size(600, 400)
    sine = SinOsc(py5.get_current_sketch())
    sine.freq(440) # A4 note (440 Hz)
    sine.amp(0.5)

    square = SqrOsc(py5.get_current_sketch())
    square.freq(440) # A4 note (440 Hz)
    square.amp(0.5)



    # 50% volume
def mouse_pressed():
    # sine.play() # Start oscillator
    square.play()
def mouse_released():
    # sine.stop()
    square.stop()
    
def draw():
    square.freq(py5.remap(py5.mouse_x, 0, py5.width, 200, 800))
# Stop oscillator

py5.run_sketch()