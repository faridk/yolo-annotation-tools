import os
import collections

input_dir = ''

label_counts = dict()

for task_dir in os.listdir(input_dir):
    annotation_dir = os.path.join(input_dir, task_dir, "labels")
    for filename in os.listdir(annotation_dir):
        if filename.endswith(".txt") and filename != "train.txt":
            annotation_file = open(os.path.join(annotation_dir, filename))
            for line in annotation_file:
                line_tokens = line.split(" ")
                label = int(line_tokens[0])
                label_counts[label] = label_counts.get(label, 0) + 1
            annotation_file.close()

# Sort dictionary by key
label_counts = collections.OrderedDict(sorted(label_counts.items()))
print(label_counts)

