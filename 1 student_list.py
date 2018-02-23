import pickle

student_list=[]
def generate_list(filename):
    with open(filename, "r") as f:
        f.readline()
        line = f.readline()
        while line != "":
            arr = line.split(",")
            student_id = arr[0][1:-1]
            if student_id not in student_list:
                student_list.append(student_id)
            else:
                pass
            line = f.readline()
student_list.sort()
generate_list('CUSZ_GRD1620_random0.35.csv')
generate_list('grade1703_random0.35.csv')

pickle.dump(student_list, open('student_list.pkl', 'wb'))
