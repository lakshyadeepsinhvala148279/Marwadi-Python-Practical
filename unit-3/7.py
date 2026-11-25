#Write a Python program to use try–except–finally block.
try:
    attemps = int(input("Enter a number of login attemps:"))
    print("Login attemps",attemps)

except ValueError:
    print("Error:Invalid input. please enter a number")

finally:
    print("Security check completed.")
