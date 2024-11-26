#"Student Grades Analysis"

input_grades = input("Enter students' grades separated by spaces: ")

grades_strings = input_grades.split()

grades = list(map(int, grades_strings))

highest_grade = max(grades)
lowest_grade = min(grades)

average_grade = sum(grades) / len(grades)

sorted_grades = sorted(grades, reverse=True)

average_grade_rounded = round(average_grade, 2)

print("\nGrade Analysis:")
print(f"Highest Grade: {highest_grade}")
print(f"Lowest Grade: {lowest_grade}")
print(f"Average Grade: {average_grade_rounded}")
print(f"Grades Sorted (Highest to Lowest): {sorted_grades}")
