def avg(students,n):
    ls=[]
    avg=0
    for name, marks in students:
        average_marks = sum(marks) / len(marks)
        ls.append(average_marks)
        
        print(f"{name}'s average marks: {average_marks:.2f}")
        
        if average_marks>avg:
            top=name
            avg=average_marks
    print(ls)
    count = 0
    for i in ls:
        if i>50:
            count+=1
    print("total students passed:",count)
    print(f"{top}is highest avg grade: {avg:.2f}")
    for student_name, marks in students:
        if student_name == n:
            specific_avg = sum(marks) / len(marks)
            print(f"{n}'s average marks: {specific_avg:.2f}")
            break
    
    
        
students = [
    ("Alice", [85, 90, 78, 92]),
    ("Bob", [60, 65, 70, 75]),
    ("Charlie", [40, 45, 50, 55]),
    ("David", [95, 100, 98, 92])
]
n=input()
print(avg(students,n)) 