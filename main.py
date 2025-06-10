import streamlit as STL

subjectname,grade,credit = [] , [] , []

STL.title ("GPA Calculator")

numberofSubject = STL.number_input("Number of Subject : ",min_value=1,step=1,value=7)

for i in range(numberofSubject):
    STL.markdown(f"##### Subject #{str(i+1)}")

    subjectName = STL.text_input("Subject Name : ",key=f"subjectname {i}")
    Grade = STL.selectbox(f"Grade for {subjectName} : ",["A(4.00)","B+(3.50)","B(3.00)","C+(2.50)","C(2.00)","D+(1.50)","D(1.00)","F(0.00)"],key=f"grade {i}")
    Credit = STL.number_input(f"Credit for {subjectName} : ",min_value=1.0,step=0.5,value=3.0 ,key=f"credit {i}")

    subjectname.append(subjectName)
    grade.append(Grade)
    credit.append(Credit)

gradeMap = {
    "A(4.00)" : 4.00 ,
    "B+(3.50)" : 3.50 ,
    "B(3.00)" : 3.00 ,
    "C+(2.50)" : 2.50 ,
    "C(2.00)" : 2.00 ,
    "D+(1.50)" : 1.50 ,
    "D(1.00)" : 1.00 ,
    "F(0.00)" : 0.00
}

if STL.button("GPA Calculate"):
    totalcredit = sum(credit)
    totalpoints = sum(gradeMap[Grade] * Credit  for Grade,Credit in zip(grade, credit))
    gpa = totalpoints / totalcredit

    STL.success(f"GPA: {gpa:.2f}")