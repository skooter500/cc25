# Take-Home Assignment: Music Experience

## Project Brief

Create an interactive music-themed application using Python and py5. Your project should respond to user input and create a visual experience connected to music, sound, or rhythm.

## Theme: Music Experience

Your application should explore music in a visual and interactive way. This could be:
- A visual music player interface
- A musical instrument simulator
- A music visualizer that responds to user input
- An album cover generator
- A visual story inspired by a song
- A beat maker or rhythm game
- A soundboard with visual feedback
- A music-themed animation controller

## Required Technical Elements

Your project MUST include all of the following:

### 1. Variables
- Use variables to store and update values
- Include at least numeric, string, and boolean variables
- Examples: positions, colors, states, user scores, song titles

### 2. Drawing with Code
- Use py5 drawing functions (shapes, colors, text)
- Create visual elements that relate to your music theme
- Consider: buttons, waveforms, notes, instruments, album art, etc.

### 3. Loops
- Use `for` loops to draw multiple elements or create patterns
- Use the `draw()` loop effectively for animation
- Examples: drawing multiple beat indicators, iterating through playlists, creating repeating patterns

### 4. If Statements
- Include conditional logic that changes behavior
- Examples: checking if a button is clicked, changing visuals based on state, responding to different key presses

### 5. Lists
- Use at least one list to store related data
- Examples: list of song names, beat patterns, colors, particle positions, sound effect names

### 6. Dictionaries
- Use at least one dictionary to organize data
- Examples: storing properties of songs, button configurations, instrument settings, visual themes

### 7. Interactivity
- Respond to mouse clicks, mouse position, or keyboard input
- User actions should change what's displayed or how the program behaves

## Project Ideas

### Idea 1: Visual Soundboard
Create a grid of clickable buttons, each representing a different sound or instrument. When clicked, buttons light up and display the sound name. Track which sounds have been played.

**Example features:**
- 6-12 colored buttons in a grid
- Each button stored as a dictionary with properties (name, color, position)
- Visual feedback when clicked (animation, color change)
- Display list of recently played sounds

### Idea 2: Mood-Based Music Visualizer
Create an interactive visualizer where clicking different areas or pressing keys changes the "mood" and visual style.

**Example features:**
- Different moods: happy, sad, energetic, calm
- Each mood has its own color palette (stored in a dictionary)
- Animated shapes that respond to mouse position
- Particles or shapes that multiply and move based on selected mood

### Idea 3: Album Collection Browser
Create a visual library of your favorite albums that you can browse through.

**Example features:**
- List of album dictionaries (title, artist, year, color theme)
- Click left/right to browse through albums
- Display album info and visual representation
- Rate albums or mark favorites

### Idea 4: Beat Pattern Maker
Create a simple rhythm sequencer where you can toggle beats on/off.

**Example features:**
- Grid representing beats in a loop (16 steps)
- Click to toggle each beat on/off
- Visual playhead that moves through the pattern
- Different instrument rows (kick, snare, hi-hat)

### Idea 5: Song Story Animator
Create a visual story inspired by a song's lyrics or feeling, controlled by user interaction.

**Example features:**
- Multiple scenes representing different parts of the song
- Click or press keys to advance through scenes
- Each scene has different visual elements and colors
- Animated elements in each scene

### Idea 6: Music Player Interface
Design a fictional music player with visual controls and displays.

**Example features:**
- Play/pause button, skip buttons
- Playlist shown as a list
- "Now playing" display with song info from dictionary
- Progress bar (simulated)
- Volume control that changes visual size/intensity

## Submission Requirements

### Code
- Python file(s)
- Bonus marks for use of git!

### Documentation (in comments or separate file)
Include:
- Your name and student number
- Brief description of your project (2-3 sentences)
- Instructions for interaction (which keys/mouse actions do what)
- What you are most proud of

### Creativity & Polish
- Your project should be complete and functional
- Consider visual appeal: colors, layout, typography

## Tips for Success

**Start Simple**
- Get basic functionality working first
- Add features one at a time
- Test frequently

**Plan Your Data**
- Sketch out what lists and dictionaries you'll need
- Think about what information you need to store

**Use What You Learned**
- Reference the particle system lab for animation techniques
- Use the list/dictionary exercises as templates
- Build on code examples from class

**Be Creative**
- Make it personal - use music you actually like
- Experiment with colors and shapes

## Rubric

| Category | Weighting | 1 | 2.1 | 2.2 | Pass | Fail |
|----------|-----------|--------|----|----|----|----|
| Technical Implementation | 33% | Excellent use of all required elements (loops, conditionals, lists, dictionaries). Creative use of nested data structures. Multiple types of loops used effectively. Complex conditional logic. Smooth animations using draw() loop. Advanced features like particle systems or procedural generation. Code is well-structured and efficient. Goes beyond requirements with additional technical features | Good use of all required elements. Lists and dictionaries used meaningfully to organize data. For loops create patterns or iterate through collections. If statements control program flow and interactivity. Variables update and change state appropriately. Code works reliably without errors | All required elements present and functional. Basic use of lists and dictionaries. Simple for loops and conditionals. Variables are used but may be basic. Some minor errors but program runs. Meets minimum technical requirements | Some required elements missing or not working properly. Limited use of lists or dictionaries. Basic variables and simple loops. Program runs but may have errors or incomplete functionality | Missing multiple required elements. Program doesn't run or has major errors. Little evidence of understanding loops, lists, or dictionaries |
| Creativity & Music Theme | 33% | Highly original interpretation of music theme. Visually polished and cohesive design. Excellent use of color, typography, and layout. Strong connection between visual elements and musical concept. Interactive elements are intuitive and satisfying. Goes beyond basic requirements with creative features. Professional-looking interface. Clear personal style and creative voice | Clear music theme with good visual design. Thoughtful use of color and shapes. Interactive elements work well. Good connection between visuals and music concept. Shows creativity and personal interpretation. Well-organized layout. Pleasant to look at and use | Music theme is present and understandable. Basic visual design with reasonable color choices. Functional interface though may lack polish. Some creativity shown. Adequate connection to music concept | Weak connection to music theme. Basic or inconsistent visual design. Limited creativity or personal interpretation. Interface works but is confusing or unappealing | No clear music theme. Poor visual design or non-functional interface. No evidence of creative thought |
| Code Quality & Documentation | 33% | Exceptionally clean, well-commented code. Clear variable naming throughout. Logical code organization. Comprehensive documentation including name, description, interaction instructions, and technical requirements breakdown. Comments explain complex logic. Code is easy to read and understand. Evidence of testing and refinement | Clean, readable code with good comments. Descriptive variable names. Complete documentation with all required sections. Instructions are clear. Technical requirements clearly identified. Code is organized and understandable | Code works with some comments. Variable names are mostly clear. Documentation present but may be incomplete. Basic instructions provided. Required elements identified but descriptions may be brief | Minimal or confusing comments. Poor variable naming. Incomplete documentation. Instructions unclear or missing. Hard to identify required technical elements | No comments or documentation. Unreadable code. No explanation of how to use the program. Cannot identify technical requirements |



## Getting Started

1. Choose your concept (or create your own!)
2. Sketch it out on paper
3. List what variables, lists, and dictionaries you'll need
4. Start with the basic visual layout
5. Add interactivity step by step
6. Test and refine

Remember: This is about demonstrating your understanding of Python and py5 fundamentals through a creative project. It doesn't need to be complex - focus on doing the basics well and adding your own creative spin!

**Most importantly: Have fun!!**