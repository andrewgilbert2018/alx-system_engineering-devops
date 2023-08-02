#!/usr/bin/python3
"""
This scripts reads an API and stores the data
"""
import json
import requests
import sys


def main():
    """
    This script reads data from a public API and saves the result in a custom
    json
    """
    number = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(number)
    url_tasks = ("https://jsonplaceholder.typicode.com/users/{}/todos".
                 format(number))
    tasks = requests.get(url_tasks).json()
    user_info = requests.get(url_user).json()
    employee_name = user_info.get("username")
    user_list = []
    user_dict = {}
    for task in tasks:
        temp_dict = {}
        temp_dict['task'] = task.get('title')
        temp_dict['completed'] = task.get('completed')
        temp_dict['username'] = employee_name
        user_list.append(temp_dict)
    user_dict[number] = user_list
    with open("{}.json".format(number), "w") as file:
        json.dump(user_dict, file)

if __name__ == '__main__':
    main()
