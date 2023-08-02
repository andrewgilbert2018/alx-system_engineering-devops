#!/usr/bin/python3
"""
This scripts reads an API and stores the data
"""
import csv
import requests
import sys


def main():
    """
    This script reads the data from the API and stores the information
    in an csv file
    """
    number = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(number)
    url_tasks = ("https://jsonplaceholder.typicode.com/users/{}/todos".
                 format(number))
    tasks = requests.get(url_tasks).json()
    user_info = requests.get(url_user).json()
    employee_name = user_info.get("username")
    with open('{}.csv'.format(number), 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([task.get('userId'), employee_name,
                             task.get('completed'), task.get('title')])


if __name__ == '__main__':
    main()
