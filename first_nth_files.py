def read_line_number(filepath, line_number):
    file = open(filepath, 'r')
    for line_num, line in enumerate(file, start=1):
        if line_num == line_number:
            return line