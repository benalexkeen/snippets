# Arizona license plates take the form TCZ2341. That is, three characters followed by four digits. 
# The first license plate issued was AAA0000 and the last one will be ZZZ9999. Given a license 
# plate, return the remaining number of license plates that can be issued after the given license plate.

import re

def remaining_plates(plate):
    assert re.match(r'[A-Z]{3}\d{4}', plate)
    plates_left = 9999 - int(plate[3:])
    for i in range(2):
        power = 2 - i
        char_number = ord(plate[i]) - 64
        chars_left = 26 - char_number
        plates_left += chars_left * 26 ** power * 1000
    return plates_left

def main():
    test_cases = ['AAA0000', 'ZZZ9999', 'TCZ2341']
    for test in test_cases:
        print remaining_plates(test)

if __name__ == '__main__':
    main()
