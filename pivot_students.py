students = {
    "nikos": [17, 18, 16],
    "maria": [15, 19, 14],
    "kostas": [10, 12, 9],
    "anna": [18, 18, 19]
}

pivot = {}

for stud, grades in students.items():
    for g in grades:
        pivot[g] = pivot.get(g, []) + [stud]

print(pivot)
