# GradeBook Analyzer

**Name:** Tarun Yadav  
**Roll No:** 2501410064  
**Date:** 2025-11-05  
**Title:** GradeBook Analyzer  

---

## 🧮 Overview

GradeBook Analyzer is a Python-based program that helps teachers or students manage and analyze grades. It allows users to input student names and marks, then calculates essential statistics such as average, median, maximum, and minimum scores. It also assigns letter grades, counts the grade distribution, and shows the number of students who passed or failed.

<img width="585" height="525" alt="Screenshot" src="https://github.com/user-attachments/assets/366aaf36-1428-4237-a01c-0f12b5122eb5" />

---

## 🚀 Features

- Interactive console menu for data entry  
- Calculation of average, median, maximum, and minimum marks  
- Automatic letter grade assignment (A–F)  
- Summary of grade distribution  
- Identification of passed and failed students  
- Display of formatted results in a table  

---

## 📊 Grade Criteria

| Marks Range | Grade |
|--------------|--------|
| 90 and above | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| Below 60 | F |

---

## ⚙️ Functions Used

| Function | Description |
|-----------|--------------|
| `calculate_average(marks_dict)` | Returns the average of all marks. |
| `calculate_median(marks_dict)` | Returns the median mark. |
| `find_max_score(marks_dict)` | Finds the highest mark. |
| `find_min_score(marks_dict)` | Finds the lowest mark. |
| `assign_grade(marks_dict)` | Assigns letter grades based on the scoring scheme. |
| `count_grades(grades_dict)` | Counts how many students received each grade. |

---

## 🧑‍💻 How to Run

1. Ensure **Python 3.8+** is installed on your system.  
2. Save the program as `gradebook_analyzer.py`.  
3. Run the file from the terminal:
