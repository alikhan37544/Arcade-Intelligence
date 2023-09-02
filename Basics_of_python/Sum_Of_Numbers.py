# Python program to find out the sum of first n numbers
user_input = int(input("Enter the number to find the sum of: "))
sum = 0
for i in range(1, user_input + 1):
    sum += i
print("The sum of first " + str(user_input) + " numbers is: " + str(sum))