from movies import Movie

# Function 1: loads movies from a csv file and returns it as objects
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

# Function 3: displays the main menu and prompts the user for a valid choice
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
    print("10) Display library summary")
    print(" 0) Exit the system")
    return input("Enter your selection: ")

# Function 4: searches for movies that match the search term
def search_movies(movies, search_term):
    matched = []
    for m in movies:
        if search_term.lower() in m.get_title().lower() or \
           search_term.lower() in m.get_director().lower() or \
           search_term.lower() in m.get_genre_name().lower():
            matched.append(m)
    return matched

# Function 5: searches for movies that match the search term.
def find_movie_by_id(movies, movie_id):
    for m in movies:
        if m.get_id() == movie_id:
            return m
    return -1

# Function 6:
def rent_movie(movies, movie_id):
    movie = find_movie_by_id(movies, movie_id)
    if movie == -1:
        return "Movie with ID " + movie_id + " is not found in library.\n"
    if movie.get_available():
        movie.borrow_movie()
        return "'" + movie.get_title() + "' rented successfully.\n"
    else:
        return "'" + movie.get_title() + "' is already rented - cannot be rented again.\n"


# Function 7:
def return_movie(movies, movie_id):
    movie = find_movie_by_id(movies, movie_id)
    if movie == -1:
        return "Movie with ID " + movie_id + " not found in library.\n"
    if not movie.get_available():
        movie.return_movie()
        return "'" + movie.get_title() + "' was returned successfully.\n"
    else:
        return "'" + movie.get_title() + "' was not rented - cannot be returned.\n"

# Function 8:
def add_movie(movies):
    movie_id = input("Enter movie ID: ")
    if find_movie_by_id(movies, movie_id) != -1:
        return "Movie with ID " + movie_id + " already exists - cannot be added to library\n"
    title = input("Enter title: ")
    director = input("Enter director: ")
    genre = get_genre()
    while True:
        price_input = input("Enter price: ")
        if price_input.replace('.', '', 1).isdigit():
            price = float(price_input)
            break
        print("Invalid price. Please enter a numeric value.")
    new_movie = Movie(movie_id, title, director, genre, True, price, 0)
    movies.append(new_movie)
    return "Movie '" + title + "' added to library successfully .\n"

# Function 9:
def remove_movie(movies):
    movie_id = input("Enter the movie ID to remove: ")
    movie = find_movie_by_id(movies, movie_id)
    if movie == -1:
        return "Movie with ID " + movie_id + " not found in library - cannot be removed.\n"
    title = movie.get_title()
    movies.remove(movie)
    return "Movie '" + title + "' has been removed from library successfully.\n"


# Function 10:
def update_movie_details(movies):
    movie_id = input("Enter the movie ID to update: ")
    movie = find_movie_by_id(movies, movie_id)

    if movie == -1:
        return "Movie with ID " + movie_id + " not found in library.\n"

    print("Leave fields blank to keep current values.")

    new_title = input("Enter new title (current: " + movie.get_title() + "): ")
    if new_title != "":
        movie.set_title(new_title)

    new_director = input("Enter new director (current: " + movie.get_director() + "): ")
    if new_director != "":
        movie.set_director(new_director)

    genre_choice = input("Enter new genre (current: " + movie.get_genre_name() + ") (Yes/Y, No/N))? ")
    if genre_choice.lower() in ["yes", "y"]:
        genre = get_genre()
        movie.set_genre(genre)

    new_price = input("Enter new price (current: " + str(movie.get_price()) + "): ")
    if new_price != "":
        if new_price.replace('.', '', 1).isdigit():
            movie.set_price(float(new_price))
        else:
            return "Invalid price. Movie details not fully updated.\n"

    return "Movie with ID " + movie.get_id() + "' is updated successfully.\n"

# Function 11:
def get_genre():
    GENRES = Movie.GENRE_NAMES
    print("\n    Genres")
    for i in range(len(GENRES)):
        print("    " + str(i) + ") " + GENRES[i])

    choice = input("    Choose genre(0-9): ")
    while not (choice.isdigit() and 0 <= int(choice) <= 9):
        print("    Invalid Genre: Enter a valid genre (0-9)")
        choice = input("    Choose genre(0-9): ")

    return int(choice)

# Function 12:
def list_movies_by_genre(movies):
    genre_index = get_genre()
    genre = Movie.GENRE_NAMES[genre_index]
    found = False
    print("\n{:<10s}{:<30s}{:<25s}{:<12s}{:<15s}{:>10s}{:>14s}".format(
        "ID", "Title", "Director", "Genre", "Availability", "Price", "# Rentals"))
    print("-" * 116)
    for m in movies:
        if m.get_genre_name().lower() == genre.lower():
            print(m)
            found = True
    print("\n")
    if not found:
        print("No movies found in this genre.")
        print("\n")

# Function 13:
def check_availability_by_genre(movies):
    genre_index = get_genre()
    genre = Movie.GENRE_NAMES[genre_index]
    found = False
    print("\n{:<10s}{:<30s}{:<25s}{:<12s}{:<15s}{:>10s}{:>14s}".format(
        "ID", "Title", "Director", "Genre", "Availability", "Price", "# Rentals"))
    print("-" * 116)
    for m in movies:
        if m.get_genre_name().lower() == genre.lower() and m.get_availability() == "Available":
            print(m)
            found = True
    if not found:
        print("No available movies found in this genre.")
    print("\n")

# Function 14:
def display_library_summary(movies):
    total = len(movies)
    available = sum(1 for m in movies if m.get_availability() == "Available")
    rented = total - available
    print("\nTotal movies    :\t", total)
    print("Available movies:\t", available)
    print("Rented movies   :\t", rented,)
    print()

# Function 15:
def popular_movies(movies):
    count_input = input("Enter the minimum number of rentals for the movies you want to view: ")
    
    while not count_input.isdigit():
        print("Invalid input. Please enter a valid number.")
        count_input = input("Enter the minimum number of rentals for the movies you want to view: ")

    count = int(count_input)

    found = False
    print("\nMovies Rented {} Times or More".format(count))
    print("{:<10s}{:<30s}{:<25s}{:<12s}{:>14s}".format(
        "ID", "Title", "Director", "Genre", "# Rentals"))
    print("-" * 91)
    
    for m in movies:
        if m.get_rental_count() >= count:
            print("{:<10s}{:<30s}{:<25s}{:<12s}{:>14}".format(
                m.get_id(), m.get_title(), m.get_director(),
                m.get_genre_name(), m.get_rental_count()))
            found = True
    if not found:
        print("No movies found with rental count >= {}".format(count))
    print("")

# Function 16:
def print_movies(movies):
    print("\n{:<10s}{:<30s}{:<25s}{:<12s}{:<15s}{:>10s}{:>14s}".format(
        "ID", "Title", "Director", "Genre", "Availability", "Price", "# Rentals"))
    print("-" * 116)
    for m in movies:
        print(m)
    print()

# --- Main Program ---
def main():
    filename = input("\nEnter a movie catalog filename: ")
    movies = load_movies(filename)

    if not movies:
        print(f'The catalog file "{filename}" is not found or could not be loaded.\n')
        choice = input("Do you want to continue without loading a file (Yes/Y, No/N)? ")
        if choice.lower() not in ["yes", "y"]:
            print("The Movie Library System will not continue...")
            print("Movie Library System Closed Successfully")
            return
    else:
        print(f'The catalog file "{filename}" successfully loaded {len(movies)} movies to the Movie Library System.')


    selection = ""
    valid_selection = True
    while selection != "0":
        if valid_selection:
            selection = print_menu()
        if valid_selection == False:
            selection = input("Enter your selection: ")
        if selection == "1":
            term = input("Enter search term: ")
            print(f'Searching for "{term.lower()}" in title, director, or genre...')
            results = search_movies(movies, term)
            valid_selection = True
            if results:
                print_movies(results)
            else:
                print("No matching movies found.")
                print()
        elif selection == "2":
            movie_id = input("Enter the movie ID to rent: ")
            print(rent_movie(movies, movie_id))
            valid_selection = True
        elif selection == "3":
            movie_id = input("Enter the movie ID to return: ")
            print(return_movie(movies, movie_id))
            valid_selection = True
        elif selection == "4":
            print(add_movie(movies))
            valid_selection = True
        elif selection == "5":
            print(remove_movie(movies))
        elif selection == "6":    
            print(update_movie_details(movies))
            valid_selection = True
        elif selection == "7":
            list_movies_by_genre(movies)
            valid_selection = True
        elif selection == "8":
            popular_movies(movies)
            valid_selection = True
        elif selection == "9":
            check_availability_by_genre(movies)
            valid_selection = True
        elif selection == "10":
            display_library_summary(movies)
            valid_selection = True
        elif selection == "0":
            print()
            valid_selection = True
        else:
            print("Invalid choice. Please try again.")
            valid_selection = False

    choice = input("Would you like to update the catalog (Yes/Y, No/N)? ")
    if choice.lower() == "yes" or choice.lower() == "y":
        written = save_movies(filename, movies)
        print(str(written) + " movies have been written to Movie catalog.")
    else:
        print("Changes were not saved.")
    print("Movie Library System Closed Successfully")


if __name__ == "__main__":
    main()
