def count_lines(filepath):
    file = open(filepath, 'r')
    return (sum(1 for l in file))