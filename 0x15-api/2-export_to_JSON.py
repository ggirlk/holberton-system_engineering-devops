#!/usr/bin/python3
""" Export to JSON """
import requests
import sys
import json



if __name__ == '__main__':
    p = {"userId" : sys.argv[1]}
    p2 = {"id" : sys.argv[1]}
    r = requests.get('https://jsonplaceholder.typicode.com/todos', params=p).json()
    user = requests.get('https://jsonplaceholder.typicode.com/users', params=p2).json()[0]
    jdata = {}
    jdata[user['id']] = []
    for i in r:
        jdata[user['id']].append({
             "task": i["title"],
             "completed": i["completed"],
             "username": user["name"]
        })
    with open(sys.argv[1]+'.json', 'a+') as f:
        json.dump(jdata, f)
