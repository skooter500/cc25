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
py5.run_sketch()