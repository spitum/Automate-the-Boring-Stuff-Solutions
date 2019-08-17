# Create a Mad Libs program that reads in text files and lets the user add their own text 
# anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For example, a text file may look like this:

# The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
# unaffected by these events.
# The program would find these occurrences and prompt the user to replace them.


# Enter an adjective:
# silly
# Enter a noun:
# chandelier
# Enter a verb:
# screamed
# Enter a noun:
# pickup truck
# The following text file would then be created:


# The silly panda walked to the chandelier and then screamed. A nearby pickup
# truck was unaffected by these events.
# The results should be printed to the screen and saved to a new text file.


madlibs = 'madlibs.txt'

with open(madlibs,'r') as f:
    contents = f.read()
    print(contents)

def input_words(adj,verb,noun):
    words = {'adj': '', 'verb': '', 'noun': ''}
    if adj != None:
        words['adj'] = adj
    if verb != None:
        words['verb'] = verb
    if noun != None:
        words['noun'] = noun
    with open('madlibs_%s.txt' % (words['noun']),'w') as f:
        f.write(f'The %s panda walked to the %s and then %s. A nearby %s was unaffected by these events.' % (words['adj'], words['noun'],words['verb'], words['noun']))
    print(f'The %s panda walked to the %s and then %s. A nearby %s was unaffected by these events.' % (words['adj'], words['noun'],words['verb'], words['noun']) )

#print(input_words())

if __name__ == '__main__':
    adj = input('Please enter adjective: ')
    verb = input('Please enter verb: ')
    noun = input('Please enter noun: ')
    input_words(adj,verb,noun)











