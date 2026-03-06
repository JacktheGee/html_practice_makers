from lib.artist import Artist

def test_artist_constructs():
    artist = Artist(1, "Test Name")
    assert artist.id == 1
    assert artist.artist_name == "Test Name"

def test_artist_formats_nicely():
    artist = Artist(1, "Test Name")
    assert str(artist) == "Artist(1, Test Name)"

def test_artists_are_equal():
    artist1 = Artist(1, "Test Title")
    artist2 = Artist(1, "Test Title")
    assert artist1 == artist2