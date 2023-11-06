#Player class
class Player:
    def play(self):
        print("The player is playing cricket.")

#Batsman class inheriting from Player class
class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

#Bowler class inheriting from Player class
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

batsman = Batsman()
bowler = Bowler()

batsman.play()
bowler.play()
