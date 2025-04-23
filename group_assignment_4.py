import os

ID_WIDTH = 3
TITLE_WIDTH = 25
DIRECTOR_WIDTH = 22
GENRE_WIDTH = 10
AVAIL_WIDTH = 13
PRICE_WIDTH = 7
RENTAL_WIDTH = 10
DELIMITER = ","
GENRE_NAMES = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance", "Thriller", "Animation", "Documentary", "Fantasy"]

# Function 1: loads movies from a csv file and returns it as objects
import os

def load_movies(filename):
    movie_list = []
    if not os.path.exists(filename):
        print("The catalog file", filename, "is not found")
        print("Do you want to continue without loading a file (Yes/Y, No/N)?")
        return []

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 7:
                m = Movie(parts[0], parts[1], parts[2], parts[3], parts[4].upper(), parts[5], parts[6])
                movie_list.append(m)

    return movie_list

# Function 2:  
def save_movies(filename, movies):
    with open(filename, "w") as file:
        for m in movies:
            file.write(",".join([
                m.get_id(), 
                m.get_title(), 
                m.get_director(),
                m.get_genre(),
                "TRUE" if m.get_available() else "FALSE",
                format(m.get_price(), ".2f"), 
                str(m.get_rental_count())
            ]) + "\n")
    
    print(f"{len(movies)} movies saved to {filename}")
    return len(movies)

#function 3: print menu
def print_menu():
    print("Movie Library - Main Menu")
    print("=========================")
    print(" 1) Search for movies")
    print(" 2) Rent a movie")
    print(" 3) Return a movie")
    print(" 4) Add a movie")
    print(" 5) Remove a movie")
    print(" 6) Update movie details")
    print(" 7) List movies by genre")
    print(" 8) Find popular movies")
    print(" 9) Check availability by genre")
    print(" 10) Display library summary")
    print(" 0) Exit the system")

    while True:
        choice = input("Enter your selection: ").strip()
        if choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "0"]:
            return choice  

#function 4: movie search
def search_movies(id, title, director, genre, search_term):
    print(f'Searching for "{search_term}" in title, director or genre...')
    print(f"\n{'ID':<{ID_WIDTH}}{'Title':<{TITLE_WIDTH}}{'Director':<{DIRECTOR_WIDTH}}{'Genre':<{GENRE_WIDTH}}")
    print("-" * 70)
    count = 0
    for i in range(len(id)):
        if (search_term.lower() in id[i].lower() or
            search_term.lower() in title[i].lower() or
            search_term.lower() in director[i].lower() or
            search_term.lower() in GENRE_NAMES[genre[i]].lower()):
            print(f"{id[i]:<{ID_WIDTH}}{title[i]:<{TITLE_WIDTH}}{director[i]:<{DIRECTOR_WIDTH}}{GENRE_NAMES[genre[i]]:<{GENRE_WIDTH}}")
            count += 1
    if count == 0:
        print("No matching movies found.")

#function 5: movie search with id
def find_movie_by_id(id, movie_id):
    if movie_id in id:
        return id.index(movie_id)
    return -1

#function 6: renting a movie with id
def rent_movie(movies, movie_id):
    for movie in movies:
        if movie.id == movie_id:
            if movie.available == "TRUE":
                movie.available = "FALSE"
                movie.rental_count = str(int(movie.rental_count) + 1)
                return (f"Movie")



