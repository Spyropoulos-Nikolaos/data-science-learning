"""
Basic Statistics: Student Grade Analysis

This script calculates descriptive statistical measures
for each student based on their grades.

Computed metrics:
- mean
- min
- max
- range
- variance (population)
- standard deviation

This demonstrates how to implement core statistical
concepts from scratch using pure Python.
"""

students = {
    "nikos": [17, 18, 16],
    "maria": [15, 19, 14],
    "kostas": [10, 12, 9],
    "anna": [18, 18, 19]
}

stats={}
for stud,grades in students.items():
    maxg=None
    ming=None
    sumg=0
    for i in grades:
        if maxg is None or i>maxg:
            maxg=i
        if ming is None or i<ming:
            ming=i
        sumg+=i
    rangeg=maxg-ming
    meang=sumg/len(grades)
    varg=0
    for i in grades:
        varg+=(i-meang)**2/len(grades)
    stnd_dev=varg**0.5
    stats[stud]={
        "max":maxg,
        "min":ming,
        "mean":meang,
        "range":rangeg,
        "variance":varg,
        "standard deviation":stnd_dev
    }
print(stats)    
