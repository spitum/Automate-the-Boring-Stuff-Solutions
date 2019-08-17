#Write a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression. The results should be printed to the screen.

import glob
import os
import re

path = os.getcwd()
fileList = glob.glob("*.txt")

# below section is from: https://stackoverflow.com/questions/51691270/python-user-input-as-regular-expression-how-to-do-it-correctly
# helps validate regex input before checking files
user_input = input("Input regex:")  # check console, it is expecting your input
regex_string = r"%s" % user_input
string_to_search = re.compile(regex_string)
print("User typed: '{}'. Input type: {}.Regex: {}".format(user_input, type(user_input), string_to_search))


for file in fileList:
    with open(file,'r') as file_object:
        contents = file_object.readlines() 
        #print(contents)
        for line in contents:
                word_search = string_to_search.finditer(line)
                for word in word_search:
                        print(file_object,word)

