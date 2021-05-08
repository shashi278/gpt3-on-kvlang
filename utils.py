base = 4

def format_kv(text):
    new_x= ""

    xl = text.split("\n")
    for i, each in enumerate(xl):
        if each:
            if i==len(xl)-2:
                new_x+= int(each[0])*4*' '+each[2:]
            else:
                new_x+= int(each[0])*4*' '+each[2:]+"\n"

    return new_x

def fix_indent(x):
    xl = [each for each in x.splitlines() if each]

    new_l = [xl[0]]

    for each in xl[1:]:
        l_spaces = len(each) - len(each.lstrip(' '))
        rounded_spaces = base * round(l_spaces/base)
        new_each = ' '*rounded_spaces+each.lstrip(' ')
        new_l.append(new_each)

    res = '\n'.join(new_l)
    return res