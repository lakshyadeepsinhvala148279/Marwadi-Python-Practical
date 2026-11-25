#Write a Python program to handle invalid input entered by the user.
try:
    number = int(input("Enter a number:"))
    print("you entered",number)

except ValueError:
    print("Error:Invalid input. please enter a number")
