# This script calculates the average grade for a student in three subjects.
# Javier Romero

student_name = input("Enter your name: ")


try:
  math_score = float(input("Enter your Math score: "))
  science_score = float(input("Enter your Science score: "))
  english_score = float(input("Enter your English score: "))
except ValueError:
  print("Error: Please enter valid numbers for the scores.")
  exit()


average_grade = (math_score + science_score + english_score) / 3

print(f"{student_name}, your average grade is: {average_grade:.2f}")
