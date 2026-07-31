def get_testinfo():
    test_name = input("Enter the name of the test: ")
    teacher_name = input("Enter the name of the teacher: ")
    return test_name, teacher_name


def get_student_name():
    return input("Enter the name of the student: ")


def find_score():
    while True:
        try:
            score = int(input("Enter the student's score (0-100): "))
            if 0 <= score <= 100:
                return score
            print("Score has to be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def get_grade(score):
    if score >= 90:
        return "E"
    elif score >= 70:
        return "M"
    elif score >= 50:
        return "A"
    else:
        return "NA"


def display_results(test_name, teacher_name, student_name, score, grade):
    print("\n--- Student Result ---")
    print("Test Name:", test_name)
    print("Teacher Name:", teacher_name)
    print("Student Name:", student_name)
    print("Score:", score)
    print("Grade:", grade)


def main():
    test_name, teacher_name = get_testinfo()

    while True:
        student_name = get_student_name()
        score = find_score()
        grade = get_grade(score)

        display_results(test_name, teacher_name, student_name, score, grade)

        another = input("\nDo you want to add another student? (yes/no): ").lower()
        if another != "yes":
            print("\nProgram finished.")
            break


main()