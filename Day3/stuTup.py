def stuDetail():
    students=[
        (1,"Ravi",82),
        (2,"Anita",67),
        (3,"Kiran",91),
        (4,"Meena",76),
        (5,"Arjun",59)
    ]
    highest_marks=0
    topper_name=""
    for student in students:
        rollno,name,marks=student
        if marks>highest_marks:
            highest_marks=marks
            topper_name=name
    print("Topper:",topper_name,"with marks",highest_marks)
    print("\nStudents more than 75 marks:")
    for student in students:
        rollno,name,marks=student
        if marks>75:
            print(name,"(Roll No:",rollno,", Marks:",marks,")")
stuDetail()
