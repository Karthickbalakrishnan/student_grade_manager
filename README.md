# Student Grade Manager

A simple command-line Python application for adding student marks, assigning letter grades, and displaying class statistics.

## RTCFR Overview

| Component | Description |
|---|---|
| **Role** | Student administration assistant |
| **Task** | Add students and calculate/report grades |
| **Context** | Local, terminal-based Python application |
| **Format** | Interactive menu and aligned results table |
| **Requirements** | Python 3 and a terminal; no external dependencies |

## Features

- Interactive menu with three options
- Name validation and title-case formatting
- Mark validation for values from `0` to `100`
- Automatic grade assignment
- Support for duplicate student names
- Average, highest, and lowest mark calculations
- Clear messages for invalid menu choices and inputs

## Grade Scale

| Mark Range | Grade |
|---:|:---:|
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| 0–59 | E |

## Project Structure

```text
student_grade_manager/
├── studentgm.py       # Main application entry point and application logic
├── .gitattributes     # Git text normalization configuration
├── .gitignore         # Python and development artifact exclusions
└── README.md          # Project documentation
```

## Requirements

- Python 3.6 or later
- A terminal or command prompt
- No third-party Python packages

## Installation and Run

### 1. Clone the repository

```bash
git clone https://github.com/Karthickbalakrishnan/student_grade_manager.git
cd student_grade_manager
```

### 2. Run the application

```bash
python studentgm.py
```

On Windows, `py` may be used instead:

```bash
py studentgm.py
```

## Usage

### Main Menu

```text
Welcome to the Student Grade Manager!
Menu:
1. Add Student
2. Show Results
3. Quit
```

### Add a Student

Enter `1` and provide a name and mark:

```text
Enter student name: priya
Enter mark (0-100): 92
Successfully added Priya with mark 92 (Grade: A).
```

Names are trimmed and converted to title case. For example, `priya sharma` becomes `Priya Sharma`.

### View Results

Enter `2` to display all records:

```text
========================================
Name           Mark      Grade
----------------------------------------
Priya          92        A
Arjun          77.5      C
----------------------------------------
Average: 84.8  Highest: 92  Lowest: 77.5
========================================
```

Enter `3` to exit the application.

## Application Logic

Student records are kept in memory as a list of dictionaries:

```python
students = [
    {
        "name": "Priya",
        "mark": 92,
        "grade": "A"
    }
]
```

### Key Functions

- `get_grade(mark)` assigns a letter grade.
- `add_student(students)` validates input and adds a record.
- `show_results(students)` prints the table and class statistics.
- `main()` runs the interactive menu loop.

## Input Validation

### Names

- Whitespace-only names are rejected.
- Leading and trailing whitespace is removed.
- Empty names require another attempt.
- Names are converted to title case.

### Marks

Valid examples include:

- `78`
- `78.5`
- `90.0`

Invalid examples include:

- Negative values
- Values greater than `100`
- Non-numeric text
- Empty input

Whole-number values are stored as integers. Decimal values are rounded to two decimal places.

## Limitations

- Records exist only in memory and are lost after exiting.
- There is no editing or deleting functionality.
- No database or file persistence is implemented.
- Duplicate names are allowed and stored as separate records.
- Automated tests are not included.
- The application is terminal-only.

## Possible Improvements

- Add CSV or JSON persistence
- Add search, edit, and delete operations
- Add ranking and pass/fail reports
- Export results to a file
- Add automated unit tests
- Add a graphical or web interface

## License

No license is currently declared. Obtain clarification from the repository owner before redistribution or reuse.

## Author

**Karthickbalakrishnan**

- GitHub: [@Karthickbalakrishnan](https://github.com/Karthickbalakrishnan)
- Repository: [student_grade_manager](https://github.com/Karthickbalakrishnan/student_grade_manager)
