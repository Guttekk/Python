from student import Student


class HighschoolStudent(Student):

    school_name = "Zan"

    def get_school_name(self):
        return "Highschool student"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"