actions = {
    0: 'right',
    1: 'down',
    2: 'left',
    3: 'up'
}

def find_spiral(matrix, actionNumber = 0):
    nextAction = (actionNumber + 1) % 4
    if actions[actionNumber] == 'right':
        if len(matrix) == 1:
            return matrix[0]
        else:
            return matrix[0] + find_spiral(matrix[1:], nextAction)
    elif actions[actionNumber] == 'left':
        if len(matrix) == 1:
            return matrix[0][::-1]
        else:
            return matrix[-1][::-1] + find_spiral(matrix[:-1], nextAction)
    elif actions[actionNumber] == 'up':
        first_elements = []
        rest_of_matrix = []
        for xs in matrix:
            first_elements.append(xs[0])
            rest_of_matrix.append(xs[1:])
        return first_elements + find_spiral(rest_of_matrix, nextAction)
    elif actions[actionNumber] == 'down':
        last_elements = []
        rest_of_matrix = []
        for xs in matrix:
            last_elements.append(xs[-1])
            rest_of_matrix.append(xs[:-1])
        return last_elements + find_spiral(rest_of_matrix, nextAction)

def find_spiral(matrix):
    
    output = []
    
    while matrix:
        row = matrix.pop(0)
        output.extend(row)
        matrix = zip(*matrix)[::-1] 

    return output
