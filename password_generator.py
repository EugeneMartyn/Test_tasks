import random 

def generate(passwordLength):
    result = ''
    number_of_conditions = 4

    lowerChar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
                 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

    upperChar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
                 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    punct= ['!', '"', '#', '$', '%', '&', "'",
            '(', ')', '*', '+', ',', '-', '.', 
            '/', ':', ';', '<', '=', '>', '?', 
            '@', '[', '\\', ']', '^', '_', '`', 
            '{', '|', '}', '~']

    allCharacters = lowerChar + upperChar + digits + punct 

    #fill part of the password with random characters.
    for i in range(passwordLength - number_of_conditions - 1):
        result += allCharacters[random.randint(0, len(allCharacters)-1)]

    #check if password contains uppercase characters. If not - add them
    if not(set(result) & set(upperChar)):
        result += upperChar[random.randint(0, len(upperChar)-1)]

    #check if password contains lowercase characters. If not - add them
    if not(set(result) & set(lowerChar)):
        result += lowerChar[random.randint(0, len(lowerChar)-1)]

    #check if password contains digits. If not - add them
    if not(set(result) & set(digits)):
        result += digits[random.randint(0, len(digits)-1)]

    #check if password contains punctuation marks. If not - add them
    if not(set(result) & set(punct)):
        result += punct[random.randint(0, len(punct)-1)]

    # if legnth of result < necessary length - fill the password with random characters to the end
    for i in range(len(result), passwordLength):
        result += allCharacters[random.randint(0, len(allCharacters)-1)]

    return result


length = 14
print(generate(length))