# This program uses numpy to analyze student grades stored in the CSV file,
# then it performs calculations and operations to gain insights into the
# dataset. -Livia Augusto Razera, Assignment 12.

import numpy as np
import csv

# Function gets numeric scores from the CSV and loads it into numpy array. 
def load_grades(filename='grades.csv'):
    
    grades = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            grades.append([int(row[2]), int(row[3]), int(row[4])])
    return np.array(grades)

# Function that displays exam statistics.
def print_exam_statistics(grades):
    print('\nExam Statistics (each column is an exam):')
    for i in range(grades.shape[1]):
        exam = grades[:, i]
        print(f'\nExam {i+1}:')
        print(f'  Mean: {np.mean(exam):.2f}')
        print(f'  Median: {np.median(exam):.2f}')
        print(f'  Std Dev: {np.std(exam):.2f}')
        print(f'  Min: {np.min(exam)}')
        print(f'  Max: {np.max(exam)}')

# Function that displays overall statistics.
def print_overall_statistics(grades):
    all_grades = grades.flatten()
    print('\nOverall Statistics (all exams combined):')
    print(f'  Mean: {np.mean(all_grades):.2f}')
    print(f'  Median: {np.median(all_grades):.2f}')
    print(f'  Std Dev: {np.std(all_grades):.2f}')
    print(f'  Min: {np.min(all_grades)}')
    print(f'  Max: {np.max(all_grades)}')

# Function that finds out and displays whether the student passed or failed.
def print_pass_fail_stats(grades, pass_mark=60):
    print('\nPass/Fail per Exam:')
    total_passes = 0
    total_grades = grades.size

    for i in range(grades.shape[1]):
        exam = grades[:, i]
        passed = np.sum(exam >= pass_mark)
        failed = np.sum(exam < pass_mark)
        total_passes += passed
        print(f'Exam {i+1}: Passed = {passed}, Failed = {failed}')

    overall_pass_percent = (total_passes / total_grades) * 100
    print(f'\n Overall Pass Percentage: {overall_pass_percent:.2f}%')

# Main function which display all the results.
def main():
    grades = load_grades()

    print('First 5 rows of grade data:')
    print(grades[:5])

    print_exam_statistics(grades)

    print_overall_statistics(grades)

    print_pass_fail_stats(grades)

# Calls out main function.
if __name__ == '__main__':
    main()