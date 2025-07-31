# collection.py

class MediaCollection:
    def __init__(self):
        # Initialize collections and favorites
        self.movies = []
        self.video_games = []
        self.favorite_movie = None
        self.favorite_game = None

    # ----- Movie Methods -----

    def display_movies(self):
        print("\n🎬 Movies in Your Collection:")
        if self.movies:
            for movie in self.movies:
                print(f"- {movie}")
        else:
            print("No movies added yet.")

    def add_movie(self, movie):
        self.movies.append(movie)
        print(f"✅ Added movie: {movie}")

    def remove_movie(self, movie):
        if movie in self.movies:
            self.movies.remove(movie)
            print(f"❌ Removed movie: {movie}")
        else:
            print(f"⚠️ Movie not found: {movie}")

    def set_favorite_movie(self, movie):
        if movie in self.movies:
            self.favorite_movie = movie
            print(f"🌟 Favorite movie set to: {movie}")
        else:
            print(f"⚠️ Cannot set favorite. '{movie}' is not in your collection.")

    # ----- Video Game Methods -----

    def display_video_games(self):
        print("\n🎮 Video Games in Your Collection:")
        if self.video_games:
            for game in self.video_games:
                print(f"- {game}")
        else:
            print("No video games added yet.")

    def add_video_game(self, game):
        self.video_games.append(game)
        print(f"✅ Added video game: {game}")

    def remove_video_game(self, game):
        if game in self.video_games:
            self.video_games.remove(game)
            print(f"❌ Removed video game: {game}")
        else:
            print(f"⚠️ Video game not found: {game}")

    def set_favorite_video_game(self, game):
        if game in self.video_games:
            self.favorite_game = game
            print(f"🌟 Favorite video game set to: {game}")
        else:
            print(f"⚠️ Cannot set favorite. '{game}' is not in your collection.")
