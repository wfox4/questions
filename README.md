# Question Generator For Alpaca Like Models

Final Update: The Questions I used for https://huggingface.co/datasets/whitefox44/AlpacaGPT3.5Customized are now inside the instruction list. Hopefully when GPT4 API comes out I can run them through that.


This repository contains four generator scripts (Each Script is based on different aspects and formatting) that can generate questions and save them to `output.txt`. You can then run the `removenumber` script and the `removedupes` script to obtain a new file with unique questions on each line. As a bonus, there's also a set of 60k unique questions included if you just want to use those.

## Usage

You might need to create two text files one named output.txt and one named samplequestions.txt


1. Run one of the generator scripts to generate 1,000,000 questions:

   ```sh
   python generator_script_name.py
   
Replace generator_script_name with the name of the generator script you want to use.

2. (Optional) Modify the generator script to specify a different output location.

3. Run the removenumber script:

python removenumber.py

4. Run the removedupes script:

python removedupes.py

After completing these steps, you'll see the samplequestions.txt file will contain unique questions on each line.

You have to move them or make a copy of the file before running the other generators. So do one at a time and make sure you run the remove numbers and dupes for each generator.

After generating the questions AND generating outputs from other sources, follow these steps to transform the JSON data using the FormatDatasetForFinetuning.py script:

1. Create an input JSON file containing the generated questions. Name it responsesfromLLM.json or modify the input_file variable in the script to match your input file name.

2, (Optional) Create an output JSON file named responsesTEST.json or modify the output_file variable in the script to specify a different output location.

3. Run the FormatDatasetForFinetuning.py script:

Copy code
   
   python FormatDatasetForFinetuning.py

4. The script will prompt you to enter the delimiter for each item. Enter the desired delimiter to split the input text into instruction and input parts. If you don't want to split an item, press Enter without typing anything.

5. The transformed JSON data will be saved to the output file after processing each item.

After completing these steps, the output JSON file will contain the transformed data with separated instructions and inputs based on the provided delimiters.


Pre-generated Questions
If you just want to use the included set of 60k unique questions, you can find them in the 60k_unique_questions.txt file.
If you're wondering what the point of this is. It's to create questions to ask larger LLM's to get your smaller one to perform much better.
You'll need to format the questions after asking the larger LLM to make sure you get the best results when finetuning but I leave that up to you. 

Contact
If you have any questions or feedback, feel free to reach out on Twitter:

@WoodnBarrelGame
