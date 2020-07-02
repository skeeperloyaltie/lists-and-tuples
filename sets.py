#sets
#Creating a set 

t = set(["GodfreyisRight"])
 
print(t)


#Creating a set from a string with a multiline

d = """Geeks For 
           Geeks"""
set1 = set(d)

print(set1)


#Adding elements to a set 

f = set()
f.add("Godfrey")
f.add("has")
f.add("a")
f.add("pen")
f.add("two")
f.add("pens")
f.add((2))

print(f)

#updating an element in a set

f.update(["Skeeper", (10,11), "is", "Godfrey"])

print(f)

#accessing an element in a set

print("Godfrey" in f)

for d in range(1,6):
    f.add(d)
    
    print(f)

#converting a set to a frozen set

g = frozenset(f)

print(g)

#Discariding a set

f.discard("Skeeper")

print(f)
      