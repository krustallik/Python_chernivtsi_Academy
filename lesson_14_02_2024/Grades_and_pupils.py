def display_grades(grades):
    print("Student's grades:", grades)


def retake_exam(grades):
    try:
        retake_count = int(input("Enter the number of tasks you want to retake: "))
        for _ in range(retake_count):
            while True:
                index = int(input("Enter the index of the task you want to retake (starting from 1): "))
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

        print("Updated list of grades after retaking exams:", grades)
    except ValueError:
        print("Invalid input.")


def check_reward(grades):
    average_grade = sum(grades) / len(grades)
    return average_grade >= 8.0


try:
        num_grades = int(input("Enter the number of grades: "))
        grades = []
        for i in range(num_grades):
            while True:
                grade = float(input("Enter grade {} (1-12): ".format(i + 1)))
                if 1 <= grade <= 12:
                    grades.append(grade)
                    break
                else:
                    print("Invalid grade entered. Grade must be between 1 and 12.")

        display_grades(grades)

        retake = input("Do you want to retake any tasks? (yes/no): ").lower()
        if retake == 'yes':
            retake_exam(grades)

        print("Updated list of grades:", grades)

        reward_allowed = check_reward(grades)
        if reward_allowed:
            print("The student is eligible for an award!")
        else:
            print("The student is not eligible for an award.")

except ValueError:
        print("Invalid input.")
