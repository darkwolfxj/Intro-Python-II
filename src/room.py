# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
    def __repr__(self):
        return f"You are currently in the {self.name} room. {self.desc}"