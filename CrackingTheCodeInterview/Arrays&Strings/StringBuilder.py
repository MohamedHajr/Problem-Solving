class StringBuilder(object):
    def __init__(self, val):
        self.store = [val]

    def __iadd__(self, value):
        self.store.append(value)
        return self

    def __str__(self):
        return "".join(self.store)


initial = 'value'
stringBuilder = StringBuilder(initial)
for _ in range(2000):
    stringBuilder += 'value'
print(str(stringBuilder))
