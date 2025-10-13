brain = {"ok":[]}

def add_to_brain(sentence:str):
    words = sentence.split(" ")
    for i in range(len(words) - 1):
        word = words[i]
        after = words[i + 1]
        if word in brain.keys():
            after_list = brain[words]
            if not after in after_list:
                after_list.add(after)
                    

print("Speak now or forever hold your peace!")
while True:
    sentence = input(">")
    add_to_brain(sentence)
    print_brain()