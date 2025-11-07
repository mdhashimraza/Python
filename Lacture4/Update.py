student = {
    "name" : "Md Hashim Raza",
    "subject" : {
        "Chemistry" : 80,
        "physics" : 75,
        "Biology" : 90,
        "mathematics" : 95,
    }
}
new_dic = {"city" : "katihar" , "age" : 22, "name" : "Fahim"}
student.update(new_dic)
print(student)