from lib.album import Album

def test_album_constructs():
    album = Album(1, "Test Name", 2026, 1)
    assert album.id == 1
    assert album.album_name == "Test Name"
    assert album.release_year == 2026
    assert album.artist_id == 1

def test_album_format_nicely():
    album = Album(1, "Test Title", 2026, 1)
    assert str(album) == "Album(1, Test Title, 2026, 1)"

def test_albums_format_nicely():
    album1 = Album(1, "Test Title", 2026, 1)
    album2 = Album(1, "Test Title", 2026, 1)
    assert album1 == album2