import py5_tools
import py5
py5_tools.processing.download_library("Sound")

from processing.sound import SoundFile
from processing.sound import Waveform
from processing.sound import Amplitude
from processing.sound import Reverb
from processing.sound import AudioIn
from processing.sound import Delay


sound_file = None
amplitude = None
waveform = None
reverb = None
mic = None
delay = None

def setup():
    global sound_file, amplitude, waveform, reverb, mic, delay
    py5.size(512, 512)
    sound_file = SoundFile(py5.get_current_sketch(), "Electric Traditions.mp3")
    

    
    reverb = Reverb(py5.get_current_sketch())
    reverb.process(sound_file)

    mic = AudioIn(py5.get_current_sketch(), 0)
    py5.color_mode(py5.HSB)
    mic.start()

    amplitude = Amplitude(py5.get_current_sketch())
    amplitude.input(mic)

    waveform = Waveform(py5.get_current_sketch(), 512)
    waveform.input(mic)

    delay = Delay(py5.get_current_sketch())
    delay.process(mic)

def draw():
    global sound_file, amplitude, waveform, reverb, delay
    
    

    py5.background(0)
    py5.fill(255)
    py5.text("Click the screen to play audio", 50, 200)

    volume = py5.remap(py5.mouse_x, 0, py5.width, 0.0, 1.0)
    # sound_file.amp(volume)

    py5.rect(0, 200, py5.mouse_x, 50)

    rate = py5.remap(py5.mouse_y, 0, py5.height, 0.5, 2.0)
    # sound_file.rate(rate)

    amp = amplitude.analyze()
    py5.stroke_weight(5)
    py5.stroke(amp * 255, 255, 255)
    py5.fill((1 - amp) * 255, 255, 255)
    
    py5.circle(250, 250, amp * 200)

    halfH = py5.height / 2
    halfW = py5.height / 2
    waveform.analyze()

    room = py5.remap(py5.mouse_x, 0, py5.width, 0.0, 1.0)
    reverb.room(room)

    damp = py5.remap(py5.mouse_y, 0, py5.height, 0.0, 1.0)
    reverb.damp(damp)

    # Delay time in seconds
    time = py5.remap(py5.mouse_x, 0, py5.width, 0.0, 2.0)
    delay.time(time)
    # Feedback: how much repeats
    feedback = py5.remap(py5.mouse_y, 0, py5.height,
    0.0, 0.9)
    delay.feedback(feedback)
    
    for i in range(len(waveform.data)):
        py5.line(i, halfH - (waveform.data[i] * halfH), i, halfH + (waveform.data[i] * halfH))


def mouse_pressed():
    global sound_file
    if sound_file.isPlaying():
        sound_file.stop()
    else:
        sound_file.play()

py5.run_sketch()



sample_rate = 44100
channels = 2
resolution = 2 
time_in_hours = 1

time_in_seconds = time_in_hours * 60 * 60
size_in_bytes = time_in_seconds * sample_rate * resolution * channels
size_in_kb = size_in_bytes / 1000
size_in_mb = size_in_kb / 1000
size_in_gb = size_in_mb / 1000

print(f"Size in bytes: {size_in_bytes}")
print(f"size_in_kb: {size_in_kb}")

print(f"size_in_gb: {size_in_gb}")

print(f"size_in_mb: {size_in_mb}")


