import os
file_path = '/Users/dariasotnikova/Desktop/Python/Homework/the longest line/20. The longest line in the file txt.py'
if not os.path.isfile(file_path):
    print("The file was not found. Please check the file path.")
else:
    max_length = 0
    longest_line = ''

    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                line_length = len(line)
                if line_length >= max_length:
                    longest_line = line
                    max_length = line_length
    except IOError:
        print("An IOError occurred while reading the file.")

    if longest_line:
        print("The longest line is:", longest_line)
        print("The maximum length is:", max_length)
    else:
        print("The file is empty or an error occurred.")