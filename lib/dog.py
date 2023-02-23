#!/usr/bin/env python3

class Dog:

    # Defining name property

    def get_name(self):
        print("Retrieving name.")
        return self._name
    def set_name(self, name):
        if (type(name) == str and (1 <= len(name) <= 25)):
            print(f"Setting name to {name}.")
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
    name = property(get_name, set_name)

    # Defining breed property

    def get_breed(self):
        print("Retrieving breed.")
        return self._breed
    def set_breed(self, breed):
        approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", 
                           "Beagle", "French Bulldog", "Pug", "Pointer"]
        if breed in approved_breeds:
            print(f"Setting breed to {breed}.")
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
        
    breed = property(get_breed, set_breed)




