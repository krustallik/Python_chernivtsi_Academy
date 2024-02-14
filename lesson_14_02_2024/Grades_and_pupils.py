
#не у всіх моментах прописав try excep або while щоб при неправильних данних код не перестава робити але нажаль немаю багато часу
def display_grades(student_grades):
    for student, grades in student_grades.items():
        print(f"{student}'s grades: {grades}")

def retake_exam(student_grades, students_to_retake):
    try:
        for student in students_to_retake:
            grades = student_grades.get(student, [])

            if not grades:
                print(f"No grades found for {student}.")
                continue

            print(f"Current grades for {student}: {grades}")

            retake_count = int(input(f"Enter the number of tasks {student} wants to retake: "))
            for _ in range(retake_count):
                while True:
                    index = int(input(f"Enter the index of the task to retake (starting from 1): "))
                    if 1 <= index <= len(grades):
                        break
                    else:
                        print("Invalid index entered.")

                while True:
                    new_grade = float(input("Enter the new grade for the task (1-12): "))
                    if 1 <= new_grade <= 12:
                        grades[index - 1] = new_grade
                        break
                    else:
                        print("Invalid grade entered. Grade must be between 1 and 12.")

            student_grades[student] = grades
            print(f"Updated list of grades for {student} after retaking exams: {grades}")
    except ValueError:
        print("Invalid input.")

def check_reward(grades):
    average_grade = sum(grades) / len(grades)
    return average_grade >= 8.0

try:
    num_students = int(input("Enter the number of students: "))
    student_grades = {}

    for _ in range(num_students):
        student = input("Enter student's name: ")
        grades = []

        num_grades = int(input(f"Enter the number of grades for {student}: "))
        for i in range(num_grades):
            while True:
                grade = float(input(f"Enter grade {i + 1} (1-12): "))
                if 1 <= grade <= 12:
                    grades.append(grade)
                    break
                else:
                    print("Invalid grade entered. Grade must be between 1 and 12.")

        student_grades[student] = grades

    display_grades(student_grades)

    retake = input("Do you want to retake exams for any students? (yes/no): ").lower()
    if retake == 'yes':
        students_to_retake = input("Enter the names of students (comma-separated) who want to retake exams: ").split(',')
        students_to_retake = [name.strip() for name in students_to_retake]
        retake_exam(student_grades, students_to_retake)

    display_grades(student_grades)

    reward_allowed = all(check_reward(grades) for grades in student_grades.values())
    if reward_allowed:
        print("All students are eligible for an award!")
    else:
        print("Some students are not eligible for an award.")

except ValueError:
    print("Invalid input.")

#не у всіх моментах прописав try excep або while щоб при неправильних данних код не перестава робити але нажаль немаю багато часу
