import webbrowser

class Movie():

    # Constructor to populate instance variables of a movie object
    def __init__(self, movie_title, image_url, trailer_youtube_link):
        self.title = movie_title
        self.box_art_url = image_url
        self.trailer_url = trailer_youtube_link

    # Method to show movie trailer on YouTube upon clicking box art
    def open_trailer(self):
  wser.open(self.trailer)      webbro