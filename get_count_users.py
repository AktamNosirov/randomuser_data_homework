from webbrowser import get
import get_data


def get_count_users(data:dict) -> int:
    res_list=data['results']
    count=0
    for i in res_list:
        count+=1
    
    
        """You are given dictionary. Find the number of users.
    Args:
        data(dict): data
    Returns:
        int: number of users"""
    return count


import json
dat=open("randomuser_data.json").read()
data=json.loads(dat)   
print(get_count_users(data))


