#python core datatypes
#Lists

fruits=["Banana","Apple","Cherry"]
numbers=[10,15,20,50]
mixed=[1,"hello",4.51,True]

print("Fruits:",fruits)
print("Numbers",numbers)
print("Mixed List:",mixed)

#common list method
fruits.append("orange")
fruits.insert(1,"mango")
fruits.remove("Banana")
fruits.pop()
fruits.sort()
fruits.reverse()

print("updated fruits:",fruits)

#list comprehensions
squares=[x**3 for x in range(1,6)]
print("Squares:",squares)

#Tuples
#creating tuples

coordinates=(20,30)
person=("John",20,"Doctor")
print("Coordinates:",coordinates)
print("Person Info:",person)

print("First Element:",coordinates[0]) #accessing coordinates
print("Length of person tuple:",len(person))

#tuple method

nums=(1,2,2,3,4,8)
print("Count of 2:",nums.count(2))
print("Index of first 3:",nums.index(3))

#Dictionaries

student={"name":"Jack",
         "age":19,
         "Major":"Computer science"}
print("Student Dictionary:",student)
print("Name:",student["name"]) #access by value key

#Dictionary method

student["age"]=23
student["GPA"]=3.1
student.pop("Major")

#viewing values and key

print("keys",list(student.keys()))
print("Values:",list(student.values()))
print("Items:",list(student.items()))

#Iterating through dictionary
for key,value in student.items():
    print(f"{key}:{value}")

#sets

numbers={1,2,3,4,5}
print("set(duplicate removed):",numbers)

odd={1,3,5,7}
even={2,4,6,8}

#set operation with another set
print("Union:",odd|even)
print("Intersection:",odd & numbers)
print("Difference:",numbers-odd)




