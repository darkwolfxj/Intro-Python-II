class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.value = value
        self.description = description
    def look(self):
        print(f"This is a {self.name}. {self.description} It's worth {self.value} points!")
    def __repr__(self):
        name = str(self.name)
        return name