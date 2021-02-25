
def oldestStudent(students):
    max=students[0]["age"]
    for student in students:
        if student["age"]>max:
            max=student["age"]
    for student in students:
        if max==student["age"]:
            print(f'Ən yaşlı tələbə {student["name"]}-dir və onun {student["age"]} yaşı var')
telebeler = [
    {
        "name":"Mehemmed",
        "age":19
    },
    {
        "name":"Eliyar",
        "age":25
    },
    {
        "name":"Aynur",
        "age":29
    }   
    
]
oldestStudent(telebeler)