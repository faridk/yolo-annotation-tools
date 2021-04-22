import os

input_dir = ''
output_dir = ''

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for filename in os.listdir(input_dir):
    if filename.endswith(".txt") and filename != "train.txt":
        input_file = open(os.path.join(input_dir, filename))
        output_file = None
        for line in input_file:
            line_tokens = line.split(" ")
            if int(line_tokens[0]) < 17:
                print(int(line_tokens[0]))
                output_file = open(os.path.join(output_dir, filename), "w")
                output_file.write(line)
        input_file.close()
        if output_file is not None:
            output_file.close()
