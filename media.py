"""
Movie object  
- title
- storyline
- poster url
- trailer url
"""

class Movie:

    def __init__(self, title):
        self.title = title
        self.storyline = ""
        self.poster_url = ""
        self.trailer_url = ""
