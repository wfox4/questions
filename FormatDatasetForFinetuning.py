import json

def transform_json_data(input_file, output_file):
    with open(input_file, 'r') as infile:
        data = json.load(infile)

    transformed_data = []

    for index, item in enumerate(data):
        print(f'Item {index + 1}: {item["input"]}')
        delimiter = input('Enter the delimiter for this item (or leave blank to skip): ')

        if delimiter and delimiter in item['input']:
            delimiter_index = item['input'].find(delimiter)
            instruction = item['input'][:delimiter_index].strip()
            input_text = item['input'][delimiter_index:].strip()
            transformed_item = {
                'instruction': instruction,
                'input': input_text,
                'output': item['output']
            }
        else:
            transformed_item = {
                'instruction': item['input'],
                'input': '',
                'output': item['output']
            }

        transformed_data.append(transformed_item)

        # Save the current transformed data to the output file after each item
        with open(output_file, 'w') as outfile:
            json.dump(transformed_data, outfile, indent=2)

input_file = r'C:\Users\thewh\Documents\responsesfromLLM.json'
output_file = r'C:\Users\thewh\Documents\responsesTEST.json'

transform_json_data(input_file, output_file)