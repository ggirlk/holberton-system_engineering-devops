#!/usr/bin/python3
""" Export to CSV """
import requests
import sys



if __name__ == '__main__':
    p = {"userId" : sys.argv[1]}
    p2 = {"id" : sys.argv[1]}
    r = requests.get('https://jsonplaceholder.typicode.com/todos', params=p).json()
    user = requests.get('https://jsonplaceholder.typicode.com/users', params=p2).json()[0]
    with open(sys.argv[1]+'.csv', 'a+') as f:
        for i in r:
            f.write('"{}","{}","{}","{}"\n'
                    .format(i["userId"], user['name'], i["completed"], i["title"]))
