"""
Data Cleaning: Student Grade Dataset

This script removes invalid values from a dataset
containing student grades.

Cleaning rules:
- grade must be numeric (int or float)
- grade must be between 0 and 20

Demonstrates basic data cleaning techniques
used before performing data analysis.
"""

students = {
    "nikos": [17, 18, "A", 16],
    "maria": [15, None, 19, 14],
    "kostas": [10, 12, -5, 9],
    "anna": [18, 18, 19, 105]
}

cleaned_students={}
for studs,grades in students.items():
    clean_grades=[]
    for i in grades:
        if isinstance(i,(int,float)) and 0<=i<=20:
            clean_grades.append(i)
    cleaned_students[studs]=clean_grades
print(cleaned_students)
