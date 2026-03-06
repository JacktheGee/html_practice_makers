import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.album import Album

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/greet')
def greet():
    name = request.args.get('name')
    return render_template('greet.html', name=name)

@app.route('/goodbye', methods=['GET'])
def get_goodbye():
    return render_template('goodbye.html', goodbye='Bye!')

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    artists = repository.all()

    return ", ".join([artist.artist_name for artist in artists])

@app.route('/artists/<artist_id>', methods=['GET'])
def get_single_artist(artist_id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    artist = repository.find(artist_id)

    return artist.artist_name

@app.route('/albums/<album_id>', methods=['GET'])
def get_single_album(album_id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    album = repository.find(album_id)

    return album.album_name

@app.route('/albums', methods=['POST'])
def add_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    album_name = request.form['album_name']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']

    new_album = Album(None, album_name, release_year, artist_id)

    repository.create(new_album)

    return f"Added album: {album_name}"

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    albums = repository.all()

    return render_template("albums.html", albums=albums)
    # return ", ".join([album.album_name for album in albums])

# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
