student_scores = {
    "harry": 81,
    "ron": 78,
    "herminone": 99,
    "draco": 74,
    "neville": 62,   
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 70:
        student_grades[key] = "Acceptable"
        if student_scores[key] > 80:
            student_grades[key] = "Exceeds Expectations"
            if student_scores[key] > 90:
                student_grades[key] = "Outstanding"
    else:
        student_grades[key] = "Fail"
    """
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
    """

print(student_grades)