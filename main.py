
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        self.energy = min(10, self.energy + 5)

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
        else:
            print(f"{self.name} is too tired to play!")

    def get_status(self):
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks:")
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")


#from pet import Pet  # Assuming your Pet class is saved in pet.py

if __name__ == "__main__":
    my_pet = Pet("Buddy")  # Creating a pet object

    # Check initial status
    my_pet.get_status()

    # Test various actions
    my_pet.eat()
    my_pet.get_status()

    my_pet.sleep()
    my_pet.get_status()

    my_pet.play()
    my_pet.get_status()

    # Train a new trick
    my_pet.train("Roll over")
    my_pet.train("Fetch")

    # Show learned tricks
    my_pet.show_tricks()
