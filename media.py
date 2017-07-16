import webbrowser

class Movie():

    # Constructor to populate instance variables of a movie object
    def __init__(self, movie_title, box_art_url, trailer_youtube_link):
        self.title = movie_title
        self.box_art = box_art_url
        self.trailer = trailer_youtube_link

    # Method to show movie trailer on YouTube upon clicking corresponding box art
    def open_trailer(self):
        webbrowser.open(self.trailer)