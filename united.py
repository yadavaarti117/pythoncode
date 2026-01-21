#string method

text = "  I'm learning python  "
print(text.upper())
print(text.strip())
print(text.replace("python", "Java"))
print("Java" in text)

#list

name_list = [
    "Aditya", "Bibek", "Dipesh", "Kiran", "Pratik",
    "Rajesh", "Suman", "Ashok", "Anjali", "Bina",
    "Kopila", "Nirmala", "Pooja", "Sabita", "Urmila"]

Fav_foods =["Pad Thai", "Paella", "Pho", "Pierogi", "Feijoada",
    "Tagine", "Biryani", "Ceviche", "Moussaka", "Rendang",
    "Borscht", "Empanadas", "Shakshuka", "Poutine", "Goulash"]

for i in range(len(name_list)):
    print(f"{name_list[i]}\t{Fav_foods[i]}")


# for loops
for i in range(5):
    print(i)

#for else
for i in range(5):
    if i == 10:
        print("found 5")
        break
else:
    print("loop completed without break")  

#nestes loops
for i in range(2):
    for j in range(3):
        print(i,j)

#Iterables
my_list =[1,2,3,4]
for item in my_list:
    print(item)
iterator = iter(my_list)
print(next(iterator))

#while loop
count = 0
while count<3:
    print(count)
    count +=1

#defining functions
def greet():
    print("hello!")
greet()

#Arguments
def greet(name):
    print(f"Hello,{name}")
greet("aarti")

#Function types(can return values or simple can perform action)
def add(a, b):
    return a+b
def show_sum(a, b):
    print(a+b)
print(add(5,7))
show_sum(5,7)

#keyword arguments
def greet(first_name,last_name):
    print(f"hello {first_name} {last_name}!")
greet(last_name="yadav",first_name="Aman")

#default arguments
def greet(name="Aarati"):
    print(f"Hello,{name}")
greet()
greet("Alice")

#*args
def add_all(*numbers):
    return sum(numbers)

print(add_all(1,2,3,4,5s))
   

