#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    # List of allowed dog breeds
    APPROVED_BREEDS = ["Pug", "Golden Retriever", "Mutt"]

    def __init__(self, name="Fido", breed="Mutt"):
        # Validate name: must be a string between 1 and 25 characters
        if not isinstance(name, str) or len(name) == 0 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            return
        self.name = name

        # Validate breed: must be in the approved list
        if breed in Dog.APPROVED_BREEDS:
            self.breed = breed
        else:
            print("Breed must be in list of approved breeds.")
            self.breed = "Unknown"
