max_length = 0
longest_line = ''
with open('/Users/dariasotnikova/Desktop/Python/QA/20. The longest line.py', 'r') as file:
    for line in file:
        line = line.rstrip('\n')
        line_length = len(line)
        if line_length >= max_length:
            longest_line = line
            max_length = line_length
print("The longest line is:", longest_line)
print("The maximum length is:", max_length)