class Cat:

    def __init__(self, name):
        self.name = name
        self.animal_type = "Mammal"

    def play(self):
        print(self.name, "plays")

    def details(self):
        print(self.name, "is a", self.animal_type)


tommy = Cat("Tommy")
jordan = Cat("Jordan")

tommy.play()
jordan.play()

tommy.details()
jordan.details()