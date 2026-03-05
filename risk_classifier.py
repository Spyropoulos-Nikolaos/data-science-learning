"""
Simple Prediction Logic: Student Risk Classification

This script classifies students into risk categories
based on their average grade.

Rules:
mean >= 15 → Safe
12 <= mean < 15 → Moderate Risk
mean < 12 → High Risk

Demonstrates rule-based classification logic.
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
risk_levels={}
for stud,statistix in stats.items():
    mean=statistix["mean"]
    if mean>=15:
        risk_levels[stud]="safe"
    elif mean>=12:
        risk_levels[stud]="moderate risk"
    else:
        risk_levels[stud]="high risk"
print(risk_levels)
