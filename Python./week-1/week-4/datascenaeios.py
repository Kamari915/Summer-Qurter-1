print("scenario #1: A RESTARANT menue with prices for each item")
print("Best structure : Dictinary; best to pair food with price in key/value")

menu={
    "french toast": 12,
    "grand slam": 12,
    "t-bone steak": 18,

}

for key, item in menu.items():
    print(key, ": ", item)

print("scenario #2: high scores to an arcade game")
print("Best structure : list; every time the high score gets broken it gets added")
highscore= [
    100,
    105,
    110,
    99
]
for score in highscore:
    print(score)

print("scenario #3: All of the months of the year")
print("Best structure : tupel; the monthes dont change")
monthsoftheyear=(
    "january",
    "February",
    "March",
    "April",
)

