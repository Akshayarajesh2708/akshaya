# Simple Student Details Table Program

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details of Student {i+1}")

    name = input("Name: ")
    roll_no = input("Roll Number: ")
    admission_no = input("Admission Number: ")
    father_name = input("Father Name: ")
    mother_name = input("Mother Name: ")
    phone = input("Phone Number: ")
    place = input("Place: ")
    address = input("Address: ")

    students.append([
        name,
        roll_no,
        admission_no,
        father_name,
        mother_name,
        phone,
        place,
        address
    ])

print("\n" + "=" * 120)
print("{:<15} {:<12} {:<15} {:<15} {:<15} {:<15} {:<12} {:<20}".format(
    "Name",
    "Roll No",
    "Admission No",
    "Father Name",
    "Mother Name",
    "Phone",
    "Place",
    "Address"
))
print("=" * 120)

for student in students:
    print("{:<15} {:<12} {:<15} {:<15} {:<15} {:<15} {:<12} {:<20}".format(
        student[0],
        student[1],
        student[2],
        student[3],
        student[4],
        student[5],
        student[6],
        student[7]
    ))

print("=" * 120)