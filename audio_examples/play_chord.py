import py5

from processing.sound import SinOsc

osc1 = SinOsc(py5.get_current_sketch())
osc2 = SinOsc(py5.get_current_sketch())
osc3 = SinOsc(py5.get_current_sketch())


# C Major chord
osc1.freq(261.63)
osc2.freq(329.63)
osc3.freq(392.00)
# C
# E
# G
def key_pressed():
    global osc1, osc2, osc3
    if py5.key == ' ':
        osc1.play()
        osc2.play()
        osc3.play()

def key_released():
    global osc1, osc2, osc3
    if py5.key == ' ':
        osc1.stop()
        osc2.stop()
        osc3.stop()



def setup():
    py5.size(512, 512)

def draw():
    py5.background(255)
    py5.fill(0)
    py5.text("Press SPACE to play a chord", 20, py5.height/2)

py5.run_sketch()