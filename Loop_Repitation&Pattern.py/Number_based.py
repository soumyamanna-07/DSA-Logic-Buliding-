                       #1. Print numbers from 1 to N.
# def num(n):
#     for i in range (1,n+1):
#         print(i)
# num(100)

                       #2. Print numbers from N to 1.
# def num(n):
#     for i in range (n,0,-1):
#         print(i)
# num(10)

                        #3. Find the sum of first N natural numbers.
# def num(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum = sum + i
#         print(sum)
# num(5)

                        #4. Find the factorial of a number.
# def num(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact*i
#     print(fact)
# num(5)

                           #5. Print the multiplication table of a number.
# def num(n):
#     mul = n
#     for i in range (1,11):
#         mul = n*i
#         print(f"{n}*{i} : {mul}")
# num(5)

                            #6. Count the digits in a number.
# def num(n):
#     print(f"{len(str(n))}")
# num(3434534)

                            #7. Find the sum of digits.

def num(n):
    sum = 0
    for i in str(n):
        sum = sum + int(i)
    print(sum)
num(123)


        
        


    