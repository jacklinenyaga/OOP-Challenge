class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting at midpoint
        self.energy = 5   # Starting at midpoint
        self.happiness = 5  # Starting at midpoint
        self.tricks = []   # For storing learned tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food. Hunger decreased, happiness increased!")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap. Energy increased!")

    def play(self):
        if self.energy >= 2:  # Only play if there's enough energy
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played happily!")
        else:
            print(f"{self.name} is too tired to play. Try sleeping first!")

    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        if self.tricks:
            print(f"Known tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    # Bonus methods
    def train(self, trick):
        if self.energy >= 3:  # Training requires energy
            self.tricks.append(trick)
            self.energy = max(0, self.energy - 3)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} is too tired to train. Try sleeping first!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

if __name__ == "__main__":
    my_pet = Pet("Pax")
    
    print("Welcome to the Pet Simulator!")
    my_pet.get_status()
    
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()
    my_pet.get_status()
    
    # Bonus features
    my_pet.train("sit")
    my_pet.train("roll over")
    my_pet.show_tricks()
    my_pet.get_status()

