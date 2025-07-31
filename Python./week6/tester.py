# tester.py

from collection import MediaCollection

# ----- Create and Setup Collection -----
my_collection = MediaCollection()

# ----- Add Movies and Games -----
my_collection.add_movie("Spider-Man: Into the Spider-Verse")
my_collection.add_movie("Black Panther")
my_collection.add_video_game("Minecraft")
my_collection.add_video_game("Fortnite")

# ----- Display Current Collections -----
my_collection.display_movies()
my_collection.display_video_games()

# ----- Set Favorites -----
my_collection.set_favorite_movie("Spider-Man: Into the Spider-Verse")
my_collection.set_favorite_video_game("Minecraft")

# ----- Remove Items -----
my_collection.remove_movie("Black Panther")
my_collection.remove_video_game("Fortnite")

# ----- Final Output -----
print("\n📦 Final Media Collection:")
my_collection.display_movies()
my_collection.display_video_games()

print("\n🌟 Favorites:")
print(f"Favorite Movie: {my_collection.favorite_movie}")
print(f"Favorite Video Game: {my_collection.favorite_game}")
