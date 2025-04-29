def print_top_students(students, threshold):
    print("🎯 Students scoring above", threshold)
    for name, marks in students.items():
        if marks > threshold:
            print(f"✅ {name} -> {marks} marks")
students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "David": 65,
    "Eva": 95
}
print_top_students(students, 80)
