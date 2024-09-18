# 1Write a Python script that prints "Hello, World!"
# 2Create a script that takes user input and prints it.
# 3Write a script that uses both single-line and multi-line comments.
# 4Write a script that demonstrates indentation in Python.
# 5Write a script that shows how to break lines in Python
#6 Add comments to explain each line of a given script.
# 7Write a script and use comments to explain a function's purpose.
# 8Add a block comment to describe the script's overall functionality.
# 9Use comments to disable a part of the script and re-enable it.
#10 Write a script with intentional errors and comment on why they occur.
#11 Write a script to demonstrate a for loop.
# 12Create a script that uses a for loop to iterate over a list.
# 13Write a script that uses a for loop with the range() function.
# 14Demonstrate nested for loops.
# 15Create a script that uses a for loop with an else clause.



# 1 Write a Python script that prints "Hello, World!"
print("hello world")



# 2 Create a script that takes user input and prints it.
user_inout =  input("enter what you want")
print(user_inout)



# 3 Write a script that uses both single-line and multi-line comments.

def factorial_iterative(n):


    result = 1
 
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):

   
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

number = 5  

print(f"Factorial of {number} (iterative): {factorial_iterative(number)}")

print(f"Factorial of {number} (recursive): {factorial_recursive(number)}")

# 4 Write a script that demonstrates indentation in Python.


def example_function(n):
   
   
    print("Start of example_function")

    if n > 0:
     
        print("n is positive")
        for i in range(n):
           
            print(f"Current value of i: ")
            if i % 2 == 0:
                
                print("is an even number")
            else:
         
                print ("an odd number")
    else:
       
        print("n is not positive")
    
    print("End of example_function")

example_function(5)

# 5Write a script that shows how to break lines in Python. 
safghgfckaehcvg
cadjcgdhkcgl
chgdfc jvmadklcavcrq8F453E9DEFGEHJFTP{Z]XS[PFOJERHW]}


# 6 Add comments to explain each line of a given script.


def example_function(n):
   
    print("Start of example_function")  

    if n > 0:
        
        return"n is positive"
        for i in range(n):
         
            return"Current value of i: " 
            
            if i % 2 == 0:
            
                return" an even number"
            else:
                
                return" an odd number" 
    else:
       
        return"n is not positive" 

   
    return("End of example_function")  


example_function(5)  

#7

def is_perfect_number(n):


    
    if n <= 0:
        return False

    sum_of_divisors = 0

  
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i

 
    return sum_of_divisors == n


number = 28  
if is_perfect_number(number):
    print(f"{number} არის სრულყოფილი რიცხვი.")
else:
    print(f"{number} არ არის სრულყოფილი რიცხვი.")

#8

def is_perfect_number(n):
   
 
    if n <= 0:
        return False

   
    sum_of_divisors = 0

  
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i

    
    return sum_of_divisors == n

number = 28  
#9

def factorial(n):
 
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    result = 1
    
  
    for i in range(1, n + 1):
        result *= i
    
    return result




number = 7 
print(f"The factorial of {number} is {factorial(number)}.")

#10



def square_number(x):
    
    return x * x 


num = 5  


print(f"The square of {number} is {square_number(number)}.")  


print(f"The square of {num} is {square_number(num)}.")  


number = 7 
print(f"The square of {number} is {square_number(number)}.")  

#11


# ??????

#12
# ????
#13
# /????
#14
# ????
#15
# ????