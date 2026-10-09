# Dictionary mapping movie titles to profits in USD in 2026 as of 10/9
# source: https://www.the-numbers.com/market/2026/top-grossing-movies

# Dictionary mapping movie titles to their 2026 profits
movie_profits = {
    "Anaconda": 33322690,
    "Avatar: Fire and Ash": 153986141,
    "Avengers: Endgame": 37481127,
    "Backrooms": 197523512,
    "Buddy": 26920768,
    "Coyote vs. Acme": 59995011,
    "Crime 101": 36588336,
    "The Devil Wears Prada 2": 220556651,
    "Dhurandhar: The Revenge": 28100759,
    "Disclosure Day": 116636645,
    "The Drama": 48062006,
    "The End of Oak Street": 54223622,
    "Evil Dead Burn": 32237058,
    "GOAT": 103316898,
    "Heart of the Beast": 41709938,
    "Hoppers": 166010783,
    "The Housemaid": 70173827,
    "Insidious: Out of the Further": 65846940,
    "The Invite": 26099134,
    "Iron Lung": 41111208,
    "Lee Cronin's The Mummy": 29152113,
    "Marty Supreme": 57056211,
    "Masters of the Universe": 64830245,
    "Michael": 372303388,
    "Minions & Monsters": 183171260,
    "Moana": 126229663,
    "Mortal Kombat II": 79770110,
    "Obsession": 263451715,
    "The Odyssey": 620870575,
    "PAW Patrol: The Dino Movie": 53084400,
    "Practical Magic 2": 65726310,
    "Primate": 25635665,
    "Primetime": 34085832,
    "Project Hail Mary": 344050007,
    "Reminders of Him": 48559430,
    "Resident Evil": 129135252,
    "Scary Movie": 108277762,
    "Scream 7": 121935967,
    "Send Help": 64734795,
    "The Sheep Detectives": 66078506,
    "Solo Mio": 25736278,
    "Spider-Man: Brand New Day": 955203202,
    "Star Wars: The Mandalorian and Grogu": 177730060,
    "The Super Mario Galaxy Movie": 429814610,
    "Supergirl": 72366532,
    "Toy Story 5": 480294461,
    "Verity": 40404150,
    "Wuthering Heights": 84001072,
    "Young Washington": 47075084,
    "Zootopia 2": 90227005
}

# Dictionary mapping movie genres to a list of titles with that genre
genre_movies = {
    "Horror": [
        "Obsession",
        "Backrooms",
        "Resident Evil",
        "Scream 7",
        "Insidious: Out of the Further",
        "Iron Lung",
        "Evil Dead Burn",
        "Lee Cronin's The Mummy",
        "Buddy",
        "Primate"
    ],
    "Adventure": [
        "The Odyssey",
        "Toy Story 5",
        "The Super Mario Galaxy Movie",
        "Minions & Monsters",
        "Star Wars: The Mandalorian and Grogu",
        "Hoppers",
        "Zootopia 2",
        "Coyote vs. Acme",
        "PAW Patrol: The Dino Movie"
    ],
    "Action": [
        "Spider-Man: Brand New Day",
        "Project Hail Mary",
        "Avatar: Fire and Ash",
        "Mortal Kombat II",
        "Supergirl",
        "Masters of the Universe",
        "Avengers: Endgame",
        "Dhurandhar: The Revenge"
    ],
    "Drama": [
        "Michael",
        "The Devil Wears Prada 2",
        "Wuthering Heights",
        "Marty Supreme",
        "Reminders of Him",
        "The Drama",
        "Young Washington",
        "Primetime"
    ],
    "Thriller/Suspense": [
        "Disclosure Day",
        "The Housemaid",
        "Send Help",
        "The End of Oak Street",
        "Heart of the Beast",
        "Verity",
        "Crime 101"
    ],
    "Comedy": [
        "Scary Movie",
        "GOAT",
        "The Sheep Detectives",
        "Practical Magic 2",
        "Anaconda",
        "The Invite"
    ],
    "Musical": [
        "Moana"
    ],
    "Romantic Comedy": [
        "Solo Mio"
    ]
}

##### TASK 1 #####
# Write a function that prints out the profits made for 
# each movie in the `movie_profits` dictionary. For example, 
# you might print out something like: 
# `Toy Story 5 made $480294461 in 2026.`
def print_each_movie_profits():
    pass

##### TASK 2 #####
# Write a function that prints out the average profit of all the movies.
def print_average_profit():
    pass

##### TASK 3 #####
# Write a function that prints the title of the highest-profiting 
# movie from the `movie_profits` dictionary.
def print_highest_profit():
    pass

##### TASK 4 #####
# Using both the `genre_movies` and `movie_profits` dictionaries, 
# create a new dictionary that maps genres (keys) to the total 
# profit amount for that genre (the values). For example, one 
# key-value pair in your dictionary might be `"Comedy": 500000000`, 
# which would indicate that all comedy movies cumulatively made 
# $500,000,000.
def create_genre_profit_dict():
    genre_profit_dict = {}
    return genre_profit_dict

##### TASK 5 #####
# Using the dictionary you just made, print out the most financially 
# successful genre of 2026.
def highest_profit_genre():
    genre_profit_dict = create_genre_profit_dict()

##### TASK 6 #####
# Create a new dictionary that maps each genre to its average profit.
def average_profit_genre():
    genre_profit_dict = create_genre_profit_dict()


#### EXTENSIONS ####
# research and implement printing out the profits with appropriately placed commas
# research and implement printing the averages rounded to two decimal places
# complete another analysis that you come up with yourself!
# modify function 3 to print out the top n highest-grossing movies, where n is an integer between 1 and 50