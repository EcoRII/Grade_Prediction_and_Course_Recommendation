import pickle
import numpy as np

student_list = pickle.load(open('student_list.pkl','br'))
course_list = pickle.load(open('course_list.pkl','br'))
student_dict = pickle.load(open('student_dict.pkl','br'))

n_course = len(course_list)
attribute_list= []
for k in student_dict.keys():
    for a in student_dict[k]:
        attribute_list.append(a)
    break
for student in student_list:
    total_grade = 0
    n_grade = 0
    for course in course_list:
        temp_grade = student_dict[student][course]
        if temp_grade != -1:
            total_grade += temp_grade
            n_grade += 1
    average_grade = total_grade/n_grade
    student_dict[student]['ave']=[]
    for course in course_list:
        temp_grade = student_dict[student][course]
        if temp_grade == -1:
            student_dict[student][course] = average_grade
            student_dict[student]['ave'].append(attribute_list.index(course))
    student_dict[student]['ave'].append(average_grade)

pickle.dump(student_dict,open('ave_student_dict.pkl','wb'))

X_train = []
y_train = []
for student in student_dict.keys():
    x_input = []
    for idx in range(len(attribute_list)):
        x_input.append(student_dict[student][attribute_list[idx]])
    for ave in range(len(student_dict[student]['ave'])-1):
        temp_x = x_input
        y_train.append(temp_x[15:])
        temp_x[student_dict[student]['ave'][ave]] = student_dict[student]['ave'][-1]
        X_train.append(temp_x)
        
X_train = np.array(X_train)
X_train = X_train.astype(np.float64)
y_train = np.array(y_train)
y_train = y_train.astype(np.float64)       

pickle.dump(X_train,open('X_total.pkl','wb'))
pickle.dump(y_train,open('y_total.pkl','wb'))
