students = {"emilly": "A", 
            "Tara": "B",
            "Sam":"C",
            "Altman":"D"}

student = input("Enter any student name: ")

if student in students:
    print(f"{student}'s grades is {students[student]}")
else:
    print(f"{student} is not found!")