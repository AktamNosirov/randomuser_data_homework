from webbrowser import get
import get_data


def get_count_users(data:dict) :
    res_list=data['results']
    count=0
    for i in res_list:
        count+=1
    return count


import json
dat=open("randomuser_data.json").read()
data=json.loads(dat)   
print(get_count_users(data))