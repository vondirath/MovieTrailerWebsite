import webbrowser


class Movie():
    """Constructor used to create a movie object"""
    def __init__(self, movie_title, synopsis, poster_image, trailer_youtube):
        self.title = movie_title
        self.synopsis = synopsis
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# using the webbrowser module to open a video
        def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)

# using the webbrowser module to open image
        def show_image(self):
            webbrowser.open(self.poster_image_url)
