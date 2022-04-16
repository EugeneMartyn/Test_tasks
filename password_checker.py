
def check(p):
    result = []
    x = True

    if p.upper() == p or p.lower() == p:
        x = False
        if not('Weak password:' in result):
            result.append('Weak password:')

        result.append('- Password must contain both lowercase and uppercase characters')

    if not(set(p) & set(d)):
        x = False
        if not('Weak password:' in result):
            result.append('Weak password:')

        result.append('- Password must contain digits')
    
    if not(set(p) & set(punct)):
        x = False
        if not('Weak password:' in result):
            result.append('Weak password:')
        
        result.append('- Password must contain at least one punctuational character (!\"#$%&\'()*+, -./:;<=>?@[\\]^_`{|}~)')

    if len(p) < 14:
        x = False
        if not('Weak password:' in result):
            result.append('Weak password:')
        result.append('- Password must be at least 14 characters long')

    if x:
        result.append('Strong password')

    return result


password = input()
d = ['1', '2', '3', '4', '5', '6', '7',
          '7', '9', '0']
punct = ['!', '"', '#', '$', '%', '&', "'",
         '(', ')', '*', '+', ',', '-', '.', 
         '/', ':', ';', '<', '=', '>', '?', 
         '@', '[', '\\', ']', '^', '_', '`', 
         '{', '|', '}', '~']

r = check(password)
for i in range(len(r)):
    print(r[i])