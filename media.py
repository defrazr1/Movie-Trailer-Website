import webbrowser

"""
Class and Constructor for movie objects

:param movie_title: This variable takes a string for the movie title
:param poster_image: This variable takes a string to the link of an image
:param trailer_youtube: This variable takes a string to the url of the video link
"""
class Movie():
   def __init__(self, movie_title, poster_image, trailer_youtube):
       self.title = movie_title
       self.poster_image_url = poster_image
       self.trailer_youtube_url = trailer_youtube
