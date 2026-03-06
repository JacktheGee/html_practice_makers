-- First need to drop all tables if they exist
-- Drop foreign tables first to prevent orphan data being created
DROP TABLE IF EXISTS albums cascade;
DROP TABLE IF EXISTS artists cascade;

-- Then recreate from scratch - Add as many columns as needed
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    artist_name text);

-- <name>_id is the foreign key and should point to the primary db - 'contraint...' is the fk rules
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    album_name text,
    release_year int,
    artist_id int,
-- Foreign key convention is typical singular
    constraint fk_artist foreign key (artist_id)
    references artists(id)
    on delete cascade);

INSERT INTO artists (artist_name)
VALUES
	('Childish Gambino'),
	('Bring Me The Horizon'),
	('Mac Miller'),
    ('Blink-182'),
    ('Zeds Dead');


INSERT INTO albums (album_name, release_year, artist_id)
VALUES
	('Camp', 2011, 1),
    ('Because the Internet', 2013, 1),
	('Sempiternal', 2013, 2),
    ('Swimming', 2018, 3),
    ('K.I.D.S', 2010, 3),
    ('Enema of the State', 1999, 4),
    ('Return to the Spectrum of Intergalactic Happiness', 2025, 5);
	
-- Replace <name> with primary db name
-- Replace <name2> with foreign db name
