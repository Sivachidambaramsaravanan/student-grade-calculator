def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good effort! You can do better 🙂"
    elif marks >= 60:
        return "D", "You passed. Work harder 💪"
    else:
        return "F", "Don't give up. Try again! 💡"


# Main Program
print("🎓 STUDENT GRADE CALCULATOR 🎓")

student_name = input("Enter student name: ")

while True:
    try:
        marks = int(input("Enter marks (0-100): "))

        if marks < 0 or marks > 100:
            print("❌ Invalid marks! Please enter between 0 and 100.")
            continue

        grade, message = calculate_grade(marks)

        print("\n📊 RESULT FOR", student_name.upper())
        print("Marks:", marks, "/100")
        print("Grade:", grade)
        print("Message:", message)
        break

    except ValueError:
        print("❌ Please enter numbers only!")