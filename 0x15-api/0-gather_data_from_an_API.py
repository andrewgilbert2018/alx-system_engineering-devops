#!/usr/bin/python3
"""
This scripts reads an API and stores the data
"""
import requests
import sys


def main():
    """
    Python script to read information from a public API
    returns employess an their completed tasks
    """
    number = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(number)
    url_tasks = ("https://jsonplaceholder.typicode.com/users/{}/todos".
                 format(number))
    response = requests.get(url_tasks)
    tasks = response.json()
    user_info = requests.get(url_user).json()
    employee_name = user_info["name"]
    list_of_done_tasks = [x for x in tasks if x['completed']]
    number_of_done_tasks = len(list_of_done_tasks)
    total_task_number = len(tasks)
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          number_of_done_tasks,
                                                          total_task_number))
    for task in list_of_done_tasks:
        print("\t {}".format(task["title"]))


if __name__ == '__main__':
    main()
