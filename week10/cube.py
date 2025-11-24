import py5, os

from processing.sound import SoundFile
from processing.sound import Waveform
from processing.sound import Amplitude
from processing.sound import SinOsc
from processing.sound import AudioIn

soundfile = None
waveform = None
amplitude = None

osc1 = SinOsc(py5.get_current_sketch())
osc2 = SinOsc(py5.get_current_sketch())
osc3 = SinOsc(py5.get_current_sketch())


# C Major chord
osc1.freq(261.63)
osc2.freq(329.63)
osc3.freq(392.00)

soundfiles = []

piano_files = []

pattern = []

piano_pattern = []

image = None

def setup():
    global soundfile, waveform, amplitude, image, pattern, piano_pattern

    py5.size(1000, 1000, py5.P3D)
    py5.color_mode(py5.HSB)
    
    image = py5.load_image("bryan.jpg")
    
    # soundfile.loop()
    
    waveform = Waveform(py5.get_current_sketch(), 512)

    amplitude = Amplitude(py5.get_current_sketch())

    soundfiles.append(SoundFile(py5.get_current_sketch(), "drums/clap-808.wav"))
    soundfiles.append(SoundFile(py5.get_current_sketch(), "drums/cowbell-808.wav"))
    soundfiles.append(SoundFile(py5.get_current_sketch(), "drums/crash-808.wav"))
    soundfiles.append(SoundFile(py5.get_current_sketch(), "drums/hihat-808.wav"))
    soundfiles.append(SoundFile(py5.get_current_sketch(), "drums/kick-808.wav"))
    soundfiles.append(SoundFile(py5.get_current_sketch(), "drums/openhat-808.wav"))
    soundfiles.append(SoundFile(py5.get_current_sketch(), "drums/perc-808.wav"))
    soundfiles.append(SoundFile(py5.get_current_sketch(), "drums/snare-808.wav"))
    soundfiles.append(SoundFile(py5.get_current_sketch(), "drums/tom-808.wav"))

    dir = "data/scale"
    for file in os.listdir(dir):
        if file.endswith('.mp3') or file.endswith('.wav'):
            # file_path = os.path.join(item_path, file)
            piano_files.append(SoundFile(py5.get_current_sketch(), "scale/" + file))
    

    pattern = [4,-1, 3, -1, 4,-1, -1, 3, 4,-1, 3, -1, 4,-1, -1, 3]
    
    piano_pattern = [4,-1, 8, -1, 4,-1, 2, -1, 4,-1, 3, -1, 4,-1, -1, 3]

    
rot_x = 0
rot_y = 0

cam_z = -100

n = 0

def key_pressed():
    global soundfiles, amplitude, waveform, piano_off
    i = py5.key_code - 48
    piano_off = i
    # if i >= 0 and i < len(soundfiles): 
        # play_sound(i)

pi = 0
piano_off = 0

def play_piano(i):
    global soundfiles, amplitude, waveform, piano_off

    if i < 0:
        return
    i = (i + piano_off) % len(piano_files) 
    
    piano_files[i].play()
    # amplitude.input(piano_files[i])
    # waveform.input(piano_files[i])
    

def play_sound(i):
    global soundfiles, amplitude, waveform
    if i >= 0 and i < len(soundfiles):
        soundfiles[i].play()

    
    
    
piano_i = 0

x = - 200

def draw():
    global rot_x, rot_y, cam_z, n, waveform, amplitude, pi, piano_i
    global osc1, osc2, osc3, image, x
    
    py5.background(0)
    py5.lights()
    py5.stroke(255)
    # py5.translate(py5.width / 2, py5.height / 2)
    py5.stroke(200, 255, 255, 100)
    py5.stroke_weight(5)
    # py5.fill(99, 255, 255)
    py5.no_fill()

    py5.image(image, x, 0)
    x = x + 1
    interval = int(py5.remap(py5.mouse_x, 0, py5.width, 5, 120))
    if py5.frame_count % interval == 0:
        play_piano(piano_pattern[piano_i])
        play_sound(pattern[pi])        
        pi = (pi + 1) % len(pattern)
        piano_i = (piano_i + 1) % len(piano_pattern)



    waveform.analyze()
    
    amp = amplitude.analyze() # Returns 0.0 to 1.0
    # amp = 0

    r = py5.noise(n)
    
    py5.push_matrix()
    py5.translate(- 200, 0, 0)
    py5.rotate_x(r)
    py5.rotate_y(r)
    py5.box(py5.remap(amp, 0, 1, 100, 300))
    py5.pop_matrix()

    n += 0.01

    py5.push_matrix()

    py5.translate(200, 0, 0)
    py5.rotate_x(rot_x)
    py5.rotate_y(rot_y)        
    py5.stroke(py5.remap(amp, 0, 1, 100, 150), 255, 255)    
    # py5.stroke(100, 255, 255, 100)
    py5.sphere(py5.remap(amp, 0, 1, 100, 300))
    py5.pop_matrix()    

    cam_z = py5.mouse_y * 2
    py5.camera(0, 0, cam_z, 0, 0, 0, 0, 1, 0)

    rot_x += 0.01
    rot_y += 0.01


    t = py5.noise(n)      
    offs = py5.mouse_y / py5.height  
    osc1.freq(py5.remap(t + offs , 0, 1, 20, 200))
    osc2.freq(py5.remap(t + offs, 0, 1, 10000, 200))
    osc3.freq(py5.remap(t + offs, 0, 1, 10000, 15000))
    # osc1.play()
    osc1.amp(0.3)
    # osc2.play()
    # osc3.play()
    osc2.amp(0.3)
    osc3.amp(0.3)
    

py5.run_sketch()