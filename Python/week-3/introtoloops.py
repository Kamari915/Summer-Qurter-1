# step create a list of evvry one in this room
Geniuses =["tae", "joaquin", "kris", "jeffrey"]
for Genius in Geniuses:
    print(Genius)
answer = input("Do you want me to print the list again? Y/N")  
while answer == "Y":
    for Genius in Geniuses:
         print(Genius)
    answer = input("Do you want me to print the list again? Y/N")  
