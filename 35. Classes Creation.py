class BoardingGame:
    """Class representing a boarding game."""
    num_players = 0
    def __init__(self, name, players, difficulty):
        """Initialize a boarding game object with name, number of players, and difficulty."""
        self.name = name
        self.players = players
        self.difficulty = difficulty
        BoardingGame.num_players += players
    def display_info(self):
        """Display information about the boarding game."""
        return f"The {self.name} is a fun game for {self.players} players with difficulty {self.difficulty}."
    def change_difficulty(self, new_difficulty):
        """Change the difficulty of the boarding game."""
        self.difficulty = new_difficulty
        return f"The difficulty of {self.name} has been changed to {self.difficulty}."
    @classmethod
    def get_num_players(cls):
        """Get the total number of players in all boarding games."""
        return f"Total number of players in all boarding games: {cls.num_players}"
    @staticmethod
    def instructions():
        """Display instructions for playing the boarding game."""
        return "Read the instruction and have exciting game!"

class Smartphone:
    """Class representing a smartphones."""
    num_smartphones = 0
    def __init__(self, brand, model, color):
        """Initialize a smartphone object with brand, model, and software."""
        self.brand = brand
        self.model = model
        self.color = color
        Smartphone.num_smartphones += 1
    def display_info(self):
        """Display information about the smartphones."""
        return f"This is a {self.color} {self.brand} {self.model}."
    def paint(self, new_color):
        """Change the color of the smartphone."""
        self.color = new_color
        return f"I changed the color of {self.brand} {self.model} to {self.color}."
    @classmethod
    def get_num_smartphones(cls):
        """Get the total number of smartphones created."""
        return f"Total number of smartphones: {cls.num_smartphones}"
    @staticmethod
    def phone_ring():
        """Make a phone ring."""
        return "Dzelin dzelin!"

boarding_game1 = BoardingGame("Yamatai", 4, "easy")
boarding_game2 = BoardingGame("Eldritch Horror", 8, "medium")

smartphone1 = Smartphone("iPhone", "13 Pro Max", "silver")
smartphone2 = Smartphone("Samsung", "Galaxy S3", "black")

print(boarding_game1.display_info())
print(boarding_game2.change_difficulty("hard"))
print(BoardingGame.get_num_players())
print(BoardingGame.instructions())

print(smartphone1.display_info())
print(smartphone2.paint("pink"))
print(Smartphone.get_num_smartphones())
print(Smartphone.phone_ring())
