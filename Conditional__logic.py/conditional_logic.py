 # 1. check whether a number is positive , negetive , zero

# def num(a):
#     if a >0:
#         print("Positive")
#     elif a < 0:
#         print("Negetive")
#     else:
#         print("zero")
# num(0)


          #Find the largest of two numbers

# def large(a,b):
#     if a >b :
#         print("The largest number is :",a)
#     else:
#         print("The largest number is : ",b)
# large(34,3)

                                #Find the large number between 3 numbers

# def large(a,b,c):
#     if a>=b and a>=c:
#         print("The largest number is : ",a)
#     elif b>=a and b>=c:
#         print("The largest number is : ",b)
#     else:
#         print("The largest number is :",c)
# large(13,32,30)
        

                  #check whether is a number is even or odd
# def num(a):
#     if (a % 2) == 0:
#        print("The number is even")  
#     else:
#         print("The number is odd")  
# num(22)


                   #Check whether a year is leap or not

# def leap(a):
#     if (a%4) == 0 or (a%400) == 0: 
#         print("The year is leap")
#     else:
#         print("The year is not leap")
# leap(2024)


                   #check whether a person is elgible for vote or not
# def vote(a):
#     if a >= 18 :
#         print("The person is elgible for vote ")
#     else:
#         print("The perosn is not elgible for vote")
# a = int(input("Enter age of the person : "))
# vote(a)

                   #Find whether a character is a vowel or consonant.
# def char(c):
#     if c  in ("a" ,"A" , "E" , "e" ,"O" , "o" , "U" ,"u" ,"I" , "i"):
#         print("The character is vowel")
#     else:
#         print("The character is a concomant")
# char("I")


                                  # Check whether a number is divisible by 5 and 11.

# def div(a):
#     if (a % 5) ==  0 and (a % 11) == 0:
#         print("Yes it is disible by 5 ans 11")
#     else:
#         print("No")
# div(55)
                                      

                                 #9. Find the grade based on marks using conditions.

# def marks(a):
#     if a >= 90:
#         print("Grade is AA")
#     elif (90>a>=80):
#         print("Grade is A")
#     elif(80>a>=50):
#         print("Grade is B")
#     elif(50>a>=30):
#         print("Grade is C")
#     else:
#         print("Grade is F")
# marks(56)



                                            #10. Calculate profit or loss.

# def cal(buy,sell):
#     if (buy > sell):
#        print(f"Loss is {buy - sell}")
#     else:
#         print(f"Profit is {sell - buy}")
# cal(90,30)



                                       #Logic practice
                              #1. Find the smallest of three numbers.

# def num(a,b,c):
#     if (a<b) and (a<c):
#         print("The smallest number is : ",a)
#     elif(b<a) and (b<c):
#         print("The smallest numbr is :",b)
#     else:
#         print("The samllest number is :",c)
# num(6,4,1)



                                           #2. Check whether a number is a multiple of another number.

# def num(a,b):
#     if (a%b) == 0:
#         print("a is multiple of b")
#     elif(b%a) == 0:
#         print("b is multiple of a")
#     else:
#         print("Those number is not multiple of each other")
# num(8,64)


                                             #3. Create a simple calculator using conditional state)

# def cal(choice,x,y):
#     if choice == "a":
#         print(f"Addition is : {x+y}")
#     elif choice == "b":
#         print(f"Substraction is :{x- y} ")
#     elif choice == "c":
#         print(f"Multiple is : {x*y}")
#     elif choice == "d":
#         print(f"Divition is : {x/y}")
    


# print("Enter a for addition")
# print("Enter b for substraction")
# print("Enter c for multiple")
# print("Enter d for divition")

# choice = input("Enter keyword, what to do :")
# x = float(input("Enter a number : "))
# y = float(input("Enter a number :"))

# cal(choice,x,y)



                                           #4. Find whether a triangle is valid based on its sides.

# def tri(a,b,c):
#     if (a+b) > c and (b+c) > a and (c+a) > b :
#         print("Triangular is valid based")
#     else:
#         print("No valid based")
# tri(1,2,3)
    


                                         #5. Determine the type of triangle.

# def tri(a,b,c):
#     if (a==b ==c):
#         print("the triangle is  equal")
#     elif (a==b !=c) or (a == c !=b) or (b == c != a):
#         print("the triangular has two equal")
#     else:
#         print("The triangular has no equal")
# tri(9,1,2)
          