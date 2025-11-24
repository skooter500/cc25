import py5
import mido

midi_input = None
last_note = None
last_velocity = 0

from processing.sound import SoundFile

soundfiles = []

def setup():
    global midi_input
    py5.size(800, 600)
    
    ports = mido.get_input_names()
    for i, port in enumerate(ports):
        print(f"{i}: {port}")
    
    if ports:
        midi_input = mido.open_input(ports[4])
        print(f"Listening on: {ports[1]}")

    soundfiles.append(SoundFile(py5.get_current_sketch(), "drums/clap-808.wav"))
    soundfiles.append(SoundFile(py5.get_current_sketch(), "drums/cowbell-808.wav"))
    soundfiles.append(SoundFile(py5.get_current_sketch(), "drums/crash-808.wav"))
    soundfiles.append(SoundFile(py5.get_current_sketch(), "drums/hihat-808.wav"))
    soundfiles.append(SoundFile(py5.get_current_sketch(), "drums/kick-808.wav"))
    soundfiles.append(SoundFile(py5.get_current_sketch(), "drums/openhat-808.wav"))
    soundfiles.append(SoundFile(py5.get_current_sketch(), "drums/perc-808.wav"))
    soundfiles.append(SoundFile(py5.get_current_sketch(), "drums/snare-808.wav"))
    soundfiles.append(SoundFile(py5.get_current_sketch(), "drums/tom-808.wav"))

def play_sound(i):
    soundfiles[i % len(soundfiles)].play()

def draw():
    global last_note, last_velocity
    
    py5.background(30)
    
    # Process ALL pending MIDI messages (non-blocking)
    if midi_input:
        for msg in midi_input.iter_pending():
            print(msg)
            
            if msg.type == 'note_on' and msg.velocity > 0:
                last_note = msg.note
                last_velocity = msg.velocity
                play_sound(msg.note)
            elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                last_velocity = 0
    
    # Visualize the current state
    if last_note and last_velocity > 0:
        py5.fill(255, py5.remap(last_note, 0, 127, 0, 255), 100)
        size = py5.remap(last_velocity, 0, 127, 50, 400)
        py5.circle(py5.width/2, py5.height/2, size)
    
    # Display info
    py5.fill(255)
    py5.text(f"FPS: {py5.get_frame_rate():.1f}", 10, 20)
    if last_note:
        py5.text(f"Note: {last_note}, Velocity: {last_velocity}", 10, 40)

def exiting():
    if midi_input:
        midi_input.close()

py5.run_sketch()