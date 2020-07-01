#Python LIsts
#My day Routine


my_day_routine = ["1: Wake up", "2: Brush my teeth", "3: Take a shower"]

print(my_day_routine)
event = "Almost forgot"

my_day_routine.append("4: I love programming")

print (my_day_routine)

#print a value of part of the list..

print (my_day_routine[1:])
#display then delete

my_day_routine.pop()

#a list with duplicates

a= [1,1,1,1,1,2,2,2,2,3,3,3,3]

print("\nList with duplcate numbers on it: ")

print (a)

#Lists with mixed values

b = ["Godfrey", 10.0, "Skeeper", 12]

print(b)

#sizes of lists

print("\nLength of my routine is: ")
print(len(my_day_routine))
print("\nLength of a is: ")
print(len(a))
print("\nLength of b is: ")
print(len(b))

#Slicing a string value

print(my_day_routine[2])



