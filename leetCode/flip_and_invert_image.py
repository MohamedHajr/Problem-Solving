def flipAndInvertImage(self, A):
    return list(map(lambda array: list(map(lambda element: int(bool(element) != bool(1)), array[::-1])), A))
