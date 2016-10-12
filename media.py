"""
Movie object  
- title
- storyline
- poster url
- trailer url
"""

class Movie:

    def __init__(self, title, storyline, poster_url, trailer_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url