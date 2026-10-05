number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

if number1 > number2 and number1 > number3:
    print("number1 is the biggest number.")
elif number2 > number1 and number2 > number3:
    print("number2 is the biggest number.")
elif number3 > number1 and number3 > number2:
    print("number3 is the biggest number.")
if number1 == number2 and number1 > number3:
    print("number1 and number2 are the biggest numbers")

if number1 < number2 and number1 < number3:
    print("number1 is the smallest number.")
elif number2 < number1 and number2 < number3:
    print("number2 is the smallest number.")
elif number3 < number1 and number3 < number2:
    print("number3 is the smallest number.")
