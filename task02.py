num = int(input("Enter a number: "))

# for loop
print("\nNumbers from 1 to", num)

for i in range(1, num):
    print(i)

# while 
print("\nNumbers from", num, "to 1")

i = num
while i >= 1:
    print(i)
    i -= 1

# Multiplication of num
print("\nMultiplication of", num)

for i in range(1, 11):
    result = num * i
    print(num, "x", i, "=", result)

    