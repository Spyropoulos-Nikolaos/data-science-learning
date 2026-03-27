# Student performance analysis using pandas

## Overview

This project analyses a student performance dataset using pandas.  
The aim is to explore academic performance patterns through data cleaning, feature engineering, and exploratory data analysis.

The analysis focuses on grades, attendance, pass rates, and academic risk across courses, teachers, cities, and semesters.

## Dataset

The dataset includes the following columns:

- `student_id`
- `student_name`
- `course`
- `semester`
- `teacher`
- `city`
- `hours_study`
- `absences`
- `assignments_completed`
- `exam_score`
- `final_grade`

## Project steps

The analysis followed these main steps:

1. Initial data inspection  
2. Data quality checks  
3. Data cleaning  
4. Feature engineering  
5. Exploratory data analysis  

## Techniques used

The main techniques used in this project include:

- pandas
- data cleaning
- grouping and aggregation
- sorting
- feature engineering
- exploratory data analysis

## Key findings

- Biology recorded the lowest average final grade among all courses.
- Mathematics showed a 100% pass rate despite having a relatively lower average final grade.
- Heraklion had the highest average number of absences.
- Teachers with higher average grades also tended to have lower average absences.
- Academic performance showed a slight improvement from semester 1 to semester 2.
- Biology contained the highest number of medium- and high-risk students, while Informatics had the lowest.

## Repository structure

```text
student-performance-analysis-pandas/
│
├── data/
│   ├── student_performance_raw.csv
│   └── student_performance_clean.csv
│
├── student_performance_analysis.ipynb
├── README.md
└── requirements.txt