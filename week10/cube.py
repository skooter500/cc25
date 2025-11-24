import py5

from processing.sound import SoundFile
from processing.sound import Waveform
from processing.sound import Amplitude

soundfile = None
waveform = None
amplitude = None


soundfiles = []

pattern = []

def setup():
    global soundfile, waveform, amplitude

    py5.size(1000, 1000, py5.P3D)
    py5.color_mode(py5.HSB)
    
    
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


    for i in range(16):
        pattern.append(int(py5.random(0, len(soundfiles))))

    for i in range(16):
        print(pattern)
    
rot_x = 0
rot_y = 0

cam_z = -100

n = 0

def key_pressed():
    global soundfiles, amplitude, waveform
    i = py5.key_code - 48
    print(i)
    if i >= 0 and i < len(soundfiles): 
        play_sound(i)

pi = 0

def play_sound(i):
    global soundfiles, amplitude, waveform
    soundfiles[i].play()
    amplitude.input(soundfiles[i])
    waveform.input(soundfiles[i])

def draw():
    global rot_x, rot_y, cam_z, n, waveform, amplitude, pi

    py5.background(0)
    py5.lights()
    py5.stroke(255)
    # py5.translate(py5.width / 2, py5.height / 2)
    py5.stroke(200, 255, 255, 100)
    py5.stroke_weight(5)
    # py5.fill(99, 255, 255)
    py5.no_fill()


    interval = int(py5.remap(py5.mouse_x, 0, py5.width, 5, 120))
    if py5.frame_count % interval == 0:
        play_sound(pattern[pi])
        pi = (pi + 1) % len(pattern)



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
    py5.sphere(300)
    py5.pop_matrix()    

    cam_z = - py5.mouse_y * 2
    py5.camera(0, 0, cam_z, 0, 0, 0, 0, -1, 0)



    rot_x += 0.01
    rot_y += 0.01

py5.run_sketch()