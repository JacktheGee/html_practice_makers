class Artist:
    def __init__(self, id, artist_name):
        self.id = id
        self.artist_name = artist_name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Artist({self.id}, {self.artist_name})"