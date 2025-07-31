1. #Create a class called calculator
2. #Create a function in the class for each mathematical operation: Addition, Multiplication, Division, Subtraction
3. #Outside of your class definition, create an instance of your calculator class
4. #Call each function in your calculator class and store each output into a variable. Use any values for arguments.
5. #Print all your variables to the console
  # 1. Create a class called Calculator
  
class Calculator:
    # 2. Function for addition
    def add(self, a, b):
        return a + b

    # Function for multiplication
    def multiply(self, a, b):
        return a * b

    # Function for division
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Cannot divide by zero"

    # Function for subtraction
    def subtract(self, a, b):
        return a - b

# 3. Create an instance of your Calculator class
my_calculator = Calculator()

# 4. Call each function and store the result in variables
sum_result = my_calculator.add(10, 5)
product_result = my_calculator.multiply(10, 5)
quotient_result = my_calculator.divide(10, 5)
difference_result = my_calculator.subtract(10, 5)

# 5. Print all your variables to the console
print("Sum:", sum_result)
print("Product:", product_result)
print("Quotient:", quotient_result)
print("Difference:", difference_result)