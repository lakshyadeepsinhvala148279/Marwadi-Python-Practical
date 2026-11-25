print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:[ENROLLMENT NUMBER]")


# Parent Class
class Animal:
    def speak(self):
        print("Animal makes a generic sound.")

# Child Class overriding the speak method
class Dog(Animal):
    def speak(self):
        print("Dog barks: Woof Woof!")

# Main Execution
print("Student Enrolment No: [ENROLLMENT NUMBER] ")
print("Name: [STUDENT NAME] \n")

# Object of Parent Class
generic_animal = Animal()
print("Calling Animal's speak method:")
generic_animal.speak()

print()

# Object of Child Class
dog = Dog()
print("Calling Dog's overridden speak method:")
dog.speak()
