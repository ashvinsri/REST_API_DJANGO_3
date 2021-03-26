import requests
import json

URL='http://127.0.0.1:8000/stu_create/'

def get_data(id=None):
    data={}

    if id is not None:
        data={'id':id}
    header={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.get(url=URL,headers=header,data=json_data)
    data=r.json()
    print(data)

# get_data(204)

def post_data():
    data={
        'clas':205,
        'name':'Sajan',
        'city':'Hyderabad'
        }
    header={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.post(url=URL,headers=header,data=json_data)
    data=r.json()
    print(data)

# post_data()

def update_data():
    data={
        'clas':205,
        'name':'Sajan',
        'city':'Chennai'
    }
    header={'content-Type':'application/json'}
    json_data=json.dumps(data)
    res=requests.put(url=URL,headers=header,data=json_data)
    data=res.json()
    print(data)

# update_data()

def delete_data():
    data={'clas':205}
    header={'content-Type':'application/json'}
    json_data=json.dumps(data)
    res=requests.delete(url=URL,headers=header,data=json_data)
    data=res.json()
    print(data)

delete_data()

