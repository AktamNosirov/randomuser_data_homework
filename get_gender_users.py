import get_data

def get_gender_users(data:dict) -> list:
    """
    Take the gender of the users and return the list.
     The list items are as follows:
        If the user is male: {"Male":1}
        If the user is female: {"Female":0}
    Args:
        data(dict): data
    Returns:
        list: users get gender list
    """
    a=[]
    b={"Male":0 ,"Female":0 }
    data=data['results']
    for i in data :       
        a.append(i["gender"])
   
    b["Male"]=a.count("male")
    b["Female"]=a.count("female")
   
    return  b
import json
dat=open("randomuser_data.json").read()
data=json.loads(dat)   
print(get_gender_users(data))





