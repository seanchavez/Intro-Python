# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, startRoom):
        self.room = startRoom
        self.items = []
        self.score = 0