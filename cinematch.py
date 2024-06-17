class Movie:
    def __init__(self, title, genre, stars_popularity, diverse_cast):
        self.title = title
        self.genre = genre
        self.stars_popularity = stars_popularity  # 'high', 'medium', 'low'
        self.diverse_cast = diverse_cast  # Boolean indicating diverse cast
        self.rating = 0

    def __str__(self):
        return f"Title: {self.title}, Genre: {self.genre}, Rating: {self.rating}"

class CineMatch:
    def __init__(self):
        self.movies = []
        self.genre_base_ratings = {
            'Sci-Fi': 7,
            'Action': 6,
            'Drama': 5,
            'Comedy': 4
        }
        self.popularity_ratings = {
            'high': 2,
            'medium': 1,
            'low': 0
        }

    def calculate_rating(self, movie):
        base_rating = self.genre_base_ratings.get(movie.genre, 0)
        popularity_bonus = self.popularity_ratings.get(movie.stars_popularity, 0)
        diversity_bonus = 1 if movie.diverse_cast else 0
        return base_rating + popularity_bonus + diversity_bonus

    def assign_unique_ratings(self):
        # Calculate initial ratings
        for movie in self.movies:
            movie.rating = self.calculate_rating(movie)

        # Sort movies by their initial ratings and assign unique ratings
        self.movies.sort(key=lambda x: x.rating, reverse=True)
        unique_ratings = list(range(10, 10 - len(self.movies), -1))
        for i, movie in enumerate(self.movies):
            movie.rating = unique_ratings[i]

    def add_movie(self, title, genre, stars_popularity, diverse_cast):
        movie = Movie(title, genre, stars_popularity, diverse_cast)
        self.movies.append(movie)
        self.assign_unique_ratings()

    def search_movies_by_title(self, title):
        return [movie for movie in self.movies if title.lower() in movie.title.lower()]

    def search_movies_by_genre(self, genre):
        return [movie for movie in self.movies if genre.lower() in movie.genre.lower()]

    def recommend_top_n_movies(self, n):
        return sorted(self.movies, key=lambda x: x.rating, reverse=True)[:n]

    def delete_movie(self, title):
        self.movies = [movie for movie in self.movies if movie.title.lower() != title.lower()]
        self.assign_unique_ratings()  # Re-assign ratings after deletion

    def display_movies(self):
        for movie in self.movies:
            print(movie)

if __name__ == "__main__":
    cinematch = CineMatch()
    
    # Add movies
    cinematch.add_movie("Inception", "Sci-Fi", "high", True)
    cinematch.add_movie("Interstellar", "Sci-Fi", "high", True)
    cinematch.add_movie("The Godfather", "Drama", "high", False)
    cinematch.add_movie("Avengers", "Action", "high", True)
    cinematch.add_movie("Joker", "Drama", "medium", False)
    cinematch.add_movie("Titanic", "Drama", "high", False)
    cinematch.add_movie("The Hangover", "Comedy", "medium", False)
    cinematch.add_movie("Guardians of the Galaxy", "Action", "medium", True)
    cinematch.add_movie("Parasite", "Drama", "low", True)
    cinematch.add_movie("John Wick", "Action", "high", False)
    
    # Display all movies
    print("All Movies:")
    cinematch.display_movies()
    
    # Search movies by title
    print("\nSearch by Title 'Inception':")
    for movie in cinematch.search_movies_by_title("Inception"):
        print(movie)
    
    # Search movies by genre
    print("\nSearch by Genre 'Drama':")
    for movie in cinematch.search_movies_by_genre("Drama"):
        print(movie)
    
    # Recommend top 5 movies
    print("\nTop 5 Movies:")
    for movie in cinematch.recommend_top_n_movies(5):
        print(movie)
    
    # Delete a movie
    cinematch.delete_movie("Joker")
    
    # Display all movies after deletion
    print("\nAll Movies after Deletion:")
    cinematch.display_movies()
