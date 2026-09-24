def addition(a, b):
    return (a + b)

def subtraction(a, b):
    return (a - b)

def multiplication(a, b):
    return (a * b)

def division(a, b):
    return (a / b)

def modulus(a, b):
    return (a % b)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nCalculator Results")

print("Addition: ", addition(num1, num2))
print("Subtraction: ", subtraction(num1, num2))
print("Multiplication: ", multiplication(num1, num2))

if num2 != 0:
    print("Division: ", division(num1, num2))
    print("Modulus: ", modulus(num1, num2))
else:
    print("Division and modulus cannot be calculated with zero.")    

