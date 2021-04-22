"""
Joins all labels from different classes into one class
"""

import os

input_dir = ''
output_dir = ''

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for filename in os.listdir(input_dir):
    if filename.endswith(".txt") and filename != "train.txt":
        input_file = open(os.path.join(input_dir, filename))
        output_file = open(os.path.join(output_dir, filename), "w")
        for line in input_file:
            if line[0] == '0':
                output_file.write(line)
        input_file.close()
        output_file.close()
