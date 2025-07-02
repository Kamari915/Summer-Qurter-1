import random
players = ["kamari" , "max" , "braylen"
           , "ollie" , " xavier" , "Avery"
           , "carl" , "walter" , "darren"
           , "EJ" , "Nahuh", "joaquin"
           , "Marshawn" , "ja'den" , "isaiah"
           , "kenlon" , "Nishad" , "Kauri"
           , "kriss" , "Joseph" , "semaj"
           , "tay" , "taqari" , "jarma"]
def PickTeams(players):
    random.shuffle(players)
    team1 = players[:len(players)//2]
    teamCaptain1 = team1[random.randrange(0, 13)]