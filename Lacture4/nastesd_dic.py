student = {
    "name" : "Md Hashim Raza",
    "subject" : {
        "Chemistry" : 80,
        "physics" : 75,
        "Biology" : 90,
        "mathematics" : 95,
    }
}

# nasted dictionary
print(student["subject"]["physics"])
print(student.keys())
print(list(student.keys()))
print(len(list(student.keys())))
print(len(list(student.values())))
print(student.values())
print(list(student.values()))
