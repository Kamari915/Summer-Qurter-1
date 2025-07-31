student ={}

studentname=input("enter your name:")
student["name"] =  studentname

studentage=input("enter age")
student["age"] = studentage

studentgrades=input("enter grade")
student["grade"]= studentgrades

hobbies=[]
hobby =input("enter hobbies enter done when done")
hobbies.append(hobby)

while hobby != "done":
    hobby =input("enter hobbies enter done when done")
    hobbies.append(hobby)
student["hobbies"]= hobbies

print(student)
