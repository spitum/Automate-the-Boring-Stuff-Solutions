# Write a function that uses regular expressions to make sure the password string it is passed is strong.
# A strong password is defined as one that is at least eight characters long, 
# contains both uppercase and lowercase characters, and has at least one digit. 
# You may need to test the string against multiple regex patterns to validate its strength.

import re
import getpass

passRegexCap = re.compile(r'[A-Z]+')
passRegexNum = re.compile(r'[0-9]+')


def pass_strength(str):
    '''checks length is at least 8, and there is at least 1 number and 1 uppercase letter'''
    count_Cap = 0
    count_Num = 0
    if len(str) < 8:
        return False
    for Cap in passRegexCap.finditer(str):
        count_Cap += 1
        if count_Cap == 0:
            return False
    for Num in passRegexCap.finditer(str):
        count_Num += 1
        if count_Num == 0:
            return False
    return True

if __name__ == '__main__':
    password = getpass.getpass()
    if pass_strength(password):
        print('Nice password!')
    else:
        print("Please use a stronger password. The password should contain at least 1 number and 1 uppercase letter.")

#TODO add lowercase and special characters