students = []


def add_student(name, number=1):
    student = {"Name": name, "Number": number}
    students.append(student)


def get_students():
    students_list = []
    for student in students:
        students_list.append(student["Name"])
    return students_list


def print_students():
    students_list = get_students()
    for student in students_list:
        print(student)


def save_student(student):
    try:
        add_student(student)
        f = open("Students.txt", 'a')
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save to the file")


def load_students():
    try:
        f = open("Students.txt", "r")
        loaded_students = f.readlines()
        for student in loaded_students:
            add_student(student)
        f.close()
    except Exception:
        print("Could not load students")


load_students()
print("Starting students list: \n")
print_students()

add_student_question = "Yes"

while add_student_question == "Yes":
    student_name = input("Name: ")
    save_student(student_name)
    add_student_question = input("Do you want to add another student?(Yes/No): ")

print("Ending students lust: \n")
print_students()
