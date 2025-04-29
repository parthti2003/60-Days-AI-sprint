# Student Grading System

###########################################################################

# Function to assign grade based on the average marks
def calculate_grade(average):
    if average >= 90:
        return 'A+'
    elif average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'

# Function to calculate total and average
def student_grading_system():
    print("Enter the number of subjects:")
    num_subjects = int(input())
    
    total_marks = 0
    
    for i in range(num_subjects):
        print(f"Enter marks for subject {i+1}:")
        marks = float(input())
        total_marks += marks
    
    average_marks = total_marks / num_subjects
    grade = calculate_grade(average_marks)
    
    print(f"\nTotal Marks: {total_marks}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Grade: {grade}")

# Run the grading system
student_grading_system()
