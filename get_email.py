import get_data

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args : 
        data(dict): data
    Returns : 
        list: users email
    """
    
    a=[]
    data=data['results']
    for i in data :       
        a.append(i["email"])
    
    
    
    return a

import json
dat=open("randomuser_data.json").read()
data=json.loads(dat)   
print(get_email(data))