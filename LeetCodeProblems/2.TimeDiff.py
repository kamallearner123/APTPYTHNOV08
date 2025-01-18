
#!/bin/python3

import math
import os
import random
import re
import sys

'''
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
'''

months = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12
}

def get_time(t):
    date = int(t[1])
    month = months[t[2]]
    year = int(t[3])
    hours = int(t[4])
    minutes = int(t[5])
    seconds = int(t[6])

    time_diff_in_seconds = int(t[8])*60*60+int(t[9])*60
    if t[7] == '-':
        time_diff_in_seconds *= -1
    
    curr_time_in_seconds = hours*60*60+minutes*60+seconds
    time_diff_in_seconds = curr_time_in_seconds + time_diff_in_seconds

    if time_diff_in_seconds < 0:
        time_diff_in_seconds = 24*60*60 + time_diff_in_seconds # 3600*24 = 86400
        date -= 1
        if date == 0:
            month -= 1
            if month == 0:
                year -= 1
                month = 12
            
            if month in [1, 3, 5, 7, 8, 10, 12]:
                date = 31
            elif month in [4, 6, 9, 11]:
                date = 30
            else: # for febrauary
                if year % 4 == 0:
                    date = 29
                else:
                    date = 28

    hours = time_diff_in_seconds // 3600
    minutes = (time_diff_in_seconds % 3600) // 60
    seconds = time_diff_in_seconds % 60
    print(date, month, year, hours, minutes, seconds)
    return (date, month, year, hours, minutes, seconds)


# Complete the time_delta function below.
def time_delta(t1, t2):
    time1 = re.findall(r"(\w{3}) (\d{2}) (\w{3}) (\d{4}) (\d{2}):(\d{2}):(\d{2}) ([-+]+)(\d{2})(\d{2})", t1)
    time2 = re.findall(r"(\w{3}) (\d{2}) (\w{3}) (\d{4}) (\d{2}):(\d{2}):(\d{2}) ([-+]+)(\d{2})(\d{2})", t2)
    print(time1, time2)

    t1 = get_time(time1[0])
    t2 = get_time(time2[0])
    total_seconds = 0
    total_seconds += abs(t1[0]-t2[0])*24*60*60
    total_seconds += abs(t1[1]-t2[1])*60*60
    total_seconds += abs(t1[2]-t2[2])*60
    total_seconds += abs(t1[3]-t2[3])

    print(total_seconds)

    # from datetime import datetime as dt
    # fmt = '%a %d %b %Y %H:%M:%S %z'
    # t1 = dt.strptime(t1, fmt)
    # t2 = dt.strptime(t2, fmt)
    # return str(int(abs((t1-t2).total_seconds())))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input())

    # for t_itr in range(t):
    #     t1 = input()
    #     t2 = input()

    delta = time_delta("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000")
    print(delta)
    #     fptr.write(delta + '\n')

    # fptr.close()
