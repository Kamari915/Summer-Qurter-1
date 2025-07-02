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
    teamCaptain1= team1[random.randrange(0, 13)]

    print("team1:")
    print("teamCaptain1:" + teamCaptain1 )
    for player in team1:
        print(player)

    team2 = players[:len(players)//2]
    teamCaptain2= team2[random.randrange(0, 13)]
    print("\n team2:")
    print("teamCaptain2:" + teamCaptain2 )
    for player in team2:
        print(player)

PickTeams(players)
