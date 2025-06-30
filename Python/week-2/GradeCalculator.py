numbergrade = int(input("Enter number grade from 1-100"))
lettergrade = ""

if(numbergrade >= 90):
    lettergrade = "A"
elif (80 <= numbergrade <= 89):
    lettergrade ="B "
elif (70 <= numbergrade <= 79):
    lettergrade ="C"
elif (60 <= numbergrade <= 69):
    lettergrade ="D"
elif (numbergrade < 60):
    lettergrade="F"
print("you got a " + lettergrade)