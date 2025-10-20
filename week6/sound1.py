import py5_tools

py5_tools.processing.download_library("Sound")

# Step 2: Import py5 and the Sound classes
import py5

from processing.sound import SoundFile
from processing.sound import Waveform
from processing.sound import Amplitude

soundfile = None
waveform = None
amplitude = None
    
def setup():
    global soundfile, waveform, amplitude
    py5.size(400, 300)
    
    # Load a sound file - put your .wav or .mp3 file in a 'data' folder
    soundfile = SoundFile(py5.get_current_sketch(), "Electric Traditions.mp3")
    # soundfile.loop()

    waveform = Waveform(py5.get_current_sketch(), 512)
    waveform.input(soundfile)

    amplitude = Amplitude(py5.get_current_sketch())
    amplitude.input(soundfile)


def draw():
    global amplitude, waveform, amplitude
    py5.background(200)
    py5.fill(0)
    py5.text("Click to play sound", 20, py5.height/2)

    # Map mouse X to volume (0.0 to 1.0)
    volume = py5.remap(py5.mouse_x, 0, py5.width, 0.0, 1.0)
    soundfile.amp(volume)
    py5.text(f"Volume: {volume:.2f}", 50, 100)
    # Visual feedback
    py5.rect(50, 150, volume * 300, 30)

    waveform.analyze()
    for i in range(512):
        x = py5.remap(i, 0, 512, 0, py5.width)
        y = py5.remap(waveform.data[i], -1, 1, 0, py5.height)
        py5.point(x, y)

    
    amp = amplitude.analyze() # Returns 0.0 to 1.0
    print(amp)
    circle_size = py5.remap(amp, 0, 0.5, 50, 400)
    py5.circle(py5.width/2, py5.height/2, circle_size)

def mouse_pressed():
    soundfile.play()

py5.run_sketch()