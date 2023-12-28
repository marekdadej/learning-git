import random

class Media:
    def __init__(self, title, year, genre, plays):
        self.title = title
        self.year = year
        self.genre = genre
        self.plays = plays

    def play(self):
        self.plays += 1

    def __str__(self):
        return f"{self.title} ({self.year})"


class Movie(Media):
    pass


class TVShow(Media):
    def __init__(self, title, year, genre, season, episode, plays):
        super().__init__(title, year, genre, plays)
        self.season = season
        self.episode = episode

    def play(self):
        self.plays += 1

    def __str__(self):
        season_str = f"{self.season:02d}"
        episode_str = f"{self.episode:02d}"
        return f"{self.title} S{season_str}E{episode_str}"


def get_movies(library):
    movies = [media for media in library if isinstance(media, Movie)]
    movies.sort(key=lambda x: x.title)
    return movies

def get_series(library):
    series = [media for media in library if isinstance(media, TVShow)]
    series.sort(key=lambda x: x.title)
    return series

def search(library, title):
    results = [media for media in library if title.lower() in media.title.lower()]
    return results

def generate_views(library):
    random_media = random.choice(library)
    views = random.randint(1, 100)
    random_media.plays += views
    print(f"Dodano {views} odtworzeń dla: {random_media.title}")

def run_generate_views(library, times=10):
    for _ in range(times):
        generate_views(library)

def top_titles(library, num_titles=5, content_type=None):
    if content_type == "movies":
        filtered_library = get_movies(library)
    elif content_type == "series":
        filtered_library = get_series(library)
    else:
        filtered_library = library

    sorted_library = sorted(filtered_library, key=lambda x: x.plays, reverse=True)
    return sorted_library[:num_titles]

# Przykładowe użycie

movies_and_shows = [
    Movie("Pulp Fiction", 1994, "Crime", 10),
    TVShow("The Simpsons", 1989, "Animation", 1, 5, 8),
    Movie("The Shawshank Redemption", 1994, "Drama", 15),
    Movie("Inception", 2010, "Sci-Fi", 12),
    Movie("Forrest Gump", 1994, "Drama", 9),
    TVShow("Friends", 1994, "Comedy", 1, 24, 5),
    TVShow("Breaking Bad", 2008, "Drama", 5, 10, 12),
    TVShow("Stranger Things", 2016, "Sci-Fi", 3, 8, 20)
]

# Przykładowe wywołanie funkcji
for media in movies_and_shows:
    print(media)
    media.play()
    print(f"Liczba odtworzeń: {media.plays}")

# Przykładowe użycie funkcji
run_generate_views(movies_and_shows)
top_movies = top_titles(movies_and_shows, num_titles=3, content_type="movies")
top_series = top_titles(movies_and_shows, num_titles=3, content_type="series")

print("\nNajpopularniejsze filmy:")
for movie in top_movies:
    print(movie)

print("\nNajpopularniejsze seriale:")
for series in top_series:
    print(series)

