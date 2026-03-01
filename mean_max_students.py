"""
Aggregation: Student Grade Summary

This script calculates summary statistics for each student.

Input:
student -> list of grades

Output:
student -> {
    mean: average grade
    max: highest grade
    count: number of grades
}

This demonstrates a basic aggregation operation in data analysis.
"""
students = {
    "nikos": [17, 18, 16],
    "maria": [15, 19, 14],
    "kostas": [10, 12, 9],
    "anna": [18, 18, 19]
}
stud_analytics={}
for stud,grades in students.items():
    total=0
    maxim=None 
    for g in grades:
        total+=g
        if maxim is None or g>maxim:
            maxim=g
    stud_analytics[stud]={
        "max":maxim,
        "mean":total/len(grades),
        "count":len(grades)
        }
print(stud_analytics)  
