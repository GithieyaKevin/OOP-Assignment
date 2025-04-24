from pet import Pet  # Assuming your Pet class is saved in pet.py

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