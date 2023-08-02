#!/usr/bin/python3
"""
This scripts reads an API and stores the data
"""
import json
import requests


def main():
    """
    This script reads data from a public API and store the result in a json
    that constains information about ALL users
    """
    url_users = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url_users).json()
    user_dict = {}
    for user in users:
        employee_name = user.get("username")
        number = user.get("id")
        url_tasks = ("https://jsonplaceholder.typicode.com/users/{}/todos".
                     format(number))
        tasks = requests.get(url_tasks).json()
        user_list = []
        for task in tasks:
            temp_dict = {}
            temp_dict['username'] = employee_name
            temp_dict['task'] = task.get('title')
            temp_dict['completed'] = task.get('completed')
            user_list.append(temp_dict)
        user_dict[number] = user_list
    with open("todo_all_employees.json".format(number), "w") as file:
        json.dump(user_dict, file)


if __name__ == '__main__':
    main()
