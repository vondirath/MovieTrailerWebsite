import media
import fresh_tomatoes

star_wars_tfa = media.Movie(
    "Star Wars: The Force Awakens",
    "Following a new set of heroes Rey and Finn search for the last jedi, Luke Skywalker.",
    "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
    "https://www.youtube.com/watch?v=sGbxmsDFVnE"
    )
evil_dead = media.Movie(
    "Evil Dead",
    "Attempting to cure his sisters heroin addiction a group of friends find more"
    "than they bargain for in a mysterious cabin which is home to an evil book.",
    "https://upload.wikimedia.org/wikipedia/en/9/9d/EvilDead2013Poster.jpg",
    "https://www.youtube.com/watch?v=FKFDkpHCQz4"
    )
black_mass = media.Movie(
    "Black Mass",
    "Following the criminal career of real-life criminal entrepreneur Whitey Bulger.",
    "https://upload.wikimedia.org/wikipedia/en/c/c0/Black_Mass_%28film%29_poster.jpg",
    "https://www.youtube.com/watch?v=CE3e3hGF2jc"
    )

movies = [star_wars_tfa, evil_dead, black_mass]
fresh_tomatoes.open_movies_page(movies)
