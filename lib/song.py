class Song():
    count=0
    genres=[]
    artists=[]
    genre_count={}
    artist_count={}
    def __init__(self,name,artist,genre) -> None:
        super().__init__()
        self.name=name
        self.artist=artist
        self.genre=genre
        Song.add_song_to_count(self)
    @classmethod
    def add_song_to_count(cls,song):
        cls.count+=1
        cls.genres.append(song.genre)
        cls.artists.append(song.artist)
        if song.genre in cls.genre_count.keys():
            cls.genre_count[song.genre]+=1
        else:
            cls.genre_count[song.genre]=1
        if song.artist in cls.artist_count.keys():
            cls.artist_count[song.artist]+=1
        else:
            cls.artist_count[song.artist]=1



