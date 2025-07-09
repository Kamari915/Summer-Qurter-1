#1. Create a list of items in your room you can potentially pack.

Travelbag=["shirts","pants","game console","hair products"]

bedroom=[]

print("pack your bags")
print("enter the index o fthe items u want in your bag")
print("type done when your done packing.\n")
print("your bendroomitems")
print(bedroom)

item = int(input("item index: "))

while item !=100:
    Travelbag.append(bedroom[item])
    bedroom.remove(bedroom[item])
    print("\nyourbedroom")
    print(bedroom)
    print("\n your travelbag")
    print(Travelbag)
    item = int(input("item index: "))
    
print("\nYour finished luggage:")
for item in Travelbag:
    print(item)




#2. Create an empty list to represent your travel bag 
#3. Repeatedly prompt the user for the index of an item to put in their travel bag by removing it from the the list of items in your room to your travel bag list.
#4. Once the list is complete, finalize it by creating a tuple representing your luggage. It should have every item in your travel bag. Empty the travel bag list as you do this.
#5. Print the contents of your luggage for the trip, as well as the number of items you decided to bring
