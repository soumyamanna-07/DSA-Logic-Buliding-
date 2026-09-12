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

# def num(n):
#     sum = 0
#     for i in str(n):
#         sum = sum + int(i)
#     print(sum)
# num(123)
                                 

                             # 8.REVERSE A NUMBER
# def num(n):
#     reverse = 0
#     while n != 0:
#         digit = n %10
#         reverse = reverse * 10 + digit
#         n = n // 10
#     return reverse
    
# print(num(123))

# def num(n):
#     reverse = 0
#     while n >0:
#         digit = n % 10
#         reverse = (reverse * 10 ) + digit
#         n = n // 10
#     return reverse
# print(num(123))


                         # 10.Palindrome  or Not  of a string
# def palindrome(x):
#     reverse = x[::-1]
#     print(reverse)
    
#     if reverse == x:
#          print("The number is palindrome")
#     else:
#          print("The no is not pLindrome")
# palindrome("madam")

                        # 11.Palindrome or not of a number
# def num(x):
#      reverse = 0
#      original = x
#      while x != 0:
#           digit = x % 10
#           reverse = (reverse * 10 ) + digit
#           x = x // 10
#      if original == reverse:
#           print("The number is Plaindrome")
#      else:
#           print("The number is not palindrome")
# num(1213)


                         #10. Check whether a number is an Armstrong number.

# def num(x):
#     orginal = x
#     total_sum = 0
#     power = len(str(x))
#     while x > 0:
#         digit = x % 10
#         total_sum += (digit ** power )
#         x = x // 10
#     if orginal == total_sum:
#         print("The number is Armstrong")
#     else:
#         print("The number is not Armstrong")
# num(1634)

                                  #11. Find the GCD of two numbers.

# import math
# def num(x,y):               # Using python build function
#     result = math.gcd(x, y)
#     print(result)  # Outputs: 4
# num(14,16)


def num(x,y):
    while y > 0:
        c =  x % y
        x = y
        y = c
    return x
print(num(14,16))

        





      


     


    
    
        
    






        
        


    