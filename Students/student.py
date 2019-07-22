students = []


class Student:

    school_name = "Polibuda"

    def __init__(self, name, number=1):
        self.name = name
        self.number = number
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name
