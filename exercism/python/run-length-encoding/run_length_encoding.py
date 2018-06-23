import re
from itertools import groupby

def decode(string):
    groups = re.findall(r'([0-9]*)(\w| )', string)
    return "".join([char * int(count or 1) for (count, char) in groups])


def encode(string):
    groups = groupby(string)
    return "".join([try_encode(list(group)) for key, group in groups])

def try_encode(chars): 
    return f"{str(len(chars)) if len(chars) > 1 else ''}{chars[0]}"
