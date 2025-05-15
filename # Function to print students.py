# Function to print students
def print_students(my_students):
    print('Class list:')
    i = 1
    for student in my_students:
        print(i, '-', student)
        i += 1

# Current list of students
my_students = ['Anderson', 'Holmes', 'Johnson', 'Smith', 'Watson']
print_students(my_students)

# Adding a new student
student = input("Enter the student's last name: ")
my_students.append(student)
my_students.sort()

# Print updated list
print_students(my_students)

