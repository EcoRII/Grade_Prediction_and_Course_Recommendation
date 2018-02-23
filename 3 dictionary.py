import time
import pickle


def generate_vector():
    '''
    generate a wifi position vector
    '''
    with open("data_all_spring.csv", "r") as f:
        f.readline()
        line = f.readline()
        while line is not None and line != "":
            arr = line.split(",")
            position_time = arr[3][:-6] + ":00:00"
            timeArray = time.strptime(position_time, "%Y-%m-%d %H:%M:%S")
            position_time = int(time.mktime(timeArray))
            if  1492358400< position_time < 1492531200:
                position_a = arr[8]  # building
                student_id = arr[6]
                try:
                    assert(student_id in student_list)
                    student_dict[student_id][position_a] += 1
                except AssertionError:
                    pass
            line = f.readline()
        pickle.dump(student_dict, open('student_dict.pkl', 'wb'))

def note_grade(filename):
    with open(filename,'r') as f:
        l=f.readline()
        l=f.readline()
        while l!='':
            l=l[1:-2].split('","')
            student_id=l[0]
            course_id=l[3]+l[4]
            grade=gpa_dict[l[6]]
            if student_dict.get(student_id) is not None:
                student_dict[student_id].update({course_id:grade})
            l=f.readline()

student_dict = dict()
position_list = pickle.load(open('position_list.pkl','br'))
student_list = pickle.load(open('student_list.pkl','br'))
for student in student_list:
    student_dict[student] = {}
    for position in position_list:
        student_dict[student].update({position: 0})
pickle.dump(student_dict, open('student_dict.pkl', 'wb'))

student_dict = pickle.load(open('student_dict.pkl', 'br'))
generate_vector()

pickle.dump(student_dict, open('student_dict.pkl','wb'))

course_list=[]
with open('courselist.txt','r') as f:
    l=f.readline()
    while l != '':
        l=l[:-1].split('\t')
        course_id=l[1]
        course_list.append(course_id)
        l=f.readline()

for student in student_dict.keys():       
    for course in course_list:
        student_dict[student].update({course:-1})
    
pickle.dump(student_dict, open('student_dict.pkl', 'wb'))

gpa_dict={'A':4,'A-':3.7,'B+':3.3,'B':3,'B-':2.7,'C+':2.3,'C':2,'C-':1.7,'D+':1.3,'D':1,'F':0,'':0,'P':0}


note_grade('grade1703_random0.35.csv')
note_grade('CUSZ_GRD1620_random0.35.csv')
pickle.dump(student_dict, open('student_dict.pkl', 'wb'))

for k in student_dict.keys():
    print(student_dict[k])
    break
