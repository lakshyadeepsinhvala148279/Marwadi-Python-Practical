#Write a Python program to use try–except–else block.
try:
    attemps = int(input("Enter a number of login attemps:"))

except ValueError:
    print("Error:Invalid input. please enter a number")

else:
    print("login attemps recorded:",attemps)
