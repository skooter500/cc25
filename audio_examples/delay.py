import py5_tools

import py5

from processing.sound import SoundFile
from processing.sound import Waveform
from processing.sound import Delay

soundfile = None
waveform = None
delay = None

def setup():
    global soundfile, waveform, delay
    py5.size(400, 300)
    
    # Load a sound file - put your .wav or .mp3 file in a 'data' folder
    soundfile = SoundFile(py5.get_current_sketch(), "Electric Traditions.mp3")
    soundfile.loop()
    soundfile.play()

    waveform = Waveform(py5.get_current_sketch(), 512)
    waveform.input(soundfile)

    delay = Delay(py5.get_current_sketch())
    delay.process(soundfile, 5)
    

    

def draw():
    global amplitude, waveform, delay, soundfile
    py5.background(200)

    
    r = py5.remap(py5.mouse_x, 0, py5.width, 0.0, 5.0)
    delay.time(r)
    
    waveform.analyze()
    for i in range(512):
        x = py5.remap(i, 0, 512, 0, py5.width)
        y = py5.remap(waveform.data[i], -1, 1, 0, py5.height)
        py5.point(x, y)

    


py5.run_sketch()