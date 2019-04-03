from Student import Student
import matplotlib.pyplot as plt
import sys

studentDL = []

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
def readFile(argv):
        try:
            fileIn = open(argv[1], 'r')

            line = fileIn.readline()
            
            while line != '':
                studentRec=line.split('_')
                if len(studentRec) < 4:
                    sys.stderr.write('Invalid data line : '+line+'\n')
                else:
                    studentDL.append(Student(int(studentRec[0]),studentRec[1],
                                                      float(studentRec[2]),float(studentRec[3])))
                    
                line = fileIn.readline()
        
            if Student.numStudent == 0:
                sys.stderr.write('empty or invalid data only : '+line+'\n')
                
            fileIn.close()
            
        except FileNotFoundError as error:
            sys.stderr.write(str(error)+'\n') 
               
if __name__ == "__main__":
    readFile(sys.argv)
    for e in studentDL:
        print(e)
