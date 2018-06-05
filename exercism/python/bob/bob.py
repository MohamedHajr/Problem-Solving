import re


def respond_to_question(s):
    return 'Sure.' if s.endswith('?') else None


def respond_to_noword(s):
    return "Fine. Be that way!" if s == '' else None


def respond_to_yelling(s):
    if s.isupper():
        if s[-1] == '?':
            return 'Calm down, I know what I\'m doing!'
        else:
            return 'Whoa, chill out!'
    else:
        return None


def hey(phrase):
    stripped = phrase.strip()
    return (respond_to_noword(stripped)
            or respond_to_yelling(stripped)
            or respond_to_question(stripped)
            or 'Whatever.')
