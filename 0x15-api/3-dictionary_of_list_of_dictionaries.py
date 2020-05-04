#!/usr/bin/python3
""" Export to JSON """
import requests
import json



if __name__ == '__main__':
    user = requests.get('https://jsonplaceholder.typicode.com/users').json()
    data = {}
    for u in user:
        p = {"userId" : u['id']}
        r = requests.get('https://jsonplaceholder.typicode.com/todos', params=p).json()
        jdata = []
        for i in r:
            jdata.append({
                 "username": u["name"],
                 "task": i["title"],
                 "completed": i["completed"]
            })
        data[u['id']] = jdata
    #print(json.dumps(data, indent=4))
    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f)
