from Student import Student
import matplotlib.pyplot as plt

def main():
    studentList=[]
    studentList.append(Student(50123456,'lam tai man',710,60.0))
    studentList.append(Student(50223456,'li tai man',60.0,90.5))
    studentList.append(Student(50323456,'wong tai man',34.5,30.0))
    studentList.append(Student(50423456,'ng tai man',90.5,70.0))
    studentList.append(Student(50523456,'lau tai man',86.0,92.4))
    studentList.append(Student(50623456,'chui tai man',70.0,64.5))
    studentList.append(Student(50723456,'lim tai man',64.5,60.0))
    studentList.append(Student(50823456,'pok tai man',37.5,35.50))
    studentList.append(Student(50923456,'kim tai man',92.4,60.0))
    studentList.append(Student(50023456,'tsang tai man',15.0,20.0))
    studentList.append(Student(50999999,'chan peter',100.00,80.00))

    gradeFeq={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0}
    
    for e in studentList:
        mark=e.overall()
        if mark > 75:
            gradeFeq['A'] += 1
        elif mark > 65 and mark < 75:
                gradeFeq['B'] += 1
        elif mark > 50 and mark < 65:
                gradeFeq['C'] += 1
        elif mark > 40 and mark < 50:
                gradeFeq['D'] += 1
        else:
            gradeFeq['F'] += 1            
             
    fig = plt.figure(figsize=(8,6))    # width x height in inches
    ax1 = fig.add_subplot(111)          # 1 row 1 columns, column 1
    ax1.bar(['A','B','C','D','F'],
            [gradeFeq['A'],gradeFeq['B'],gradeFeq['C'],
             gradeFeq['D'],gradeFeq['F']])            # vertical bar charts
    plt.show()
    
    for e in studentList:
        print(e,e.overall())
        
if __name__ == "__main__":
    main()   