import pyttsx3

engine = pyttsx3.init()

class Cat:
    def __init__(self, name, age): # constructor
        self.name = name # fields
        self.age = age

    def speak(self):
        message = f"{self.name} says meaow meaow meaow meaow!"
        print(message)
        engine.say(message)
        engine.runAndWait()


class Dog:
    def __init__(self, name, age): # constructor
        self.name = name # fields
        self.age = age

    def speak(self):
        message = f"{self.name} says woof woof woof woof woof!"
        print(message)
        engine.say(message)
        engine.runAndWait()

lucy = Dog("Lucy", 5)

lucy.speak()

john = Dog("John", 20)
john.speak()

annie = Cat("Annie", 3)

annie.speak()

topcat = Cat("Topcat", 3)

topcat.speak()