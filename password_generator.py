import random 

def generate():
    result = ''

    for i in range(11):
        result += ch[random.randint(0, len(ch)-1)]

    if result.lower() == result:
        result += ch[26 + random.randint(0, 25)]

    if result.upper() == result:
        result += ch[0 + random.randint(0, 25)]

    if not(set(result) & set(ch[52:62])):
        result += ch[52 + random.randint(0, 9)]

    if not(set(result) & set(ch[62:])):
        result += ch[62 + random.randint(0, 31)]

    for i in range(len(result), 14):
        result += ch[random.randint(0, len(ch)-1)]

    return result


ch = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
      'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
      's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 
      'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
      'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
      'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', 
      '3', '4', '5', '6', '7', '8', '9', '0', '!', 
      '"', '#', '$', '%', '&', "'", '(', ')', '*', 
      '+', ',', '-', '.', '/', ':', ';', '<', '=', 
      '>', '?', '@', '[', '\\', ']', '^', '_', '`', 
      '{', '|', '}', '~']  

print(generate())