import py5

players = ["bryan", "mary", "peter", "mari", "michael"]
health = [100, 250, 300, 500, 20]

print(len(players))

print(players[0] + " is top of the list")
print(f"{players[0]} is top of the list")
print(f"{players[0]} health is {health[0]}")

players.append("senan")
health.append(134)

for i in range(len(players)):
    print(f"{players[i]} health is {health[i]}")

lowest_health = min(health)

lowest_index = 0
for i in range(len(health)):
    if health[i] < health[lowest_index]:
        lowest_index = i

print(f"{players[lowest_index]} has the lowest health")

highest_index = 0
for i in range(len(health)):
    if health[i] > health[highest_index]:
        highest_index = i

for i in range(len(players) -1, -1, -1):
    print(f"{players[i]} {health[i]}")

s = "I love pythin"

love = s[2:6]

print(love)

loveb = s[6: 2: -1]
print(love)

# dictionary
bryan = {"name" : "Bryan", "health" : 100, "armor": 60}

print(bryan["name"])
print(bryan["health"])
print(bryan["armor"])

all_players = [{"name": "Pat", "health": 60, "armor": 80}]
all_players.append(bryan)

for i in range(len(all_players)):
    print(f"{all_players[i]["name"]}")
    print(f"{all_players[i]["health"]}")
    print(f"{all_players[i]["armor"]}")

s = "Grace Murry Hopper"

names = s.split(" ")

for i in range(len(names)):
    print(names[i])

for n in names:
    print(n)


if s.startswith("Grace"):
    print("I invented COBOL")

s_lower = s.lower()
print(s_lower)

power_ups = [{"x": 100, "y": 200}, 
             {"x": 200, "y": 150},
             {"x": 50, "y": 20},
             {"x": 150, "y": 90},
            ]

def setup():
    py5.size(500, 500)

def draw():
    global power_ups
    for i in range(len(power_ups)):
        power = power_ups[i]
        py5.circle(power["x"], power["y"], 50)
    
py5.run_sketch()
