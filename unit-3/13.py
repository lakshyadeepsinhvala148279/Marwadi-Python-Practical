print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:[ENROLLMENT NUMBER]")


class Parent:

    def feature_parent(self):
        print("This is parent class.")


class Mother:

    def feature_mother(self):
        print("This is mother class.")


class ChildMultilevel(Parent):

    def feature_child(self):
        print("This is multilevel child class.")


class ChildMultiple(Parent, Mother):

    def feature_multiple(self):
        print("This is multiple inheritance child class.")


if __name__ == "__main__":
    c1 = ChildMultilevel()
    c1.feature_parent()
    c1.feature_child()

    c2 = ChildMultiple()
    c2.feature_parent()
    c2.feature_mother()
    c2.feature_multiple()
