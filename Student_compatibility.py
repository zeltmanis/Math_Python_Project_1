import csv

# Open and read the CSV file
with open('students.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    students = []

    for row in reader:
        students.append(row)

# Print the loaded student data
for student in students:
    print(student)