import fresh_tomatoes
import media

# Instance variables initialized by the constructor in media.py
# //Note to reviewer: Pep dosen't like it when my line continuation isn't lined
# up, yet by doing so seems to cause a complaint against the legnth of line as
# a result of meeting that requirement. Either way it's unhappy with either the
# long code lines or inproper line continuation, what should I do?

# // Note to reviewer: The images work for me when I run the script, and have
# worked for a previous reviewer. If for some reason the image url's don't worke
# please provide a clue as to why because they work perfectly on my end and I'm
# rather curious as to what the problem may be with them.
FIGHT_CLUB = media.Movie("Fight Club",
    "young men start a fight club",  #
    "https://i.ytimg.com/vi_webp/amiyHvl0I4s/movieposter.webp",
    "https://www.youtube.com/watch?v=SUXWAEX2jlg")

V_FOR_VENDETTA = media.Movie("V for Vendetta",
    "A shadowy freedom fighter",
    "https://i.ytimg.com/vi_webp/Et6M2r3yTAw/movieposter.webp",
    "https://www.youtube.com/watch?v=lSA7mAHolAw")

PULP_FICTION = media.Movie("Pulp Fiction",
    "Hit men converge in Quentin Tarantino's",
    "https://i.ytimg.com/vi_webp/hhMtO1MVFSo/movieposter.webp",
    "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

DONNIE_DARKO = media.Movie("Donnie Darko",
    "A troubled teenager is plagued",
    "https://i.ytimg.com/vi_webp/6ytjJM7RriQ/movieposter.webp",
    "https://www.youtube.com/watch?v=ZZyBaFYFySk")

A_CLOCK_WORK_ORANGE = media.Movie("A Clock Work Orange",
    "In future Britain, charismatic delinquent",
    "https://i.ytimg.com/vi_webp/tzUR_CmoYLk/movieposter.webp",
    "https://www.youtube.com/watch?v=SPRzm8ibDQ8")

THE_DEVILS_REJECTS = media.Movie("The Devils Rejects",
    "Ambushed at their isolated home by Sheriff",
    "https://i.ytimg.com/vi_webp/RHDCwu1SEOg/movieposter.webp",
    "https://www.youtube.com/watch?v=poxddLZq2k0")

# Movies array, contains the list of movies as input, which
# is passed to the function "open_movies_page". This function
# translates this list into a web page when we run the
# "entertainment_center.py" file.
MOVIES = [FIGHT_CLUB,
          V_FOR_VENDETTA,
          PULP_FICTION,
          DONNIE_DARKO,
          A_CLOCK_WORK_ORANGE,
          THE_DEVILS_REJECTS]

# Method Call to open the website whe script is ran
fresh_tomatoes.open_movies_page(MOVIES)
