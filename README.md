# Cinematch
CineMatch is a simple and intuitive movie recommendation system designed to enhance the movie-watching experience by providing personalized suggestions and efficient movie management. This system allows users to submit, search, recommend, and delete movies, all while utilizing in-memory data structures for fast and reliable performance.

# CineMatch

CineMatch is a simple movie recommendation system designed to enhance the movie-watching experience by providing personalized suggestions and efficient movie management. The system allows users to submit, search, recommend, and delete movies, utilizing in-memory data structures for fast and reliable performance.

## Features

- **Movie Submission**: Add new movies with details such as title, genre, and rating.
- **Movie Search**: Search for movies by title or genre.
- **Movie Recommendation**: Get top N movie recommendations based on ratings.
- **Movie Deletion**: Remove movies from the system.
- **Automated Rating System**: Movies are automatically assigned unique ratings based on genre, star power, and cast diversity.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/CineMatch.git
    cd CineMatch
    ```

2. Ensure you have Python installed (version 3.6+ recommended).

3. Run the main script:
    ```sh
    python cinematch.py
    ```

## Usage

### Adding a Movie
```python
add_movie(title="Inception", genre="Sci-Fi", stars=["Leonardo DiCaprio"])

search_by_title("Inception")
search_by_genre("Sci-Fi")

recommend_movies(n=5)

delete_movie("Inception")

from cinematch import CineMatch

cm = CineMatch()
cm.add_movie(title="Inception", genre="Sci-Fi", stars=["Leonardo DiCaprio"])
cm.add_movie(title="The Dark Knight", genre="Action", stars=["Christian Bale"])
cm.add_movie(title="Interstellar", genre="Sci-Fi", stars=["Matthew McConaughey"])

print(cm.search_by_title("Inception"))
print(cm.search_by_genre("Sci-Fi"))

print(cm.recommend_movies(n=2))

cm.delete_movie("Inception")

