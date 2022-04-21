import get_data
from pprint import pprint
def get_users_data(data:dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.
    
    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}

    Args:
        data(dict): data
    Returns:
        list: users data list
    """
   
    foydalanuvchilar_haqida_malumotlar=[]
   
    foydalanuvchilar=data['results']
    for user in foydalanuvchilar :
        ismlar=user["name"]["first"]
        familiyalar=user["name"]["last"]
        telefonlar=user["phone"]
        malumotlar={"first_name" :ismlar,"last_name" :familiyalar , "phone_number" :telefonlar  }
        foydalanuvchilar_haqida_malumotlar.append(malumotlar)
    return foydalanuvchilar_haqida_malumotlar

import json
dat=open("randomuser_data.json").read()
data=json.loads(dat)   
pprint(get_users_data(data))