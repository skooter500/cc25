import py5_tools
import py5

py5_tools.processing.download_library("Sound")

from processing.sound import SoundFile
from processing.sound import Waveform
from processing.sound import Amplitude
from processing.sound import Reverb
from processing.sound import AudioIn
from processing.sound import Delay
from processing.sound import FFT
from processing.sound import PitchDetector


amplitude = None
waveform = None
reverb = None
mic = None
delay = None
fft = None
pitchdetector = None

def setup():
    global amplitude, waveform, reverb, mic, delay, fft, pitchdetector
    py5.size(512, 512)
    
    mic = AudioIn(py5.get_current_sketch(), 0)
    py5.color_mode(py5.HSB)
    mic.start()

    amplitude = Amplitude(py5.get_current_sketch())
    amplitude.input(mic)
    
    waveform = Waveform(py5.get_current_sketch(), 512)    
    waveform.input(mic)

    soundfile = SoundFile(py5.get_current_sketch(), "Electric Traditions.mp3")

    # soundfile.play()
    fft = FFT(py5.get_current_sketch(), 512)
    fft.input(mic)

    pitchdetector = PitchDetector(py5.get_current_sketch(), 0.5)

    pitchdetector.input(mic)

    


def draw():
    global amplitude, waveform, reverb, delay, fft, pitchdetector

    py5.background(0)
    py5.fill(255)

    amp = amplitude.analyze()
    print(amp)
    py5.stroke_weight(5)
    py5.stroke(amp * 255, 255, 255)
    py5.fill((1 - amp) * 255, 255, 255)

    waveform.analyze()
    for i in range(512):
        x = py5.remap(i, 0, 512, 0, py5.width)
        y = py5.remap(waveform.data[i], -1, 1, 0, py5.height)
        py5.point(x, y)


    halfH = py5.height / 2
    halfW = py5.height / 2


    # py5.circle(250, 250, amp * 200)

    fft.analyze()

    for i in range(512):
        band_amplitude = fft.spectrum[i]
        bar_height = py5.remap(band_amplitude, 0, 0.5,
        0, py5.height)
        py5.rect(i * 2, py5.height - bar_height, 2, bar_height)
    
    freq = pitchdetector.analyze()
    print(freq)
    
    y = py5.remap(freq, 250, 1173, 0, py5.height)
    py5.rect(20, y, 50, 50)

py5.run_sketch()


