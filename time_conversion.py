# Convert and print the given time in 24-hour format, where 00<=hh<=23
# Sample Input 07:05:45PM
# Sample Output 19:05:45

import datetime

def convert_time(time):
    new_time = datetime.datetime.strptime(time, '%I:%M:%S%p')
    print datetime.datetime.strftime(new_time, '%H:%M:%S')


def main():
    convert_time("07:05:45PM")

if __name__ == '__main__':
    main()
    