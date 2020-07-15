class Task:
    def __init__(self, description, team):
        self.description = description
        self.team = team

    # create the method
    def __add__(self, other):
        description = self.description + '\n' + other.description
        team = self.team + ', ' + other.team
        return Task(description, team)
