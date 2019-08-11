
def collatz(number):
    """If number is even then print nummber//2, else print 3 * number + 1"""
    if number % 2 == 0:
        return number // 2
    else:
        return (3*number)+1


value = 0
while value != 1:
    try:
        print('please enter a number')
        user_input = int(input())
    except ValueError:
        print('please enter a valid number')
    else:
        value = collatz(user_input)
        if value == 1:
            print(f'You have solved the Collatz Sequence: {value}')
            break
        else:
            continue


