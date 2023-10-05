import datetime
name=input("Hello!Please enter yOur Name: ")
print("Hello" + name)
age=int(input("Enter Your Age: "))
year_now=datetime.datetime.now()
print("you will turn 100 in " + str(int(100-age)+int(year_now.year)))
