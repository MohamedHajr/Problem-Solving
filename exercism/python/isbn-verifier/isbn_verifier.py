import re

def verify(isbn):
    strippedIsbn = isbn.replace('-', '')
    if not re.compile("[0-9]{9}([0-9]|X)$").match(strippedIsbn):
        return False
    return isIsbn(strippedIsbn, 0, 10)    


def isIsbn(isbn, result, calculationStepValue):
    if len(isbn) == 0 : return (result % 11) == 0
    element = int(isbn[0]) if isbn[0] != 'X' else 10
    newResult = element * calculationStepValue + result
    return isIsbn(isbn[1:], newResult, calculationStepValue - 1)