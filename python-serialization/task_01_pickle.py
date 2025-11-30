#!/usr/bin/python3
"""CustomObject class with pickle serialization and deserialization."""

import pickle


class CustomObject:
    """Represents a custom object with name, age, and is_student attributes."""

    def __init__(self, name, age, is_student):
        """Initialize a new CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the attributes of the object."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object instance to a file using pickle.

        Args:
            filename (str): The name of the file to save the object to.

        Returns:
            None
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject instance from a pickle file.

        Args:
            filename (str): The name of the file to load the object from.

        Returns:
            CustomObject: The deserialized object, or None if an error occurs.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
            return None
        except (OSError, pickle.PickleError):
            return None
