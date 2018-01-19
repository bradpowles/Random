data = {'Monday': [],'Tuesday': [], 'Wednesday':[],'Thursday':[],'Friday':[],'Saturday':[],'Sunday':[]}
for i in data:
    data[i].append({})
data['Monday'][-1]['Lat'] = 123456789
print(data['Monday'])
import datetime
now = datetime.datetime.now()
day = now.strftime("%A")
print(data[day])
