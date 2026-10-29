# Grading Program

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 91 and student_scores[key] < 101:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 81 and student_scores[key] < 91:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 71 and student_scores[key] < 81:
        student_grades[key] = "Acceptable"
    elif student_scores[key] < 71:
        student_grades[key] = "Fail"

print(student_grades)



# Nested List and dictionaries

travel_log = {
     "Germany": {
          "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
          "total_visits" : 5
     },
}
# Get Stuttgart

print(travel_log["Germany"]["cities_visited"][2])

for key in travel_log:
    print(key)