"""
Ranking: Top Students by Mean Grade

Finds the best and second-best student based on mean grade.
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

best_mean=None
sec_best_mean=None
sec_best_stud=None
best_stud=None
for stud,grade in stud_analytics.items():
    if best_mean is None or grade["mean"]>best_mean:
        sec_best_mean=best_mean
        sec_best_stud=best_stud
        
        best_mean=grade["mean"]
        best_stud=stud
    elif sec_best_mean is None or grade["mean"]>sec_best_mean:
        sec_best_mean=grade["mean"]
        sec_best_stud=stud
print(best_stud,best_mean)    
print(sec_best_stud,sec_best_mean) 
