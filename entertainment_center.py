import fresh_tomatoes
import media

fight_club = media.Movie("Fight Club",
                        """Sick of his dead end, white bread, corporate career and disgusted
                         with the empty consumer culture of his generation, a confused young
                         man serendipitously meets Tyler Durden. Together they create a new club
                         where young men come to relieve their frustrations by beating each other to a pulp""",
                        "https://i.ytimg.com/vi_webp/amiyHvl0I4s/movieposter.webp",
                        "https://www.youtube.com/watch?v=SUXWAEX2jlg")
#Add in more movies
v_for_vendetta = media.Movie("V for Vendetta",
                            """A shadowy freedom fighter known only as "V" uses guerrilla tactics to fight against
                             his terrorist, totalitarian society. Upon rescuing a girl from the secret police, he also
                             finds his best chance at having an ally""",
                             "https://i.ytimg.com/vi_webp/Et6M2r3yTAw/movieposter.webp",
                             "https://www.youtube.com/watch?v=lSA7mAHolAw")

pulp_fiction = media.Movie("Pulp Fiction",
                            """Hit men, gangsters and robbers converge in Quentin Tarantino's violent tale of revenge.
                            Stars John Travolta Samuel L. Jackson Bruce Willis and Uma Thurman""",
                            "https://i.ytimg.com/vi_webp/hhMtO1MVFSo/movieposter.webp",
                            "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

donnie_darko = media.Movie("Donnie Darko",
                            """A troubled teenager is plagued by visions of a large bunny rabbit that manipulates him to
                            commit a series of crimes, after narrowly escaping a bizarre accident.""",
                            "https://i.ytimg.com/vi_webp/6ytjJM7RriQ/movieposter.webp",
                            "https://www.youtube.com/watch?v=ZZyBaFYFySk")

a_clock_work_orange = media.Movie("A Clock Work Orange",
                                    """In future Britain, charismatic delinquent Alex DeLarge is jailed and volunteers for an
                                     experimental aversion therapy developed by the government in an effort to solve society's crime problem
                                      - but not all goes according to plan.""",
                                    "https://i.ytimg.com/vi_webp/tzUR_CmoYLk/movieposter.webp",
                                    "https://www.youtube.com/watch?v=SPRzm8ibDQ8")

the_devils_rejects = media.Movie("The Devils Rejects",
                                """Ambushed at their isolated home by Sheriff Wydell (William Forsythe) and a squad of armed men, the Firefly
                                family wakes up one morning with guns blazing ? yet only Otis (Bill Moseley) and his sister, Baby (Sheri Moon Zombie),
                                manage to escape the barrage of bullets unharmed. Hiding out in a backwater motel, the wanted siblings wait to rendez-vous
                                with their errant""",
                                "https://i.ytimg.com/vi_webp/RHDCwu1SEOg/movieposter.webp",
                                "https://www.youtube.com/watch?v=poxddLZq2k0")

movies = [fight_club, v_for_vendetta, pulp_fiction, donnie_darko, a_clock_work_orange, the_devils_rejects]
fresh_tomatoes.open_movies_page(movies)
