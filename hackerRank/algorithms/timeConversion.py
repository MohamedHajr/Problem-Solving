def timeConversion(s):
    #
    # Write your code here.
    new = s[:8]
    if s[8:] == 'AM':
        if new[:2] == '12':
            return  '00' + new[2:]
        return new
    
    else:
        hours = str(int( + 12))
        if hours == 24:
            hours = 0
        return  hours + new[2:]
    
result = timeConversion('12:45:54PM')
print(result)