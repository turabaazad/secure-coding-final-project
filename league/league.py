"""
Description: {description of the file.}
Author: Turaba Turaba
"""
from team.team import Team

class League:
    """
    A class to represent a league.
    """

    def __init__(self, name):
        """
        Constructs all the necessary attributes for the league object.

        Args: 
            name (str): The name of the league.

        Raises:
            ValueError: If the name is not a string.
        """
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        
        self.__name = name
        self.__teams = []

    @property
    def name(self):
        """
        To Do:Document this method.
        """
        return self.__name

    @property
    def teams(self):
        """
        Gets the list of teams in the league.
        
        Returns:
            A list of Team objects.
        """
        return self.__teams

    def add_team(self, team):
        """
        Adds a team to the league.

        Args:
            team (Team): The team to be added to the league.
        
        Raises:
            ValueError: If the team is not an instance of Team.
        """
        if not isinstance(team, Team):
            raise ValueError("team must be an instance of Team")
        
        self.__teams.append(team)

    def __str__(self):
        """
        Returns a string representation of the league.

        Returns
            str: A string containing the league's details.
        """
        team_details = ', '.join(str(team) for team in self.__teams)
        return f"League: {self.__name}, Teams: [{team_details}]"