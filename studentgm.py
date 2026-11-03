# grade_manager.py

def get_grade(mark):
    """Determines the grade based on inclusive mark ranges."""
    if 90 <= mark <= 100:
        return "A"
    elif 80 <= mark <= 89:
        return "B"
    elif 70 <= mark <= 79:
        return "C"
    elif 60 <= mark <= 69:
        return "D"
    else:
        return "E"

def add_student(students):
    """Asks for student name and mark, validates inputs, and stores them.
    
    Storage choice: A list of dictionaries. This allows multiple students 
    with the same name (e.g., two Priyas) to be stored distinctly without 
    overwriting each other, while keeping track of their individual marks.
    """
    # Get and validate name
    while True:
        name = input("Enter student name: ").strip()
        if name:
            # Capitalize name nicely
            name = name.title()
            break
        print("Name cannot be empty. Please try again.")

    # Get and validate mark
    while True:
        mark_input = input("Enter mark (0-100): ").strip()
        try:
            mark = float(mark_input)
            if 0 <= mark <= 100:
                # Round to 2 decimal places if it's a float, or int if whole
                if mark.is_integer():
                    mark = int(mark)
                else:
                    mark = round(mark, 2)
                break
            else:
                print("Invalid range! Mark must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a valid number for the mark.")

    # Store the student record
    grade = get_grade(mark)
    students.append({"name": name, "mark": mark, "grade": grade})
    print(f"Successfully added {name} with mark {mark} (Grade: {grade}).\n")

def show_results(students):
    """Prints a neatly aligned table of all students along with class statistics."""
    if not students:
        print("\nNo student records found. Add some students first!\n")
        return

    print("\n" + "=" * 40)
    print(f"{'Name':<15}{'Mark':<10}{'Grade':<5}")
    print("-" * 40)

    total_marks = 0
    highest_mark = students[0]["mark"]
    lowest_mark = students[0]["mark"]

    for student in students:
        name = student["name"]
        mark = student["mark"]
        grade = student["grade"]
        
        print(f"{name:<15}{mark:<10}{grade:<5}")

        total_marks += mark
        if mark > highest_mark:
            highest_mark = mark
        if mark < lowest_mark:
            lowest_mark = mark

    average = total_marks / len(students)

    print("-" * 40)
    print(f"Average: {average:.1f}  Highest: {highest_mark}  Lowest: {lowest_mark}")
    print("=" * 40 + "\n")

def main():
    """Main menu loop that runs the program without crashing on bad inputs."""
    students = []

    print("Welcome to the Student Grade Manager!")

    while True:
        print("Menu:")
        print("1. Add Student")
        print("2. Show Results")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_results(students)
        elif choice == "3":
            print("\nExiting Student Grade Manager. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()