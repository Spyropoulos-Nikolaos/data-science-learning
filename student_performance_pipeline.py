"""
Student Performance Pipeline

A small pure Python project for processing student grades.
"""
students_raw = {
    "nikos": [17, 18, "A", 16],
    "maria": [15, None, 19, 14],
    "kostas": [10, 12, -5, 9],
    "anna": [18, 18, 19, 105]
}

#Functions

#1)clean data

def clean_data(students_raw):
    students_clean = {}
    for stud, grades in students_raw.items():
        grades_clean = []
        for g in grades:
            if isinstance(g, (int, float)) and 0 <= g <= 20:
                grades_clean.append(g)
        students_clean[stud] = grades_clean
    return students_clean

#2)compute statistics

def compute_statistics(students_clean):
    stud_analytics = {}
    for stud, grades in students_clean.items():
        total = 0
        max_g = None
        min_g = None
        for g in grades:
            total += g
            if max_g is None or max_g < g:
                max_g = g
            if min_g is None or min_g > g:
                min_g = g
        n = len(grades)
        mean = total / n
        total_var_sq = 0
        for g in grades:
            total_var_sq += (g - mean) ** 2
        var_g = total_var_sq / n
        std_dev = (var_g) ** 0.5
        range_g = max_g - min_g
        stud_analytics[stud] = {
            "grades": grades,
            "mean": mean,
            "max": max_g,
            "min": min_g,
            "range": range_g,
            "variance": var_g,
            "std_dev": std_dev,
            "count": n
        }
    return stud_analytics

#3) filter high performers
def filter_high_performers(stud_analytics):
    high_performers = {}
    for stud, stats in stud_analytics.items():
        mean = stats["mean"]
        if mean >= 17:
            high_performers[stud] = stats
    return high_performers

#4) rank top students
def rank_top_students(stud_analytics):
    best_mean = sec_best_mean = None
    best_stud = sec_best_stud = None

    for stud, grades in stud_analytics.items():
        mean = grades["mean"]
        if best_mean is None or mean > best_mean:
            sec_best_mean = best_mean
            sec_best_stud = best_stud
            best_mean = mean
            best_stud = stud
        elif sec_best_mean is None or mean > sec_best_mean:
            sec_best_mean = mean
            sec_best_stud = stud
    best_students = {
        "1st student": {
            "name": best_stud,
            "mean": best_mean
            },
        "2nd student": {
            "name": sec_best_stud,
            "mean": sec_best_mean
            }
        }
    return best_students

#5) pivot grades

def pivot_grades(stud_analytics):
    grade_to_students = {}
    for stud, stats in stud_analytics.items():
        grades = stats["grades"]
        for g in grades:
            if g not in grade_to_students:
                grade_to_students[g] = []
                grade_to_students[g].append(stud)
            else:    
                if stud not in grade_to_students[g]:
                    grade_to_students[g].append(stud)
    sorted_grade_to_students = {}
    for g in sorted(grade_to_students):
        sorted_grade_to_students[g] = grade_to_students[g]
    return sorted_grade_to_students

#6) classify risk
def classify_risk(stud_analytics):
    risk_levels = {}
    for stud, stats in stud_analytics.items():
        mean = stats["mean"]
        if mean >= 15:
            risk_level = "safe"
        elif mean >= 12:
            risk_level = "moderate risk"
        else:
            risk_level = "high risk"
        risk_levels[stud] = {
            "mean": mean,
            "risk": risk_level
            }
    return risk_levels

#program flow

def main():   
    students_clean = clean_data(students_raw)
    stud_analytics = compute_statistics(students_clean)
    high_performers = filter_high_performers(stud_analytics)
    best_students = rank_top_students(stud_analytics)
    grade_to_students = pivot_grades(stud_analytics)
    risk_levels = classify_risk(stud_analytics)

    print(students_clean)
    print(stud_analytics)
    print(high_performers)
    print(best_students)
    print(grade_to_students)
    print(risk_levels)

if __name__ == "__main__":
    main()
    
