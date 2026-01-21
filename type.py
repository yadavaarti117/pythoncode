#type conversion
a = "10"
b = int(a)
print(b)
print(type(b))

#comparision operators
a = 10
b = 20
print(a == b)   
print(a != b)   
print(a > b)    

#conditional statements
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
#short-circuit evaluation
a =int(5) 
b = int(0)
if a > 0 and b >0: 
    print("Both are Positive")
else:
    print("condition Failed") 
#Chaining Comparison Operators
x = 15
if 10 < x < 20:
    print("x is between 10 and 20")
else:
    print("x is not in the range")