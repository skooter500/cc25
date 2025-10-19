# Comprehensive Py5 Sound Processing Tutorial

## Table of Contents
1. [Installation and Setup](#installation-and-setup)
2. [Basic Sound Playback](#basic-sound-playback)
3. [Sound Control](#sound-control)
4. [Sound Analysis](#sound-analysis)
5. [Sound Synthesis](#sound-synthesis)
6. [Audio Input](#audio-input)
7. [Audio Effects](#audio-effects)
8. [Complete Examples](#complete-examples)

---

## Installation and Setup

### Step 1: Install py5
```bash
pip install py5
```

### Step 2: Download the Processing Sound Library
Run this once to download the Sound library:

```python
import py5_tools

# Download the Sound library
py5_tools.processing.download_library("Sound")

# Check installed libraries
print(py5_tools.processing.installed_libraries())
```

### Step 3: Project Structure
Create your project folder structure:
```
my_project/
├── sketch.py
└── data/
    ├── mysound.wav
    ├── beat.mp3
    └── other_audio_files...
```

Place all your audio files in the `data` folder.

---

## Basic Sound Playback

### Loading and Playing a Sound File

```python
import py5
from processing.sound import SoundFile

soundfile = None

def setup():
    global soundfile
    py5.size(600, 400)
    
    # Load sound file (supports .wav, .aiff, .mp3)
    soundfile = SoundFile(py5.get_current_sketch(), "mysound.wav")
    
    # Play the sound once
    soundfile.play()

def draw():
    py5.background(220)
    py5.fill(0)
    py5.text("Sound is playing!", 50, 200)

py5.run_sketch()
```

### Playing Multiple Sounds

```python
import py5
from processing.sound import SoundFile

sound1 = None
sound2 = None
sound3 = None

def setup():
    global sound1, sound2, sound3
    py5.size(600, 400)
    
    sound1 = SoundFile(py5.get_current_sketch(), "kick.wav")
    sound2 = SoundFile(py5.get_current_sketch(), "snare.wav")
    sound3 = SoundFile(py5.get_current_sketch(), "hihat.wav")

def draw():
    py5.background(220)
    py5.fill(0)
    py5.text("Press 1, 2, or 3 to play sounds", 50, 200)

def key_pressed():
    if py5.key == '1':
        sound1.play()
    elif py5.key == '2':
        sound2.play()
    elif py5.key == '3':
        sound3.play()

py5.run_sketch()
```

---

## Sound Control

### Play, Pause, Stop, and Loop

```python
import py5
from processing.sound import SoundFile

soundfile = None

def setup():
    global soundfile
    py5.size(600, 400)
    soundfile = SoundFile(py5.get_current_sketch(), "mysound.wav")

def draw():
    py5.background(220)
    py5.fill(0)
    py5.text("SPACE: Play/Pause", 50, 100)
    py5.text("S: Stop", 50, 130)
    py5.text("L: Loop", 50, 160)
    py5.text("J: Jump to position", 50, 190)
    
    # Show if playing
    if soundfile.isPlaying():
        py5.fill(0, 255, 0)
        py5.text("PLAYING", 50, 250)

def key_pressed():
    if py5.key == ' ':
        if soundfile.isPlaying():
            soundfile.pause()
        else:
            soundfile.play()
    elif py5.key == 's':
        soundfile.stop()
    elif py5.key == 'l':
        soundfile.loop()
    elif py5.key == 'j':
        # Jump to 5 seconds into the track
        soundfile.jump(5.0)

py5.run_sketch()
```

### Volume and Playback Rate Control

```python
import py5
from processing.sound import SoundFile

soundfile = None

def setup():
    global soundfile
    py5.size(600, 400)
    soundfile = SoundFile(py5.get_current_sketch(), "mysound.wav")
    soundfile.loop()

def draw():
    py5.background(220)
    
    # Control volume with mouse X (0.0 to 1.0)
    volume = py5.remap(py5.mouse_x, 0, py5.width, 0.0, 1.0)
    soundfile.amp(volume)
    
    # Control playback rate with mouse Y (0.5x to 2.0x)
    rate = py5.remap(py5.mouse_y, 0, py5.height, 0.5, 2.0)
    soundfile.rate(rate)
    
    # Display info
    py5.fill(0)
    py5.text(f"Volume: {volume:.2f}", 50, 100)
    py5.text(f"Playback Rate: {rate:.2f}x", 50, 130)
    py5.text("Move mouse to adjust", 50, 160)
    
    # Draw volume bar
    py5.fill(100, 200, 255)
    py5.rect(50, 200, volume * 200, 30)
    
    # Draw rate indicator
    py5.stroke(255, 100, 100)
    py5.stroke_weight(3)
    py5.line(py5.mouse_x, 0, py5.mouse_x, py5.height)
    py5.no_stroke()

py5.run_sketch()
```

### Panning (Stereo Position)

```python
import py5
from processing.sound import SoundFile

soundfile = None

def setup():
    global soundfile
    py5.size(600, 400)
    soundfile = SoundFile(py5.get_current_sketch(), "mysound.wav")
    soundfile.loop()

def draw():
    py5.background(220)
    
    # Pan from left (-1.0) to right (1.0) with mouse X
    pan = py5.remap(py5.mouse_x, 0, py5.width, -1.0, 1.0)
    soundfile.pan(pan)
    
    py5.fill(0)
    py5.text(f"Pan: {pan:.2f}", 50, 100)
    py5.text("Left (-1.0) ← → Right (1.0)", 50, 130)
    
    # Draw pan indicator
    center_x = py5.width / 2
    indicator_x = center_x + (pan * center_x)
    py5.fill(255, 100, 150)
    py5.circle(indicator_x, py5.height / 2, 50)

py5.run_sketch()
```

---

## Sound Analysis

### Amplitude Analysis (Volume Detection)

```python
import py5
from processing.sound import SoundFile, Amplitude

soundfile = None
amplitude = None

def setup():
    global soundfile, amplitude
    py5.size(800, 400)
    
    soundfile = SoundFile(py5.get_current_sketch(), "mysound.wav")
    soundfile.loop()
    
    # Create amplitude analyzer
    amplitude = Amplitude(py5.get_current_sketch())
    amplitude.input(soundfile)

def draw():
    py5.background(0)
    
    # Get current amplitude (0.0 to 1.0)
    amp = amplitude.analyze()
    
    # Map amplitude to visual size
    circle_size = py5.remap(amp, 0, 0.5, 50, 400)
    
    # Draw pulsing circle
    py5.fill(255, 100, 150)
    py5.no_stroke()
    py5.circle(py5.width / 2, py5.height / 2, circle_size)
    
    # Display amplitude value
    py5.fill(255)
    py5.text(f"Amplitude: {amp:.3f}", 20, 30)
    py5.text(f"Circle size: {circle_size:.0f}", 20, 50)

py5.run_sketch()
```

### FFT - Frequency Spectrum Analysis

```python
import py5
from processing.sound import SoundFile, FFT

soundfile = None
fft = None
bands = 512

def setup():
    global soundfile, fft
    py5.size(800, 400)
    
    soundfile = SoundFile(py5.get_current_sketch(), "mysound.wav")
    soundfile.loop()
    
    # Create FFT analyzer with number of bands
    fft = FFT(py5.get_current_sketch(), bands)
    fft.input(soundfile)

def draw():
    py5.background(0)
    
    # Analyze the frequency spectrum
    fft.analyze()
    
    # Draw the spectrum as bars
    bar_width = py5.width / bands
    
    for i in range(bands):
        # Get amplitude for this frequency band
        band_amp = fft.spectrum[i]
        
        # Map to bar height
        bar_height = py5.remap(band_amp, 0, 0.5, 0, py5.height)
        
        # Color gradient: low freq = red, high freq = blue
        r = py5.remap(i, 0, bands, 255, 0)
        b = py5.remap(i, 0, bands, 0, 255)
        py5.fill(r, 100, b)
        
        # Draw bar from bottom up
        py5.rect(i * bar_width, py5.height - bar_height, bar_width, bar_height)

py5.run_sketch()
```

### Smoothed FFT Spectrum (Better Visualization)

```python
import py5
from processing.sound import SoundFile, FFT

soundfile = None
fft = None
bands = 128
sum_values = []
smooth_factor = 0.2

def setup():
    global soundfile, fft, sum_values
    py5.size(800, 400)
    
    soundfile = SoundFile(py5.get_current_sketch(), "beat.mp3")
    soundfile.loop()
    
    fft = FFT(py5.get_current_sketch(), bands)
    fft.input(soundfile)
    
    # Initialize smoothing array
    sum_values = [0.0] * bands

def draw():
    global sum_values
    py5.background(0)
    
    fft.analyze()
    
    bar_width = py5.width / bands
    
    for i in range(bands):
        # Smooth the values over time
        sum_values[i] += (fft.spectrum[i] - sum_values[i]) * smooth_factor
        
        # Map to bar height with scaling
        bar_height = py5.remap(sum_values[i], 0, 0.3, 0, py5.height)
        
        # Color based on amplitude
        brightness = py5.remap(sum_values[i], 0, 0.3, 50, 255)
        py5.fill(brightness, 100, 255 - brightness)
        
        py5.rect(i * bar_width, py5.height - bar_height, bar_width, bar_height)
    
    # Display info
    py5.fill(255)
    py5.text(f"Bands: {bands}", 10, 20)
    py5.text(f"Smooth Factor: {smooth_factor}", 10, 40)

py5.run_sketch()
```

### Waveform Visualization

```python
import py5
from processing.sound import SoundFile, Waveform

soundfile = None
waveform = None
samples = 512

def setup():
    global soundfile, waveform
    py5.size(800, 400)
    
    soundfile = SoundFile(py5.get_current_sketch(), "mysound.wav")
    soundfile.loop()
    
    # Create waveform analyzer
    waveform = Waveform(py5.get_current_sketch(), samples)
    waveform.input(soundfile)

def draw():
    py5.background(0)
    py5.stroke(100, 255, 150)
    py5.stroke_weight(2)
    py5.no_fill()
    
    # Analyze waveform
    waveform.analyze()
    
    # Draw waveform
    py5.begin_shape()
    for i in range(samples):
        x = py5.remap(i, 0, samples, 0, py5.width)
        # data[i] ranges from -1 to 1
        y = py5.remap(waveform.data[i], -1, 1, 0, py5.height)
        py5.vertex(x, y)
    py5.end_shape()
    
    # Center line
    py5.stroke(255, 100)
    py5.stroke_weight(1)
    py5.line(0, py5.height/2, py5.width, py5.height/2)

py5.run_sketch()
```

---

## Sound Synthesis

### Basic Oscillators

```python
import py5
from processing.sound import SinOsc

sine = None

def setup():
    global sine
    py5.size(600, 400)
    
    # Create sine wave oscillator
    sine = SinOsc(py5.get_current_sketch())
    sine.freq(440)  # A4 note
    sine.amp(0.5)   # 50% volume

def draw():
    py5.background(220)
    
    # Control frequency with mouse X (100 Hz to 1000 Hz)
    freq = py5.remap(py5.mouse_x, 0, py5.width, 100, 1000)
    sine.freq(freq)
    
    py5.fill(0)
    py5.text(f"Frequency: {freq:.0f} Hz", 50, 100)
    py5.text("Click to start/stop", 50, 130)
    
    # Draw frequency line
    py5.stroke(100, 150, 255)
    py5.stroke_weight(3)
    py5.line(py5.mouse_x, 0, py5.mouse_x, py5.height)

def mouse_pressed():
    if sine.isPlaying():
        sine.stop()
    else:
        sine.play()

py5.run_sketch()
```

### Different Waveform Types

```python
import py5
from processing.sound import SinOsc, TriOsc, SawOsc, SqrOsc

sine = None
triangle = None
sawtooth = None
square = None
current_osc = None

def setup():
    global sine, triangle, sawtooth, square, current_osc
    py5.size(600, 400)
    
    # Create different oscillator types
    sine = SinOsc(py5.get_current_sketch())
    triangle = TriOsc(py5.get_current_sketch())
    sawtooth = SawOsc(py5.get_current_sketch())
    square = SqrOsc(py5.get_current_sketch())
    
    # Set frequency and amplitude for all
    for osc in [sine, triangle, sawtooth, square]:
        osc.freq(220)
        osc.amp(0.3)
    
    current_osc = sine

def draw():
    py5.background(220)
    py5.fill(0)
    py5.text("Press 1: Sine Wave", 50, 100)
    py5.text("Press 2: Triangle Wave", 50, 130)
    py5.text("Press 3: Sawtooth Wave", 50, 160)
    py5.text("Press 4: Square Wave", 50, 190)
    
    # Display current wave type
    py5.text_size(20)
    py5.fill(255, 100, 0)
    if current_osc == sine:
        py5.text("Playing: SINE", 50, 250)
    elif current_osc == triangle:
        py5.text("Playing: TRIANGLE", 50, 250)
    elif current_osc == sawtooth:
        py5.text("Playing: SAWTOOTH", 50, 250)
    elif current_osc == square:
        py5.text("Playing: SQUARE", 50, 250)
    py5.text_size(12)

def key_pressed():
    global current_osc
    
    # Stop current oscillator
    if current_osc:
        current_osc.stop()
    
    # Start new oscillator
    if py5.key == '1':
        current_osc = sine
    elif py5.key == '2':
        current_osc = triangle
    elif py5.key == '3':
        current_osc = sawtooth
    elif py5.key == '4':
        current_osc = square
    
    current_osc.play()

py5.run_sketch()
```

### Musical Chord Generator

```python
import py5
from processing.sound import SinOsc

osc1, osc2, osc3 = None, None, None

def setup():
    global osc1, osc2, osc3
    py5.size(600, 400)
    
    # Create three oscillators for harmony
    osc1 = SinOsc(py5.get_current_sketch())
    osc2 = SinOsc(py5.get_current_sketch())
    osc3 = SinOsc(py5.get_current_sketch())
    
    # Set amplitudes
    osc1.amp(0.2)
    osc2.amp(0.2)
    osc3.amp(0.2)

def draw():
    py5.background(220)
    py5.fill(0)
    py5.text("Press keys to play chords:", 50, 50)
    py5.text("C: C Major (C-E-G)", 50, 100)
    py5.text("D: D Minor (D-F-A)", 50, 130)
    py5.text("G: G Major (G-B-D)", 50, 160)
    py5.text("A: A Minor (A-C-E)", 50, 190)

def key_pressed():
    if py5.key == 'c':
        # C Major: C (261.63), E (329.63), G (392.00)
        osc1.freq(261.63)
        osc2.freq(329.63)
        osc3.freq(392.00)
        play_chord()
    elif py5.key == 'd':
        # D Minor: D (293.66), F (349.23), A (440.00)
        osc1.freq(293.66)
        osc2.freq(349.23)
        osc3.freq(440.00)
        play_chord()
    elif py5.key == 'g':
        # G Major: G (392.00), B (493.88), D (587.33)
        osc1.freq(392.00)
        osc2.freq(493.88)
        osc3.freq(587.33)
        play_chord()
    elif py5.key == 'a':
        # A Minor: A (440.00), C (523.25), E (659.25)
        osc1.freq(440.00)
        osc2.freq(523.25)
        osc3.freq(659.25)
        play_chord()

def play_chord():
    osc1.play()
    osc2.play()
    osc3.play()

def key_released():
    osc1.stop()
    osc2.stop()
    osc3.stop()

py5.run_sketch()
```

### White and Pink Noise

```python
import py5
from processing.sound import WhiteNoise, PinkNoise

white = None
pink = None

def setup():
    global white, pink
    py5.size(600, 400)
    
    white = WhiteNoise(py5.get_current_sketch())
    pink = PinkNoise(py5.get_current_sketch())
    
    white.amp(0.3)
    pink.amp(0.3)

def draw():
    py5.background(220)
    py5.fill(0)
    py5.text("Press W: White Noise", 50, 100)
    py5.text("Press P: Pink Noise", 50, 130)
    py5.text("Press S: Stop", 50, 160)

def key_pressed():
    if py5.key == 'w':
        pink.stop()
        white.play()
    elif py5.key == 'p':
        white.stop()
        pink.play()
    elif py5.key == 's':
        white.stop()
        pink.stop()

py5.run_sketch()
```

---

## Audio Input

### Microphone Input with Amplitude

```python
import py5
from processing.sound import AudioIn, Amplitude

mic = None
amplitude = None

def setup():
    global mic, amplitude
    py5.size(600, 400)
    
    # Create audio input (microphone)
    mic = AudioIn(py5.get_current_sketch(), 0)
    mic.start()
    
    # Analyze microphone input
    amplitude = Amplitude(py5.get_current_sketch())
    amplitude.input(mic)

def draw():
    py5.background(0)
    
    # Get microphone amplitude
    amp = amplitude.analyze()
    
    # Visualize with circle
    size = py5.remap(amp, 0, 0.5, 50, 400)
    py5.fill(100, 255, 150)
    py5.circle(py5.width / 2, py5.height / 2, size)
    
    # Display value
    py5.fill(255)
    py5.text(f"Microphone Level: {amp:.3f}", 20, 30)
    py5.text("Make some noise!", 20, 50)

py5.run_sketch()
```

### Microphone Input with FFT

```python
import py5
from processing.sound import AudioIn, FFT

mic = None
fft = None
bands = 256

def setup():
    global mic, fft
    py5.size(800, 400)
    
    mic = AudioIn(py5.get_current_sketch(), 0)
    mic.start()
    
    fft = FFT(py5.get_current_sketch(), bands)
    fft.input(mic)

def draw():
    py5.background(0)
    
    fft.analyze()
    
    bar_width = py5.width / bands
    
    for i in range(bands):
        bar_height = py5.remap(fft.spectrum[i], 0, 0.5, 0, py5.height)
        
        # Color based on frequency
        hue = py5.remap(i, 0, bands, 0, 255)
        py5.color_mode(py5.HSB)
        py5.fill(hue, 255, 255)
        py5.color_mode(py5.RGB)
        
        py5.rect(i * bar_width, py5.height - bar_height, bar_width, bar_height)
    
    py5.fill(255)
    py5.text("Microphone Frequency Spectrum", 20, 20)

py5.run_sketch()
```

---

## Audio Effects

### Low Pass Filter

```python
import py5
from processing.sound import SoundFile, LowPass

soundfile = None
lowpass = None

def setup():
    global soundfile, lowpass
    py5.size(600, 400)
    
    soundfile = SoundFile(py5.get_current_sketch(), "mysound.wav")
    soundfile.loop()
    
    # Create low-pass filter
    lowpass = LowPass(py5.get_current_sketch())
    lowpass.process(soundfile)

def draw():
    py5.background(220)
    
    # Control filter frequency with mouse X (100 Hz to 10000 Hz)
    cutoff = py5.remap(py5.mouse_x, 0, py5.width, 100, 10000)
    lowpass.freq(cutoff)
    
    py5.fill(0)
    py5.text(f"Low-Pass Filter Cutoff: {cutoff:.0f} Hz", 50, 100)
    py5.text("Move mouse left/right", 50, 130)
    
    # Draw cutoff indicator
    py5.stroke(255, 0, 0)
    py5.stroke_weight(2)
    py5.line(py5.mouse_x, 0, py5.mouse_x, py5.height)

py5.run_sketch()
```

### High Pass Filter

```python
import py5
from processing.sound import SoundFile, HighPass

soundfile = None
highpass = None

def setup():
    global soundfile, highpass
    py5.size(600, 400)
    
    soundfile = SoundFile(py5.get_current_sketch(), "mysound.wav")
    soundfile.loop()
    
    # Create high-pass filter
    highpass = HighPass(py5.get_current_sketch())
    highpass.process(soundfile)

def draw():
    py5.background(220)
    
    # Control filter frequency
    cutoff = py5.remap(py5.mouse_x, 0, py5.width, 100, 5000)
    highpass.freq(cutoff)
    
    py5.fill(0)
    py5.text(f"High-Pass Filter Cutoff: {cutoff:.0f} Hz", 50, 100)
    py5.text("Move mouse to adjust filter", 50, 130)

py5.run_sketch()
```

### Band Pass Filter

```python
import py5
from processing.sound import SoundFile, BandPass

soundfile = None
bandpass = None

def setup():
    global soundfile, bandpass
    py5.size(600, 400)
    
    soundfile = SoundFile(py5.get_current_sketch(), "mysound.wav")
    soundfile.loop()
    
    bandpass = BandPass(py5.get_current_sketch())
    bandpass.process(soundfile)

def draw():
    py5.background(220)
    
    # Control center frequency with mouse X
    freq = py5.remap(py5.mouse_x, 0, py5.width, 100, 5000)
    bandpass.freq(freq)
    
    # Control bandwidth with mouse Y
    bw = py5.remap(py5.mouse_y, 0, py5.height, 0.1, 10.0)
    bandpass.bw(bw)
    
    py5.fill(0)
    py5.text(f"Center Frequency: {freq:.0f} Hz", 50, 100)
    py5.text(f"Bandwidth: {bw:.2f}", 50, 130)
    py5.text("Move mouse to adjust", 50, 160)

py5.run_sketch()
```

### Reverb Effect

```python
import py5
from processing.sound import SoundFile, Reverb

soundfile = None
reverb = None

def setup():
    global soundfile, reverb
    py5.size(600, 400)
    
    soundfile = SoundFile(py5.get_current_sketch(), "mysound.wav")
    soundfile.loop()
    
    reverb = Reverb(py5.get_current_sketch())
    reverb.process(soundfile)

def draw():
    py5.background(220)
    
    # Control room size (0.0 to 1.0)
    room_size = py5.remap(py5.mouse_x, 0, py5.width, 0.0, 1.0)
    reverb.room(room_size)
    
    # Control damping (0.0 to 1.0)
    damp = py5.remap(py5.mouse_y, 0, py5.height, 0.0, 1.0)
    reverb.damp(damp)
    
    py5.fill(0)
    py5.text(f"Room Size: {room_size:.2f}", 50, 100)
    py5.text(f"Damping: {damp:.2f}", 50, 130)
    py5.text("Move mouse to adjust reverb", 50, 160)

py5.run_sketch()
```

### Delay Effect

```python
import py5
from processing.sound import SoundFile, Delay

soundfile = None
delay = None

def setup():
    global soundfile, delay
    py5.size(600, 400)
    
    soundfile = SoundFile(py5.get_current_sketch(), "mysound.wav")
    soundfile.loop()
    
    delay = Delay(py5.get_current_sketch())
    delay.process(soundfile)

def draw():
    py5.background(220)
    
    # Control delay time (0.0 to 5.0 seconds)
    delay_time = py5.remap(py5.mouse_x, 0, py5.width, 0.0, 2.0)
    delay.time(delay_time)
    
    # Control feedback (0.0 to 1.0)
    feedback = py5.remap(py5.mouse_y, 0, py5.height, 0.0, 0.9)
    delay.feedback(feedback)
    
    py5.fill(0)
    py5.text(f"Delay Time: {delay_time:.2f} seconds", 50, 100)
    py5.text(f"Feedback: {feedback:.2f}", 50, 130)
    py5.text("Move mouse to adjust delay", 50, 160)

py5.run_sketch()
```

---

## Complete Examples

### Example 1: Interactive Music Visualizer

```python
import py5
from processing.sound import SoundFile, FFT, Amplitude

soundfile = None
fft = None
amplitude = None
bands = 128
sum_values = []

def setup():
    global soundfile, fft, amplitude, sum_values
    py5.size(800, 600)
    py5.color_mode(py5.HSB, 360, 100, 100)
    
    soundfile = SoundFile(py5.get_current_sketch(), "beat.mp3")
    soundfile.loop()
    
    fft = FFT(py5.get_current_sketch(), bands)
    fft.input(soundfile)
    
    amplitude = Amplitude(py5.get_current_sketch())
    amplitude.input(soundfile)
    
    sum_values = [0.0] * bands

def draw():
    global sum_values
    
    # Get overall amplitude
    amp = amplitude.analyze()
    
    # Background pulses with music
    bg_brightness = py5.remap(amp, 0, 0.5, 10, 30)
    py5.background(0, 0, bg_brightness)
    
    fft.analyze()
    
    # Draw spectrum bars
    bar_width = py5.width / bands
    
    for i in range(bands):
        sum_values[i] += (fft.spectrum[i] - sum_values[i]) * 0.3
        
        bar_height = py5.remap(sum_values[i], 0, 0.3, 0, py5.height * 0.8)
        
        # Rainbow colors
        hue = py5.remap(i, 0, bands, 0, 360)
        saturation = 80
        brightness = py5.remap(sum_values[i], 0, 0.3, 30, 100)
        
        py5.fill(hue, saturation, brightness)
        py5.no_stroke()
        
        x = i * bar_width
        y = py5.height - bar_height
        py5.rect(x, y, bar_width, bar_height)
    
    # Central circle that pulses
    circle_size = py5.remap(amp, 0, 0.5, 100, 400)
    py5.fill(180, 100, 100, 50)
    py5.circle(py5.width / 2, py5.height / 2, circle_size)
    
    # Info text
    py5.fill(0, 0, 100)
    py5.text(f"FPS: {py5.frame_rate:.0f}", 10, 20)
    py5.text("Press SPACE to pause/play", 10, 40)

def key_pressed():
    if py5.key == ' ':
        if soundfile.isPlaying():
            soundfile.pause()
        else:
            soundfile.play()

py5.run_sketch()
```

### Example 2: Simple Synthesizer

```python
import py5
from processing.sound import SinOsc

# Piano key frequencies (one octave)
notes = {
    'a': 261.63,  # C
    's': 293.66,  # D
    'd': 329.63,  # E
    'f': 349.23,  # F
    'g': 392.00,  # G
    'h': 440.00,  # A
    'j': 493.88,  # B
    'k': 523.25,  # C (high)
}

oscillators = {}
active_notes = set()

def setup():
    global oscillators
    py5.size(800, 400)
    
    # Create an oscillator for each note
    for key, freq in notes.items():
        osc = SinOsc(py5.get_current_sketch())
        osc.freq(freq)
        osc.amp(0.3)
        oscillators[key] = osc

def draw():
    py5.background(220)
    
    # Draw piano keys
    key_width = py5.width / len(notes)
    for i, (key, freq) in enumerate(notes.items()):
        x = i * key_width
        
        # Highlight active keys
        if key in active_notes:
            py5.fill(100, 200, 255)
        else:
            py5.fill(255)
        
        py5.stroke(0)
        py5.rect(x, 100, key_width - 2, 200)
        
        # Label
        py5.fill(0)
        py5.text(key.upper(), x + key_width/2 - 5, 200)
        py5.text(f"{freq:.0f}Hz", x + key_width/2 - 20, 220)
    
    # Instructions
    py5.fill(0)
    py5.text("Play notes with keys: A S D F G H J K", 50, 50)
    py5.text(f"Active notes: {len(active_notes)}", 50, 350)

def key_pressed():
    if py5.key in notes:
        active_notes.add(py5.key)
        oscillators[py5.key].play()

def key_released():
    if py5.key in notes:
        active_notes.discard(py5.key)
        oscillators[py5.key].stop()

py5.run_sketch()
```

### Example 3: Real-time Microphone Visualizer

```python
import py5
from processing.sound import AudioIn, FFT, Amplitude
import math

mic = None
fft = None
amplitude = None
bands = 256

def setup():
    global mic, fft, amplitude
    py5.size(800, 800)
    py5.color_mode(py5.HSB, 360, 100, 100)
    
    mic = AudioIn(py5.get_current_sketch(), 0)
    mic.start()
    
    fft = FFT(py5.get_current_sketch(), bands)
    fft.input(mic)
    
    amplitude = Amplitude(py5.get_current_sketch())
    amplitude.input(mic)

def draw():
    py5.background(0, 0, 10)
    py5.translate(py5.width / 2, py5.height / 2)
    
    fft.analyze()
    amp = amplitude.analyze()
    
    # Draw circular spectrum
    for i in range(bands):
        angle = py5.remap(i, 0, bands, 0, py5.TWO_PI)
        
        # Map spectrum to radius
        spec_val = fft.spectrum[i]
        radius = py5.remap(spec_val, 0, 0.5, 100, 350)
        
        # Calculate position
        x = math.cos(angle) * radius
        y = math.sin(angle) * radius
        
        # Color
        hue = py5.remap(i, 0, bands, 0, 360)
        brightness = py5.remap(spec_val, 0, 0.5, 30, 100)
        
        py5.fill(hue, 80, brightness)
        py5.no_stroke()
        py5.circle(x, y, 5)
    
    # Central circle pulsing with amplitude
    center_size = py5.remap(amp, 0, 0.3, 50, 150)
    py5.fill(180, 100, 100)
    py5.circle(0, 0, center_size)
    
    # Info
    py5.fill(0, 0, 100)
    py5.text("Microphone Input", -60, -py5.height/2 + 30)

py5.run_sketch()
```

---

## Tips and Best Practices

### 1. File Formats
- **WAV**: Uncompressed, best quality, larger files
- **MP3**: Compressed, smaller files, good quality
- **AIFF**: Uncompressed, high quality (Mac-friendly)

### 2. Performance Tips
- Use fewer FFT bands for better performance (128 or 256 instead of 512)
- Limit the number of simultaneous sound sources
- Use `.stop()` on sounds you're no longer using
- Lower the frame rate if visualization is choppy: `py5.frame_rate(30)`

### 3. Volume Levels
- Keep amplitude values between 0.0 and 1.0
- Start with lower volumes (0.3-0.5) and adjust
- Be careful with multiple oscillators - they can add up quickly

### 4. Common Issues

**No sound playing:**
- Check that the sound file exists in the `data` folder
- Verify your system audio is working
- Make sure you called `.play()` or started the oscillator

**Sound is distorted:**
- Reduce amplitude/volume
- Check for too many simultaneous sounds
- Try lowering playback rate if it's too high

**FFT looks weird:**
- Adjust the number of bands
- Use smoothing for better visualization
- Map values appropriately (usually 0-0.3 or 0-0.5 range)

### 5. File Paths
All audio files should be in a `data` folder:
```
your_project/
├── sketch.py
└── data/
    └── your_sound.wav
```

Then load with just the filename:
```python
soundfile = SoundFile(py5.get_current_sketch(), "your_sound.wav")
```

---

## Additional Resources

- **Processing Sound Library**: https://processing.org/reference/libraries/sound/
- **Py5 Documentation**: https://py5coding.org
- **Audio File Converters**: Use Audacity (free) to convert between formats
- **Free Sound Effects**: freesound.org, zapsplat.com

---

## Summary

You now know how to:
- ✅ Load and play sound files
- ✅ Control playback (play, pause, stop, loop, volume, rate, pan)
- ✅ Analyze sound (amplitude, FFT, waveform)
- ✅ Synthesize sound (oscillators, noise)
- ✅ Process microphone input
- ✅ Apply audio effects (filters, reverb, delay)
- ✅ Create interactive audio visualizations

Happy sound coding with Py5! 🎵🎨