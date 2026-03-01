"""
Filtering: High Performing Students

This script filters students based on performance.

Input:
student -> summary statistics

Output:
subset of students with mean grade >= 17

This demonstrates a basic filtering operation in data analysis.
"""
students = {
    "nikos": [17, 18, 16],
    "maria": [15, 19, 14],
    "kostas": [10, 12, 9],
    "anna": [18, 18, 19]
}
stud_analytics = {}

for stud, grades in students.items():
    total = 0
    maxim = None
    for g in grades:
        total += g
        if maxim is None or g > maxim:
            maxim = g
    stud_analytics[stud] = {
        "max": maxim,
        "mean": total / len(grades),
        "count": len(grades)
    }
high_performers = {}

for stud, grades in stud_analytics.items():
    if grades["mean"] >= 17:
        high_performers[stud] = grades

print(high_performers)
