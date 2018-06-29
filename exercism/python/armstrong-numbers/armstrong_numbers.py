def is_armstrong(number):
    string_of_number = str(number)
    power = len(string_of_number)
    return True if calculate_digits_sum(number = string_of_number, power = power) == number else  False

def calculate_digits_sum(*, number, power, result = 0):
   return result if len(number) == 0 else calculate_digits_sum(number = number[1:], power = power, result =  result + (int(number[0]) ** power))
    

