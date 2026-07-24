def get_input():
    test_name = input("Enter the name of the test: ")
    teacher_name = input("Enter the name of the teacher: ")
    student_name = input("Enter the name of the student: ")

    score = int(input("Enter the score of this student's test: "))
    grade = input("Enter the grade of this student's test: ")

    return test_name, teacher_name, student_name, score, grade


def display_results(test_name, teacher_name, student_name, score, grade):
    print("Test Name: ", test_name)
    print("Teacher Name: ", teacher_name)
    print("Student Name: ", student_name)
    print("Score: ", score)
    print("Grade: ", grade)





# main programs start here #
def main():