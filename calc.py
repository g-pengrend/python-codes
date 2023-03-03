num1 = int(input("Key in the first number: "))
num2 = int(input("Key in the second number: "))
symbol = input("Key in + or - or * or /: ")

if symbol == "+":
    ans = num1 + num2

elif symbol == "-":
    ans = num1 - num2

elif symbol == "*":
    ans = num1 * num2

print("The answer is: ", num1)