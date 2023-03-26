# Question Generator For Alpaca Like Models

Update5PM3/25-Wasn't grabbing unique tasks for the rewrite gens. Now the base can generate somewhere between 100k unique questions without adding anymore variables. Maybe even more than that, I haven't tested it much.

Update use the 60k for correct formatting or make your own, I updated the scripts to fix formatting issues.

This repository contains four generator scripts that can generate 1,000,000 questions and save them to `output.txt`. You can then run the `removenumber` script and the `removedupes` script to obtain a new file with unique questions on each line. As a bonus, there's also a set of 60k unique questions included if you just want to use those.

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

Pre-generated Questions
If you just want to use the included set of 60k unique questions, you can find them in the 60k_unique_questions.txt file.
If you're wondering what the point of this is. It's to create questions to ask larger LLM's to get your smaller one to perform much better.
You'll need to format the questions after asking the larger LLM to make sure you get the best results when finetuning but I leave that up to you. 

Contact
If you have any questions or feedback, feel free to reach out on Twitter:

@WoodnBarrelGame
