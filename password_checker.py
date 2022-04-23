

def check(password):
    result = []

    digits = ['1', '2', '3', '4', '5', '6', '7',
              '8', '9', '0']
    punct= ['!', '"', '#', '$', '%', '&', "'",
            '(', ')', '*', '+', ',', '-', '.', 
            '/', ':', ';', '<', '=', '>', '?', 
            '@', '[', '\\', ']', '^', '_', '`', 
            '{', '|', '}', '~']

    # check if password contains both lowercase and uppercase characters
    if password.upper() == password or password.lower() == password:
        result.append('- Password must contain both lowercase and uppercase characters')

    # check if password contains digits
    if not(set(password) & set(digits)):
        result.append('- Password must contain digits')
    
    # check if password contains punctuation marks
    if not(set(password) & set(punct)):
        result.append('- Password must contain at least one punctuational character (!\"#$%&\'()*+, -./:;<=>?@[\\]^_`{|}~)')

    # check if password is at least 14 characters long
    if len(password) < 14:
        result.append('- Password must be at least 14 characters long')

    if result: # if there are weaknesses added to result - password is weak
        result.insert(0, 'Weak password:')
    else:
        result.append('Strong password')

    return result


password_to_check = input()

result_of_checking = check(password_to_check)

for string in result_of_checking:
    print(string)