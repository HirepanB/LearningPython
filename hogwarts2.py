students={
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron":"Gryffindor",
    "Draco": "Slytherin",
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

for student in students:
    print(student)



print("----------\n")

students2 = [
    {"name": "Hermion", "house":"Gryffindor","patronus":"Otter"},
    {"name": "Harry", "house":"Gryffindor","patronus":"Stag"},
    {"name": "Ron","house":"Gryffindor","patronus":"Jack Rusell Terrier"},
    {"name": "Draco", "house": "Slytherin","patronus":None}
]

for student in students2:
    print(student["name"], student["house"], student["patronus"],sep=", ")

