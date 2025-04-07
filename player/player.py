"""
Description: {description of the file.}
Author: Turaba Turaba
"""
class Player:
    """
    A class to represent a player.
    """

    def __init__(self, name, age, position):
        """
        Constructs all the necessary attributes for the player object.

        Args:
            name (str): The name of the player.
            age (int): The age of the player.
            position (str): The position of the player on the team.

        Raises
            ValueError: If the name is not a string, age is not an integer, or position is not a string.
        """
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not isinstance(age, int):
            raise ValueError("Age must be an integer")
        if not isinstance(position, str):
            raise ValueError("Position must be a string")
        
        self.__name = name
        self.__age = age
        self.__position = position

    @property
    def name(self):
        """
        Returns the name of the player.
        
        Returns:
            str: The name of the player instance.
        """
        return self.__name

    @property
    def age(self):
        """
        Returns the age of the player.
        
        Returns:
            int: The age of the player instance.
        """

        return self.__age

    @property
    def position(self):
        """
        Returns the position of the player.
        
        Returns:
            str: The position of the player instance.
        """

        return self.__position

    def __str__(self):
        """
        Returns a string representation of the player.

        Returns
            str: A string containing the player's details.
        """
        return f"Name: {self.__name}, Age: {self.__age}, Position: {self.__position}"