"""
Description: {description of the file.}
Author: Turaba Turaba
"""
from  player.player import Player

class Team:
    """
    A class to represent a team.
    """

    def __init__(self, name, city):
        """
        Constructs all the necessary attributes for the team object.

        Args:
            name (str): The name of the team.
            city (str): The city the team is based in.

        Raises: 
            ValueError: If the name is not a string, or city is not a string.
        """

        
        self.__name = name
        self.__city = city
        self.__players = []

    @property
    def name(self):
        """
        Returns the name of the team.
        
        Returns:
            str: The name of the team instance.
        """
        return self.__name

    @property
    def city(self):
        """
        Returns the city of the team.
        
        Returns:
            str: The city of the team instance.
        """
        return self.__city

    @property
    def players(self):
        """
        Returns a list of players on the team.
        
        Returns:
            list: A list of players on the team instance.
        """
        return self.__players

    def add_player(self, player):
        """
        Adds a player to the team.

        Args: 
            player (Player): The player to be added to the team.
        """
        
        self.__players.append(player)

    def __str__(self):
        """
        Returns a string representation of the team.

        Returns
            str: A string containing the team's details.
        """
        player_details = ', '.join(str(player) for player in self.__players)
        return f"Team: {self.__name}, City: {self.__city}, Players: [{player_details}]"