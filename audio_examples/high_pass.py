import py5_tools

import py5

from processing.sound import SoundFile
from processing.sound import Waveform
from processing.sound import HighPass
from processing.sound import WhiteNoise

soundfile = None
waveform = None
high_pass = None
white_noise = None

def setup():
    global soundfile, waveform, high_pass, white_noise
    py5.size(400, 300)
    
    white_noise = WhiteNoise(py5.get_current_sketch())
    white_noise.play()
    waveform = Waveform(py5.get_current_sketch(), 512)
    waveform.input(white_noise)

    high_pass = HighPass(py5.get_current_sketch())
    high_pass.process(white_noise)


    

def draw():
    global amplitude, waveform, reverb, soundfile
    py5.background(200)

    
    r = py5.remap(py5.mouse_x, 0, py5.width, 0.0, 15000)
    high_pass.freq(r)
    
    waveform.analyze()
    for i in range(512):
        x = py5.remap(i, 0, 512, 0, py5.width)
        y = py5.remap(waveform.data[i], -1, 1, 0, py5.height)
        py5.point(x, y)

    


py5.run_sketch()