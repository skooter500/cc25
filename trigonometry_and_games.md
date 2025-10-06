# Basic Trigonometry - Problem Set

**Name:** _________________ **Date:** _________________

---

## Part 1: Finding Trigonometric Ratios (10 points)

For each triangle representing a game vector or design element, find sin A, cos A, and tan A. Round to three decimal places.

**Problem 1 (Velocity Vector):**
```
        C
        |\ 
      8 | \ 17 units/sec
        |  \
        |___\
        A  15  B
```

sin A = _______ cos A = _______ tan A = _______


**Problem 2 (Camera Ray):**
```
        target
        C
        |\ 
      5 | \ 13 units
        |  \
        |___\
        A  12  B
       camera
```

sin A = _______ cos A = _______ tan A = _______


**Problem 3 (Jump Trajectory):**
```
        C
        |\ 
      7 | \ 25 units
        |  \
        |___\
        A  24  B
```

sin A = _______ cos A = _______ tan A = _______

---

## Part 2: Special Triangles (10 points)

Solve for the missing sides. Use exact values (leave in radical form when appropriate).

**Problem 4:** 45-45-90 Triangle (Isometric Grid)
```
        C
        |\ 
      x | \ 10 units
        |  \
        |___\
        A  x  B
```
In isometric game design, tiles often use 45° angles. Find x.

x = _______


**Problem 5:** 30-60-90 Triangle (Hex Grid)
```
        C
        |\ 
      y | \ 12 pixels
        |  \
        |___\
        A  x  B
        30°
```
Hexagonal grids use 30° and 60° angles. Find x and y.

x = _______ y = _______


**Problem 6:** 45-45-90 Triangle (Diagonal Movement)
```
        C
        |\ 
      6 | \ x units
        |  \
        |___\
        A  6  B
```
A character moves diagonally 6 units in each direction. Find the total distance x.

x = _______

---

## Part 3: Finding Missing Sides (15 points)

Use trigonometric ratios to find the missing side. Round to two decimal places.

**Problem 7 (Character Jump):**
```
        peak
        |\ 
      x | \ 20 units
        |  \
        |___\
    start    
        35°
```
A character jumps with initial velocity 20 units/sec at 35° angle. Find x (the maximum height reached).

x = _______


**Problem 8 (Camera Distance):**
```
        C
        |\ 
        | \ 15 units
      9 |  \
        |___\
        A  x  B
```
A camera is 9 units above a character and has line-of-sight distance of 15 units. Find x (the horizontal distance).

x = _______


**Problem 9 (Projectile Range):**
```
        C
        |\ 
      8 | \ x
        |  \
        |___\
        A     B
        50°
```
An arrow is shot at 50° and reaches maximum height of 8 units. Find x (the initial velocity, treating the vertical component as 8 units).

x = _______

---

## Part 4: Finding Missing Angles (15 points)

Find the angle θ. Round to the nearest degree.

**Problem 10 (Sprite Rotation):**
```
          top
        C
        |\ 
      6 | \ 10 pixels
        |  \
        |___\
      pivot  B
         θ
```
A sprite rotates around a pivot point. Find the rotation angle θ.

θ = _______


**Problem 11 (Slope Angle):**
```
        C
        |\ 
      5 | \ 
        |  \
        |___\
        A  12  B
         θ
```
A game terrain rises 5 units over 12 units horizontal distance. Find the slope angle θ.

θ = _______


**Problem 12 (Camera Tilt):**
```
        target
        C
        |\ 
        | \ 13 units
      5 |  \
        |___\
      camera  B
         θ
```
A camera is 5 units below a target and 13 units away (line-of-sight). Find the upward tilt angle θ.

θ = _______

---

## Part 5: Pythagorean Theorem (10 points)

Find the missing side using the Pythagorean theorem.

**Problem 13 (Distance Calculation):**
A player moves 9 units right and 12 units up on a 2D grid. Find the direct distance c from start to finish.

c = _______


**Problem 14 (Hitbox Diagonal):**
A rectangular hitbox has width 7 pixels and diagonal 25 pixels. Find the height b.

b = _______

---

## Part 6: Word Problems (20 points)

Show all work for full credit.

**Problem 15 (Game Dev):** 
A character in a platformer game jumps with an initial velocity of 30 units/second at a 60° angle.

a) What is the horizontal velocity component? _______

b) What is the vertical velocity component? _______


**Problem 16 (Game Design):**
An enemy's vision cone extends 50 units forward with a 40° angle from their facing direction. A player stands 30 units directly in front of the enemy.

a) Draw and label a diagram of this situation.

b) How far to the side (perpendicular distance) can the player move before leaving the vision cone? _______


**Problem 17 (UI/UX Design):**
You're designing a radial menu with 8 buttons arranged in a perfect circle with radius 120 pixels. The first button is at 0° (directly right).

a) What angle separates each button? _______

b) What are the x and y coordinates of the button at position 3? (Hint: position 3 is at 2 × the separation angle) _______

---

## Part 7: Challenge Problems (20 points)

**Problem 18 (3D Graphics):**
A 3D camera is positioned 100 units away from an object. The camera's field of view (FOV) is 90°. How wide is the viewing area at the object's distance? (Hint: The FOV creates two 45° angles from center)



**Problem 19 (Game Mechanics):**
A grappling hook in a game shoots at 45° upward with a range of 80 units on flat ground. A player wants to grapple to a platform that is 25 units high and 50 units away horizontally. 

a) Can they reach it with the same launch angle? Show your work.

b) If not, what angle would they need? (Round to nearest degree)



**Problem 20 (Animation):**
An animated character's arm rotates around a shoulder pivot point. The shoulder is at coordinates (100, 150), and the hand is 60 pixels away from the shoulder. If the arm rotates to 120° (measured counterclockwise from the positive x-axis):

a) What are the x and y coordinates of the hand? _______

b) If the arm rotates an additional 30°, what are the new coordinates? _______

---

## Bonus Problem (+5 points)

**Game Design Challenge:**

You're designing a top-down racing game. A car is traveling at 100 pixels/second and needs to drift around a corner. The drift angle is 25° from the car's direction of travel.

a) What is the forward velocity component (in the direction the car is pointing)? _______

b) What is the sideways velocity component (perpendicular to car's direction)? _______

c) If the car maintains this drift for 2 seconds, how far sideways does it slide? _______

---

**