# questions

Update5PM3/25-Wasn't grabbing unique tasks for the rewrite gens. Now the base can generate somewhere between 100k questions maybe even more.

Update use the 60k for correct formatting or make your own, I updated the scripts to fix formatting issues.

This repository contains four generator scripts that generate 1,000,000 questions and save them to `output.txt`. You can then run the `removenumber` script and the `removedupes` script to obtain a new file with unique questions on each line. As a bonus, there's also a set of 67k unique questions included if you just want to use those.

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
If you just want to use the included set of 67k unique questions, you can find them in the 67k_unique_questions.txt file.

Contact
If you have any questions or feedback, feel free to reach out on Twitter:

@WoodnBarrelGame
