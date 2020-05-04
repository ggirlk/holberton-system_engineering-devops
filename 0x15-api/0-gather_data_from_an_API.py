#!/usr/bin/python3
""" Gather data from an API """
import requests
import sys



p = {"userId" : sys.argv[1]}
p2 = {"id" : sys.argv[1]}
r = requests.get('https://jsonplaceholder.typicode.com/todos', params=p).json()
done = 0
for i in r:
    if i['completed'] == True:
        done += 1
user = requests.get('https://jsonplaceholder.typicode.com/users', params=p2).json()[0]
print("Employee {} is done with tasks({}/{}):"
      .format(user['name'], done, len(r)))
for i in r:
    if i['completed'] == True:
        print('\t{}'.format(i['title']))
