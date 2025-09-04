def studentMark(marks):
    if (marks>=40):
        print("Pass")
        if(marks<50):
            print("C grade")
        elif (marks>51 and marks<70):
            print("B grade")
        elif (marks>71 and marks<80):
            print("A grade")
        else:
            print("Distension")
    else:
        print("Fail")
x=int(input("Enter the student marks:"))
studentMark(x)