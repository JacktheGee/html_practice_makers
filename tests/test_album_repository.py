from lib.album_repository import AlbumRepository
from lib.album import Album

def test_get_all_records(db_connection):
    db_connection.seed("seeds/flask_exercise_seed.sql")
    repository = AlbumRepository(db_connection)

    albums = repository.all()

    assert albums == [
        Album(1, "Camp", 2011, 1),
        Album(2, "Because the Internet", 2013, 1),
        Album(3, "Sempiternal", 2013, 2),
        Album(4, "Swimming", 2018, 3),
        Album(5, "K.I.D.S", 2010, 3),
        Album(6, "Enema of the State", 1999, 4),
        Album(7, "Return to the Spectrum of Intergalactic Happiness", 2025, 5),
    ]

def test_get_single_record(db_connection):
    db_connection.seed("seeds/flask_exercise_seed.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find(3)

    assert album == Album(3, "Sempiternal", 2013, 2)

def test_create_record(db_connection):
    db_connection.seed("seeds/flask_exercise_seed.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(None, "Atavista", 2024, 1))

    result = repository.all()

    assert result == [
        Album(1, "Camp", 2011, 1),
        Album(2, "Because the Internet", 2013, 1),
        Album(3, "Sempiternal", 2013, 2),
        Album(4, "Swimming", 2018, 3),
        Album(5, "K.I.D.S", 2010, 3),
        Album(6, "Enema of the State", 1999, 4),
        Album(7, "Return to the Spectrum of Intergalactic Happiness", 2025, 5),
        Album(8, "Atavista", 2024, 1),
    ]

def test_delete_record(db_connection):
    db_connection.seed("seeds/flask_exercise_seed.sql")
    repository = AlbumRepository(db_connection)

    repository.delete(3)
    result = repository.all()
    assert result == [
        Album(1, "Camp", 2011, 1),
        Album(2, "Because the Internet", 2013, 1),
        Album(4, "Swimming", 2018, 3),
        Album(5, "K.I.D.S", 2010, 3),
        Album(6, "Enema of the State", 1999, 4),
        Album(7, "Return to the Spectrum of Intergalactic Happiness", 2025, 5)
    ]