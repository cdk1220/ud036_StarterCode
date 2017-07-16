import media
import fresh_tomatoes

def main():

    # Creating movie object for Inception
    inception = media.Movie('Inception',
                            "https://images-na.ssl-images-amazon.com/images/"
                            "M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw"
                            "@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            'https://www.youtube.com/watch?v=8hP9D6kZseM')

    # Creating movie object for Wonder Woman
    wonder_woman = media.Movie('Wonder Woman',
                               "http://t1.gstatic.com/images?q=tbn:ANd9GcQcCAOm"
                               "t-FsRsR8GebIzI67qSvdQ2JLYDRLxeAcbH-541fzqq1H",
                               'https://www.youtube.com/watch?v=VSB4wGIdDwo')

    # Creating movie object for Thor 3
    thor_3 = media.Movie('Thor 3',
                         "http://1.bp.blogspot.com/-_8wm66q6-8s/UnX5m5ilZII"
                         "/AAAAAAAATlQ/JPPV19LQS8M/s320/thor+s%C3%B6t%C3%A9"
                         "t+vil%C3%A1g.jpg",
                         'https://www.youtube.com/watch?v=F7ayGFHGqeQ')

    #Creating movie object for The Dark Knight
    the_dark_knight = media.Movie('The Dark Knight',
                                  "http://www.gstatic.com/tv/thumb/movie"
                                  "posters/173378/p173378_p_v8_au.jpg",
                                  'https://www.youtube.com/watch?v=EXeTwQWrcwY')

    #Creating movie object for Arrival
    arrival = media.Movie('Arrival',
                          "https://images-na.ssl-images-amazon.com/images/M/"
                          "MV5BMTExMzU0ODcxNDheQTJeQWpwZ15BbWU4MDE1OTI4MzAy."
                          "_V1_UX182_CR0,0,182,268_AL_.jpg",
                          'https://www.youtube.com/watch?v=tFMo3UJ4B4g')

    # Creating movie object for The Martian
    the_martian = media.Movie('The Martian',
                              "http://t2.gstatic.com/images?q=tbn:ANd9GcTkKPZ"
                              "7EIOafEsemyn6zTIDeGYthKC_Okgxi1eX6diuOT3xKWXQ",
                              'https://www.youtube.com/watch?v=ej3ioOneTy8')

    # Creating a list of movies to pass as an argument to open_movies_page
    # method in fresh_tomatoes.py
    movies = [inception, wonder_woman, thor_3, the_dark_knight, arrival,
              the_martian]

    # Passing the above data for the creation of the site
    fresh_tomatoes.open_movies_page(movies)


main()