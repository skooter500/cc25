# Python Data Structures with py5 - Visual Examples
# Install: pip install py5

import py5
import random
import math

# =============================================================================
# EXAMPLE 1: LISTS - Particle System
# =============================================================================

def example_1_lists():
    """
    Particles stored in a list. Click to add particles.
    Demonstrates: append, iteration, list comprehension
    """
    particles = []
    
    def setup():
        py5.size(600, 400)
        py5.background(20)
    
    def draw():
        py5.background(20, 20, 30, 50)  # Trail effect
        
        # Update and draw all particles
        for p in particles:
            p['x'] += p['vx']
            p['y'] += p['vy']
            p['life'] -= 1
            
            # Draw particle
            alpha = py5.remap(p['life'], 0, 60, 0, 255)
            py5.fill(p['color'][0], p['color'][1], p['color'][2], alpha)
            py5.no_stroke()
            py5.circle(p['x'], p['y'], p['size'])
        
        # Remove dead particles (list comprehension)
        particles[:] = [p for p in particles if p['life'] > 0]
        
        # Display count
        py5.fill(255)
        py5.text(f"Particles: {len(particles)}", 10, 20)
        py5.text("Click to add particles", 10, 40)
    
    def mouse_pressed():
        # Add burst of particles
        for _ in range(20):
            particles.append({
                'x': py5.mouse_x,
                'y': py5.mouse_y,
                'vx': random.uniform(-3, 3),
                'vy': random.uniform(-3, 3),
                'size': random.uniform(3, 8),
                'life': 60,
                'color': (random.randint(100, 255), 
                         random.randint(100, 255), 
                         random.randint(200, 255))
            })
    
    py5.run_sketch()


# =============================================================================
# EXAMPLE 2: DICTIONARIES - Game Entities
# =============================================================================

def example_2_dictionaries():
    """
    Game entities with properties stored as dictionaries.
    Click to spawn enemy. SPACE to spawn player projectile.
    """
    player = {
        'x': 300,
        'y': 350,
        'size': 20,
        'color': (0, 200, 100),
        'health': 100,
        'speed': 5
    }
    
    enemies = []
    projectiles = []
    
    def setup():
        py5.size(600, 400)
    
    def draw():
        py5.background(30)
        
        # Move player with arrow keys
        if py5.is_key_pressed:
            if py5.key_code == py5.LEFT:
                player['x'] = max(player['size'], player['x'] - player['speed'])
            if py5.key_code == py5.RIGHT:
                player['x'] = min(600 - player['size'], player['x'] + player['speed'])
        
        # Draw player
        py5.fill(*player['color'])
        py5.rect(player['x'] - player['size']/2, player['y'], player['size'], player['size'])
        
        # Update and draw enemies
        for enemy in enemies[:]:
            enemy['y'] += enemy['speed']
            py5.fill(*enemy['color'])
            py5.circle(enemy['x'], enemy['y'], enemy['size'])
            
            # Remove if off screen
            if enemy['y'] > 400:
                enemies.remove(enemy)
        
        # Update projectiles
        for proj in projectiles[:]:
            proj['y'] -= 10
            py5.fill(255, 255, 0)
            py5.circle(proj['x'], proj['y'], 5)
            
            # Check collision with enemies
            for enemy in enemies[:]:
                dist = py5.dist(proj['x'], proj['y'], enemy['x'], enemy['y'])
                if dist < enemy['size']:
                    enemy['health'] -= 20
                    if enemy['health'] <= 0:
                        enemies.remove(enemy)
                    if proj in projectiles:
                        projectiles.remove(proj)
            
            if proj['y'] < 0:
                projectiles.remove(proj)
        
        # UI
        py5.fill(255)
        py5.text(f"Health: {player['health']}", 10, 20)
        py5.text(f"Enemies: {len(enemies)}", 10, 40)
        py5.text("Arrow keys to move, SPACE to shoot, Click to spawn enemy", 10, 380)
    
    def mouse_pressed():
        enemies.append({
            'x': py5.mouse_x,
            'y': 50,
            'size': 30,
            'speed': random.uniform(1, 3),
            'health': 40,
            'color': (255, 50, 50)
        })
    
    def key_pressed():
        if py5.key == ' ':
            projectiles.append({'x': player['x'], 'y': player['y']})
    
    py5.run_sketch()


# =============================================================================
# EXAMPLE 3: SETS - Collision Detection
# =============================================================================

def example_3_sets():
    """
    Visual grid using sets to track occupied cells.
    Click to toggle cells. Shows fast set operations.
    """
    cell_size = 20
    active_cells = set()  # Set of (x, y) tuples
    
    def setup():
        py5.size(600, 400)
    
    def draw():
        py5.background(20)
        
        # Draw grid
        py5.stroke(60)
        for x in range(0, 600, cell_size):
            py5.line(x, 0, x, 400)
        for y in range(0, 400, cell_size):
            py5.line(0, y, 600, y)
        
        # Draw active cells
        py5.no_stroke()
        for cell in active_cells:
            x, y = cell
            py5.fill(0, 200, 255)
            py5.rect(x * cell_size, y * cell_size, cell_size, cell_size)
        
        # Highlight current cell
        if 0 <= py5.mouse_x < 600 and 0 <= py5.mouse_y < 400:
            grid_x = py5.mouse_x // cell_size
            grid_y = py5.mouse_y // cell_size
            
            if (grid_x, grid_y) in active_cells:
                py5.fill(255, 0, 0, 100)
            else:
                py5.fill(0, 255, 0, 100)
            
            py5.rect(grid_x * cell_size, grid_y * cell_size, cell_size, cell_size)
        
        # UI
        py5.fill(255)
        py5.text(f"Active cells: {len(active_cells)}", 10, 20)
        py5.text("Click to toggle cells | 'C' to clear | 'R' for random", 10, 380)
    
    def mouse_pressed():
        grid_x = py5.mouse_x // cell_size
        grid_y = py5.mouse_y // cell_size
        cell = (grid_x, grid_y)
        
        # Toggle cell (set operation)
        if cell in active_cells:
            active_cells.remove(cell)
        else:
            active_cells.add(cell)
    
    def key_pressed():
        if py5.key == 'c':
            active_cells.clear()
        elif py5.key == 'r':
            # Random pattern
            for _ in range(100):
                x = random.randint(0, 29)
                y = random.randint(0, 19)
                active_cells.add((x, y))
    
    py5.run_sketch()


# =============================================================================
# EXAMPLE 4: TUPLES - Constellation Drawing
# =============================================================================

def example_4_tuples():
    """
    Click to create stars (immutable positions as tuples).
    Stars automatically connect when close enough.
    """
    stars = []  # List of (x, y) tuples
    connection_dist = 100
    
    def setup():
        py5.size(600, 400)
        py5.background(10, 10, 30)
    
    def draw():
        py5.background(10, 10, 30)
        
        # Draw connections
        py5.stroke(100, 100, 200, 100)
        for i, star1 in enumerate(stars):
            for star2 in stars[i+1:]:
                dist = py5.dist(star1[0], star1[1], star2[0], star2[1])
                if dist < connection_dist:
                    py5.line(star1[0], star1[1], star2[0], star2[1])
        
        # Draw stars
        py5.no_stroke()
        py5.fill(255, 255, 200)
        for star in stars:
            x, y = star  # Tuple unpacking
            py5.circle(x, y, 8)
        
        # UI
        py5.fill(255)
        py5.text(f"Stars: {len(stars)}", 10, 20)
        py5.text("Click to add stars | 'C' to clear", 10, 380)
    
    def mouse_pressed():
        # Store position as immutable tuple
        stars.append((py5.mouse_x, py5.mouse_y))
    
    def key_pressed():
        if py5.key == 'c':
            stars.clear()
    
    py5.run_sketch()


# =============================================================================
# EXAMPLE 5: NESTED STRUCTURES - Simple Inventory
# =============================================================================

def example_5_nested():
    """
    Visual inventory system using nested dictionaries.
    Click on items to select/use them.
    """
    inventory = [
        {'name': 'Sword', 'color': (200, 200, 200), 'count': 1, 'type': 'weapon'},
        {'name': 'Potion', 'color': (255, 100, 100), 'count': 5, 'type': 'consumable'},
        {'name': 'Shield', 'color': (100, 100, 200), 'count': 1, 'type': 'armor'},
        {'name': 'Gem', 'color': (100, 255, 100), 'count': 12, 'type': 'material'}
    ]
    
    selected = None
    
    def setup():
        py5.size(600, 400)
    
    def draw():
        py5.background(40, 40, 50)
        
        # Draw inventory slots
        slot_size = 80
        margin = 20
        
        for i, item in enumerate(inventory):
            x = margin + (i % 4) * (slot_size + margin)
            y = margin + (i // 4) * (slot_size + margin)
            
            # Highlight if selected
            if selected == i:
                py5.fill(255, 255, 0, 100)
                py5.stroke(255, 255, 0)
            else:
                py5.fill(60, 60, 70)
                py5.stroke(100)
            
            py5.rect(x, y, slot_size, slot_size)
            
            # Draw item
            py5.fill(*item['color'])
            py5.no_stroke()
            py5.circle(x + slot_size/2, y + slot_size/2, 40)
            
            # Draw count
            py5.fill(255)
            py5.text_align(py5.RIGHT, py5.BOTTOM)
            py5.text(str(item['count']), x + slot_size - 5, y + slot_size - 5)
            
            # Draw name
            py5.text_align(py5.CENTER, py5.TOP)
            py5.text(item['name'], x + slot_size/2, y + slot_size + 5)
        
        # Show selected item info
        if selected is not None:
            item = inventory[selected]
            py5.fill(255)
            py5.text_align(py5.LEFT, py5.TOP)
            py5.text(f"Selected: {item['name']}", 20, 300)
            py5.text(f"Type: {item['type']}", 20, 320)
            py5.text(f"Count: {item['count']}", 20, 340)
            py5.text("Press SPACE to use/consume", 20, 360)
        
        py5.text_align(py5.LEFT, py5.TOP)
        py5.text("Click items to select", 20, 380)
    
    def mouse_pressed():
        nonlocal selected
        slot_size = 80
        margin = 20
        
        for i in range(len(inventory)):
            x = margin + (i % 4) * (slot_size + margin)
            y = margin + (i // 4) * (slot_size + margin)
            
            if x <= py5.mouse_x <= x + slot_size and y <= py5.mouse_y <= y + slot_size:
                selected = i
                break
    
    def key_pressed():
        nonlocal selected
        if py5.key == ' ' and selected is not None:
            item = inventory[selected]
            if item['type'] == 'consumable' and item['count'] > 0:
                item['count'] -= 1
                if item['count'] == 0:
                    selected = None
    
    py5.run_sketch()


# =============================================================================
# EXAMPLE 6: DEQUE - Snake Game
# =============================================================================

def example_6_deque():
    """
    Classic snake game using deque for efficient head/tail operations.
    Arrow keys to move. Eat the red food!
    """
    from collections import deque
    
    cell_size = 20
    snake = deque([(10, 10), (9, 10), (8, 10)])  # Positions as tuples
    direction = (1, 0)  # Moving right
    food = (15, 15)
    score = 0
    game_over = False
    frame_count = 0
    
    def setup():
        py5.size(600, 400)
        py5.frame_rate(10)  # Slower for snake game
    
    def draw():
        nonlocal food, score, game_over, frame_count
        
        py5.background(30)
        
        if not game_over:
            # Move snake every frame
            head = snake[0]
            new_head = (head[0] + direction[0], head[1] + direction[1])
            
            # Check collisions
            if (new_head[0] < 0 or new_head[0] >= 30 or 
                new_head[1] < 0 or new_head[1] >= 20 or
                new_head in snake):
                game_over = True
            else:
                snake.appendleft(new_head)  # Add to front (deque operation)
                
                # Check if ate food
                if new_head == food:
                    score += 1
                    food = (random.randint(0, 29), random.randint(0, 19))
                else:
                    snake.pop()  # Remove tail (deque operation)
        
        # Draw grid
        py5.stroke(50)
        for x in range(0, 600, cell_size):
            py5.line(x, 0, x, 400)
        for y in range(0, 400, cell_size):
            py5.line(0, y, 600, y)
        
        # Draw snake
        py5.no_stroke()
        for i, segment in enumerate(snake):
            brightness = 255 - (i * 10) if i < 25 else 5
            py5.fill(0, brightness, 0)
            py5.rect(segment[0] * cell_size, segment[1] * cell_size, 
                    cell_size, cell_size)
        
        # Draw food
        py5.fill(255, 0, 0)
        py5.circle(food[0] * cell_size + cell_size/2, 
                  food[1] * cell_size + cell_size/2, cell_size - 4)
        
        # UI
        py5.fill(255)
        py5.text(f"Score: {score} | Length: {len(snake)}", 10, 20)
        
        if game_over:
            py5.text_align(py5.CENTER, py5.CENTER)
            py5.text_size(32)
            py5.fill(255, 0, 0)
            py5.text("GAME OVER", 300, 200)
            py5.text_size(12)
    
    def key_pressed():
        nonlocal direction
        if py5.key_code == py5.UP and direction != (0, 1):
            direction = (0, -1)
        elif py5.key_code == py5.DOWN and direction != (0, -1):
            direction = (0, 1)
        elif py5.key_code == py5.LEFT and direction != (1, 0):
            direction = (-1, 0)
        elif py5.key_code == py5.RIGHT and direction != (-1, 0):
            direction = (1, 0)
    
    py5.run_sketch()


# =============================================================================
# Run examples - uncomment one at a time
# =============================================================================

if __name__ == "__main__":
    print("Python Data Structures with py5")
    print("=" * 50)
    print("Uncomment one example at a time to run:")
    print()
    print("1. Lists - Particle System")
    print("2. Dictionaries - Game Entities")
    print("3. Sets - Grid Collision")
    print("4. Tuples - Constellation")
    print("5. Nested - Inventory System")
    print("6. Deque - Snake Game")
    print()
    
    # Uncomment ONE of these to run:
    
    example_1_lists()
    # example_2_dictionaries()
    # example_3_sets()
    # example_4_tuples()
    # example_5_nested()
    # example_6_deque()