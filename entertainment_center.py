import media
import fresh_tomatoes

movieOne = media.Movie("Blazing Saddles",
                       "https://upload.wikimedia.org/wikipedia/en/7/7b/Blazing_saddles_movie_poster.jpg",
                       "https://youtu.be/VKayG1TrfuE")

movieTwo = media.Movie("Robin Hood: Men in Tights",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTA2OTYyODU3MDheQTJeQWpwZ15BbWU3MDA5MjIwNDE@._V1_UY268_CR2,0,182,268_AL_.jpg",
                       "https://youtu.be/K8PLLQ-OODQ")

movieThree = media.Movie("Airplane",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BNDU2MjE4MTcwNl5BMl5BanBnXkFtZTgwNDExOTMxMDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                         "https://youtu.be/HMnVs287AJ4")

movieFour = media.Movie("Young Frankenstein",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTEwNjg2MjM2ODFeQTJeQWpwZ15BbWU4MDQ1MDU5OTEx._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://youtu.be/7csc1O21jDU")

movie_list = [movieOne, movieTwo, movieThree, movieFour]
fresh_tomatoes.open_movies_page(movie_list)
