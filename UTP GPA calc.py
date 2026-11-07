def get_grade_point(score):
  """Converts a numerical score into a letter grade and grade point

  based on the institutional grading scale.
  """
  if score >= 85.0:
    return "A", 4.0
  elif score >= 80.0:
    return "A-", 3.75
  elif score >= 75.0:
    return "B+", 3.5
  elif score >= 65.0:
    return "B", 3.0
  elif score >= 55.0:
    return "C+", 2.5
  elif score >= 50.0:
    return "C", 2.0
  elif score >= 45.0:
    return "D+", 1.5
  elif score >= 40.0:
    return "D", 1.0
  else:
    return "F", 0.0


def calculate_gpa():

  subjects = {
      "Thinking Skills": 4,
      "Technical English": 3,
      "Islamic Studies": 3,
      "Programming": 5,
      "CoQ": 1,
  }

  total_quality_points = 0
  total_credits = sum(subjects.values())

  print("========================================")
  print("         SEMESTER GPA CALCULATOR        ")
  print("========================================")
  print("Please enter your marks (0.0 to 100.0) for each subject:\n")

  for subject, credits in subjects.items():
    while True:
      try:
        score = float(input(f"Enter score for {subject} (CR: {credits}): "))
        if 0.0 <= score <= 100.0:
          break
        print("Error: Score must be between 0.0 and 100.0.")
      except ValueError:
        print("Invalid input. Please enter a numeric value.")

    grade, point = get_grade_point(score)
    total_quality_points += point * credits
    print(f"   -> Result: Grade {grade} | Point: {point}\n")


  gpa = total_quality_points / total_credits

  print("========================================")
  print(f" Total Credit Hours Registered: {total_credits}")
  print(f" Final GPA: {gpa:.2f}")
  print("========================================")

if __name__ == "__main__":
  calculate_gpa()