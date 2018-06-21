def decode(string):
    if string == '': return ''
    elif string.isalpha(): return string
    else : 
        if string[0].isdigit() and not string[1].isdigit(): 
            print(int(string[0]) * string[1])
            return int(string[0]) * string[1] + decode(string[2:])
        elif string[0].isdigit() and string[1].isdigit():
            print(string[3:])
            return int(string[0]+ string[1]) * string[2] + decode(string[3:])
        elif not string[0].isdigit():
            return string[0] + decode(string[1:])

def encode(string):
    if string == '': return ''
    return try_encode_it(string, string[0], 0)


def try_encode_it(string, current_letter, current_counter):
    
    if string == ''  and current_counter == 1: return current_letter 
    elif string == '' and current_counter > 1:
        return str(current_counter) + current_letter

    elif string[0] == current_letter:
        return try_encode_it(string[1:], current_letter, current_counter+1 )
    else :
        new_string = string[1:]
        if current_counter == 1:
            return current_letter + try_encode_it(new_string, string[0], 1)
        else: 
            return str(current_counter) + current_letter + try_encode_it(new_string,
                    string[0], 1)
