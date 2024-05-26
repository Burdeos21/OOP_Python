from abc import ABC, abstractmethod
# Import the Abstract Base Class (ABC) and abstractmethod decorator from the "abc" module to create abstract classes.

class Animal(ABC):
    # Create an abstract base class named "Animal".

    def __init__(self, name, species):
        # Constructor to initialize the name and species of the animal.
        self._name = name
        # Set a private instance variable "_name" to hold the animal's name.
        self._species = species
        # Set a private instance variable "_species" to hold the animal's species.

    @abstractmethod
    def sound(self):
        # Abstract method for the sound the animal makes. This method is intended to be overridden in subclasses.
        pass

    @abstractmethod
    def habitat(self):
        # Abstract method for the habitat of the animal. This method is intended to be overridden in subclasses.
        pass

    def info(self):
        # Method to return a formatted string with the animal's name and species.
        return f"{self._name} ({self._species})"

class Mammal(Animal):
    # Create a subclass of "Animal" called "Mammal".

    def sound(self):
        # Override the "sound" method to return a generic mammal sound.
        return "Generic mammal sound"

    def habitat(self):
        # Override the "habitat" method to return a generic description for mammal habitats.
        return "Varies for mammals"

class Bird(Animal):
    # Create a subclass of "Animal" called "Bird".

    def sound(self):
        # Override the "sound" method to return bird-specific sounds.
        return "Chirping and singing"

    def habitat(self):
        # Override the "habitat" method to return typical habitats for birds.
        return "Nests and trees"

class Reptile(Animal):
    # Create a subclass of "Animal" called "Reptile".

    def sound(self):
        # Override the "sound" method to return reptile-specific sounds.
        return "Hiss or growl"

    def habitat(self):
        # Override the "habitat" method to return typical habitats for reptiles.
        return "Desert or tropical regions"

class Elephant(Mammal):
    # Create a subclass of "Mammal" called "Elephant".

    def sound(self):
        # Override the "sound" method to return the sound elephants make.
        return "Trumpeting"

    def habitat(self):
        # Override the "habitat" method to return the common habitats for elephants.
        return "Savannah or forest"

class Parrot(Bird):
    # Create a subclass of "Bird" called "Parrot".

    def sound(self):
        # Override the "sound" method to return the sound parrots make.
        return "Mimicry and squawking"

    def habitat(self):
        # Override the "habitat" method to return the common habitat for parrots.
        return "Tropical rainforest"

class Snake(Reptile):
    # Create a subclass of "Reptile" called "Snake".

    def sound(self):
        # Override the "sound" method to return the sound snakes make.
        return "Ssssssss"

    def habitat(self):
        # Override the "habitat" method to return the typical habitat for snakes.
        return "Deserts, forests, and wetlands"

def show_animal_info(animals):
    # Function that takes a list of animals and displays their information.
    for animal in animals:
        # Loop through each animal in the given list.
        print(f"{animal.info()} - Sound: {animal.sound()}, Habitat: {animal.habitat()}")
        # Print the animal's information, including name, sound, and habitat.

elephant = Elephant("Zel", "Elephant")
# Create an instance of "Elephant" with name "Zel" and species "Elephant".
parrot = Parrot("Jason", "Parrot")
# Create an instance of "Parrot" with name "Jason" and species "Parrot".
snake = Snake("Joshua", "Snake")
# Create an instance of "Snake" with name "Joshua" and species "Snake".
animal_list = [elephant, parrot, snake]
# Create a list containing the created animal instances.

show_animal_info(animal_list)
# Call the "show_animal_info" function with the list of animals to display their information.
