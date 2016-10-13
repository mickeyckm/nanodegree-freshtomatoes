import os
import tmdbsimple as tmdb
import media
import fresh_tomatoes as ft

movies = []

if os.environ.get('TMDB_API', False):
    # Retrieve API KEY
    tmdb.API_KEY = os.environ['TMDB_API']

    # TMDB Movie Ids
    movie_ids = [271110, 297761, 246655, 278154, 135397, 188927]

    # Get Configuration
    configuration = tmdb.Configuration().info()
    image_base_url = configuration['images']['secure_base_url']
    image_width = "w500"

    for movie_id in movie_ids:
        m = tmdb.Movies(movie_id)

        # Retrieve Image URL
        minfo = m.info()
        poster_image_url = image_base_url + image_width + minfo['poster_path']

        # Retrieve Youtube Video URL
        videos = m.videos()
        video = videos['results'][0]
        youtube_url = 'https://youtube.com/watch?v=' + video['key']
        
        # Append Movie object
        movie = media.Movie(m.title, m.overview, poster_image_url, youtube_url)
        movies.append(movie)

else:
    avatar = media.Movie("Avatar", "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=-9ceBgWV8io")
    deadpool = media.Movie("Deadpool", "A fast-talking mercenary with a morbid sense of humor is subjected to a rogue experiment that leaves him with accelerated healing powers and a quest for revenge.", "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg", "https://www.youtube.com/watch?v=gtTfd6tISfw")
    ghostbusters = media.Movie("Ghostbusters", "Following a ghost invasion of Manhattan, paranormal enthusiasts Erin Gilbert and Abby Yates, nuclear engineer Jillian Holtzmann, and subway worker Patty Tolan band together to stop the otherworldly threat.", "https://upload.wikimedia.org/wikipedia/en/3/32/Ghostbusters_2016_film_poster.png", "https://www.youtube.com/watch?v=w3ugHP-yZXw")
    olympus = media.Movie("Olympus Has Fallen", "Disgraced Secret Service agent (and former presidential guard) Mike Banning finds himself trapped inside the White House in the wake of a terrorist attack; using his inside knowledge, Banning works with national security to rescue the President from his kidnappers.", "https://upload.wikimedia.org/wikipedia/en/b/bf/Olympus_Has_Fallen_poster.jpg", "https://www.youtube.com/watch?v=vwx1f0kyNwI")
    angry_birds = media.Movie("The Angry Birds Movie", "Find out why the birds are so angry. When an island populated by happy, flightless birds is visited by mysterious green piggies, it's up to three unlikely outcasts - Red, Chuck and Bomb - to figure out what the pigs are up to.", "https://upload.wikimedia.org/wikipedia/en/f/f9/The_Angry_Birds_Movie_poster.png", "https://www.youtube.com/watch?v=1U2DKKqxHgE")
    iron_man = media.Movie("Iron Man", "After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil.", "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG", "https://www.youtube.com/watch?v=8hYlB38asDY")

    movies = [avatar, deadpool, ghostbusters, olympus, angry_birds, iron_man]

ft.open_movies_page(movies)