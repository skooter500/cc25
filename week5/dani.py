import random

brain = {"ok":[]}

def add_to_brain(sentence:str):
    words = sentence.split(" ")
    for i in range(len(words) - 1):
        word = words[i]
        after = words[i + 1]
        if word in brain.keys():
            after_list = brain[word]
            if after not in after_list:
                after_list.append(after)
        else:
            brain[word] = [after]

def generate_response(sentence):
    words = sentence.split(" ")
    r = random.randrange(0, len(words))
    word = words[r]
    if word 

def print_brain():
    global brain
    for key in brain.keys():
        print(f"{key}: {brain[key]}")

print("Speak now or forever hold your peace! Type 'list' to see my brain")
while True:
    sentence = input(">")
    if sentence == "list":
        print_brain()
    else:
        add_to_brain(sentence)
        response = generate_response(sentence)
        print(response)
    # print_brain()