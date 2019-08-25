# Regex Version of strip()
# Write a function that takes a string and does the same thing as the strip() string method. 
# If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end 
# of the string. Otherwise, the characters specified in the second argument to the function will be removed from the string.

import re

def regex_strip(str,rep = None):
    '''function to strip white space from start and end of string while replacement string is None. 
    Else replace characters passed in replacement string.'''
    if len(rep) == 0:   
        new_string = re.sub(r'^\s+|\s+$', "" ,str)  #check replacement string length and remove spaces from start and end.
        return new_string
    elif len(rep) >= 1:
        #build list of characters to remove from the test string.
        c_list = '[' + re.escape(''.join(rep)) + ']' #build string of characters that will be removed.
        new_string = re.sub(c_list,"",str) 
        return new_string
    else:
        print('please enter a valid string and replacement character')

if __name__ == '__main__':
    print('Please enter your string here: ')
    str = input("     ")
    print('Please enter replacement characters here: ')
    rep = input("     ")
    print(regex_strip(str,rep))
