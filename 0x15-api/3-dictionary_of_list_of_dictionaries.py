#!/usr/bin/python3
""" Export to JSON """
import requests
import sys
import json



if __name__ == '__main__':
    user = requests.get('https://jsonplaceholder.typicode.com/users').json()
    jdata = {}
    for u in user:
        p = {"userId" : u['id']}
        r = requests.get('https://jsonplaceholder.typicode.com/todos', params=p).json()
        jdata[u['id']] = []
        for i in r:
            jdata[u['id']].append({
                 "username": u["name"],
                 "task": i["title"],
                 "completed": i["completed"]
            })
    with open('todo_all_employees.json', 'a+') as f:
        json.dump(jdata, f)
