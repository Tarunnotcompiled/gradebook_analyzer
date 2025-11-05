# GradeBook Analyzer
# Name: Tarun Yadav 
# Date: 2025-11-05
#roll no.=2501410064
# Title: GradeBook Analyzer

def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    sorted_marks = sorted(marks_dict.values())
    n = len(sorted_marks)
    if n % 2 == 0:
        return (sorted_marks[n//2 - 1] + sorted_marks[n//2]) / 2
    else:
        return sorted_marks[n//2]

def find_max_score(marks_dict):
    return max(marks_dict.values())

def find_min_score(marks_dict):
    return min(marks_dict.values())

def assign_grade(marks_dict):
    grades = {}
    for name, mark in marks_dict.items():
        if mark >= 90:
            grades[name] = "A"
        elif mark >= 80:
            grades[name] = "B"
        elif mark >= 70:
            grades[name] = "C"
        elif mark >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"
    return grades

def count_grades(grades_dict):
    counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for grade in grades_dict.values():
        counts[grade] += 1
    return counts

def main():
    print("Welcome to GradeBook Analyzer!")
    while True:
        print("\n--- GradeBook Analyzer Menu ---")
        print("1. Enter student data")
        print("2. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            marks = {}
            num_students = int(input("Enter number of students: "))
            for _ in range(num_students):
                name = input("Enter student name: ")
                mark = int(input("Enter marks: "))
                marks[name] = mark

            grades = assign_grade(marks)
            grade_counts = count_grades(grades)

            print("\n--- Statistics ---")
            print(f"Average: {calculate_average(marks):.2f}")
            print(f"Median: {calculate_median(marks):.2f}")
            print(f"Max: {find_max_score(marks)}")
            print(f"Min: {find_min_score(marks)}")

            print("\n--- Grade Summary ---")
            for grade, count in grade_counts.items():
                print(f"{grade}: {count}")

            passed = [name for name, mark in marks.items() if mark >= 40]
            failed = [name for name, mark in marks.items() if mark < 40]
            print(f"\nPassed: {len(passed)} students: {passed}")
            print(f"Failed: {len(failed)} students: {failed}")

            print("\n--- Results Table ---")
            print(f"{'Name':<12} {'Marks':<8} {'Grade':<8}")
            print("-" * 30)
            for name, mark in marks.items():
                print(f"{name:<12} {mark:<8} {grades[name]:<8}")
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
