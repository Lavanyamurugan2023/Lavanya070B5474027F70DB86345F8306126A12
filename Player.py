class Player:
    def __init__(self, name, age, skills, style=None):
        self.name = name
        self.age = age
        self.skills = skills
        self.style = style

    def __str__(self):
        return f"{self.name} {self.age} {self.skills} {self.style or ''}"


class Team:
    def __init__(self, name, players=None):
        self.name = name
        if players is not None:
            self._players = list(players)
        else:
            self._players = []

    def add_player(self, obj):
        if isinstance(obj, Player):
            self._players.append(obj)
        else:
            print("Please provide player object")

    def __iter__(self):
        return iter(self._players)

    def __str__(self):
        out = [f"Team name: {self.name}", "Players:"]
        out.extend(str(player) for player in self)
        return "\n".join(out)


if __name__ == "__main__":

    players = [Player("Mahendra", 46, "Wicket Kipper", "Right-Hand Batsman"),
               Player("Sachin", 35, "Batsman", "Right-Hand Batsman"),
               Player("Saurabh", 44, "Batsman", "Left-Hand Batsman"),
               Player("Zahir", 38, "Bauwller", "Medium Pace Bauwller"),
               Player("Yuvraj", 43, "All rounder")]

    india = Team("India", players)
    print(india)

    # equivalent:
    print("Team name:", india.name)
    print("Players:")
    for player in india:
        print(player)