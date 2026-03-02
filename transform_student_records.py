"""
Transformation: Student Analytics to Record Format

This script transforms a nested dictionary structure into
a list of flat records.

Original structure:
student -> summary statistics

Transformed structure:
list of records containing student name and statistics

This demonstrates a basic data transformation operation.
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

records=[]
for stud,stats in stud_analytics.items():
    record={
        "student":stud,
        "max":stats["max"],
        "mean":stats["mean"],
        "count":stats["count"]
        }
    records.append(record)
print(records)
