import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Set the input and output file names
input_file = os.path.join(script_dir, 'output.txt')
output_file = os.path.join(script_dir, 'SampleQuestions.txt')

# Set the predefined string to remove text before
predefined_string = '. '

# Read the input file
with open(input_file, 'r') as file:
    lines = file.readlines()

# Process the lines
processed_lines = []
for line in lines:
    index = line.find(predefined_string)
    if index != -1:
        new_line = line[index + len(predefined_string):]
    else:
        new_line = line
    processed_lines.append(new_line)

# Save the processed lines to the output file
with open(output_file, 'w') as file:
    file.writelines(processed_lines)

print(f"Processed file saved as {output_file}.")
