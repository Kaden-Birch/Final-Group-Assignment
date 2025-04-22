class movie:
    GENRE_NAMES = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi",
                   "Romance", "Thriller", "Animation", "Documentary", "Fantasy"]

    def __init__(self, id, title, director, genre, available=True, price=0.0, rental_count=0):
        self.id = id
        self.title = title
        self.director = director
        self.genre = int(genre)
        self.available = available == True or str(available).upper() == "TRUE"
        self.price = float(price)
        self.rental_count = int(rental_count)

    def get_id(self): return self.id
    def get_title(self): return self.title
    def get_director(self): return self.director
    def get_genre(self): return self.genre
    def get_available(self): return self.available
    def get_price(self): return self.price
    def get_rental_count(self): return self.rental_count

    def get_genre_name(self):
        if 0 <= self.genre < len(movie.GENRE_NAMES):
            return movie.GENRE_NAMES[self.genre]
        return "Unknown"

    def get_availability(self):
        return "Available" if self.available else "Rented"

    def set_title(self, title): self.title = title
    def set_director(self, director): self.director = director
    def set_genre(self, genre): self.genre = int(genre)
    def set_price(self, price): self.price = float(price)

    def borrow_movie(self):
        if self.available:
            self.available = False
            self.rental_count += 1

    def return_movie(self):
        self.available = True

    def __str__(self):
        return "{:<10s}{:<30s}{:<25s}{:<12s}{:<15s}${:>8.2f}{:>10}".format(
            self.id, self.title, self.director, self.get_genre_name(),
            self.get_availability(), self.price, self.rental_count)
