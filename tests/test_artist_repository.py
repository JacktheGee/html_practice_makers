from lib.artist_repository import ArtistRepository
from lib.artist import Artist

def test_get_all_records(db_connection):
    db_connection.seed("seeds/flask_exercise_seed.sql")
    repository = ArtistRepository(db_connection)

    artists = repository.all()

    assert artists == [
        Artist(1, "Childish Gambino"),
        Artist(2, "Bring Me The Horizon"),
        Artist(3, "Mac Miller"),
        Artist(4, "Blink-182"),
        Artist(5, "Zeds Dead")
    ]

def test_get_single_record(db_connection):
    db_connection.seed("seeds/flask_exercise_seed.sql")
    repository = ArtistRepository(db_connection)

    artist = repository.find(3)

    assert artist == Artist(3, "Mac Miller")

def test_create_record(db_connection):
    db_connection.seed("seeds/flask_exercise_seed.sql")
    repository = ArtistRepository(db_connection)

    repository.create(Artist(None, "Bullet For My Valentine"))

    result = repository.all()
    assert result == [
        Artist(1, "Childish Gambino"),
        Artist(2, "Bring Me The Horizon"),
        Artist(3, "Mac Miller"),
        Artist(4, "Blink-182"),
        Artist(5, "Zeds Dead"),
        Artist(6, "Bullet For My Valentine")
    ]

def test_delete_record(db_connection):
    db_connection.seed("seeds/flask_exercise_seed.sql")
    repository = ArtistRepository(db_connection)

    repository.delete(3)

    result = repository.all()
    assert result == [
        Artist(1, "Childish Gambino"),
        Artist(2, "Bring Me The Horizon"),
        Artist(4, "Blink-182"),
        Artist(5, "Zeds Dead")
    ]