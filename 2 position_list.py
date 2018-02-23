import time
import pickle

def position_list():
    with open("data_all_spring.csv") as f:
        line=f.readline()
        line=f.readline()
        while line!='':
            arr = line.split(",")
            position_time = arr[3][:-6] + ":00:00"
            timeArray = time.strptime(position_time, "%Y-%m-%d %H:%M:%S")
            position_time = int(time.mktime(timeArray))
            if position_time > 1492531200:
                break
            position = arr[8]
            if position in positionList:
                pass
            else:
                positionList.append(position)
            line=f.readline()

positionList=[]
positionList()
positionList.sort()
pickle.dump(positionList,open('position_list.pkl','wb'))
 
