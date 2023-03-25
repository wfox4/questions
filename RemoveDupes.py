
file_path = os.path.join(script_dir, 'SampleQuestions.txt')

# Read and deduplicate the lines
with open(file_path, 'r') as f:
    lines = f.readlines()
    unique_lines = list(set(lines))

# Write the unique lines to the output file
with open(file_path, 'w') as f:
    for line in unique_lines:
        f.write(line)

print("De-duplication complete!")
