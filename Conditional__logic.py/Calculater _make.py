def cal(choice,x,y):
    if choice == "a":
        print(f"Addition is : {x+y}")
    elif choice == "b":
        print(f"Substraction is :{x- y} ")
    elif choice == "c":
        print(f"Multiple is : {x*y}")
    elif choice == "d":
        print(f"Divition is : {x/y}")
    


print("Enter a for addition")
print("Enter b for substraction")
print("Enter c for multiple")
print("Enter d for divition")

choice = input("Enter keyword, what to do :")
x = float(input("Enter a number : "))
y = float(input("Enter a number :"))

cal(choice,x,y)