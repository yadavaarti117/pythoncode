history =[]

while True:
    if history !=[]:
     continue_input = input("Do you want to continue(y/n):")
     if continue_input == "y":
        pass
     elif continue_input=="n":
        print("Logs:")
        for h in history:
            print(h)
        break
     else:
        print("Type a valid choice")

        continue

    #take two inputs

    a_input= input("Enter first Number:")
    a= int(a_input)
    b_input=input("Enter second Number:")
    b= int(b_input)

    help_text=""""
    1:Addition
    2:Subtraction
    3:Multiplication
    4:Division
    5:Exponential
    6:Modulo

    """

    print(help_text)

    operation = input("Enter the operation type (1/2/3/4/5/6):")

    if operation == "1":
        print(a+b)
        history.append(f"{a}+{b} = {a+b}")

    elif operation =="2":
        print(a-b)
        history.append(f"{a}-{b} = {a-b}")

    elif operation =="3":
        print(a*b)
        history.append(f"{a}*{b} = {a*b}")

    elif operation =="4":
        if b==0:
            print("Cannot divide by 0.")
            continue
        print(a/b)
        history.append(f"{a}/{b} = {a/b}")

    elif operation =="5":
        print(a**b)
        history.append(f"{a}**{b} = {a**b}")

    elif operation =="6":
        if b==0:
            print("Cannot perform modulo by 0:")
            continue
        print(a%b)
        history.append(f"{a}%{b} ={a%b}")

    else:
        print("Not a valid command ,Try again!")
    