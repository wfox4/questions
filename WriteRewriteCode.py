import random

tasks = {
    'Code': ['Write an algorithm', 'Write a program', 'Provide a solution', 'Describe the process', 'Explain the concept', 'Write a function', 'Design an algorithm',],
}

taskmodifiers = {
    'Code': ['Python', 'JavaScript', 'Java', 'C++', 'C#','Ruby', 'PHP', 'Swift', 'Kotlin', 'TypeScript', 'Go (Golang)', 'Go', 'Rust', 'R', 'Scala', 'Lua', 'Haskell', 'Dart', 'Groovy', 'Elixir', 'Perl', 'using F#', 'Julia', 'Objective-C', 'Shell (Bash)', 'Shell', 'SQL', 'MATLAB', 'Ada', 'Fortran', 'COBOL', 'Erlang',],
}

informationtoalter = {
    'Code': ['that goes through two different jsons and compares the each item for duplicates. ', 'to calculate the factorial of a given number.', 'to convert a given string to uppercase.', 'to convert Fahrenheit to Celsius', 'to find the minimum element in an array.', 'to calculate the perimeter of a rectangle.', 'that gets all items from one file and adds them to another.', 'that runs an api call for each item in a file.', 'performs a function on an array of numbers and returns the result', 'that takes in a string and returns the number of vowels in the string.', 'that takes in a list of integers and returns the largest number in the list.', 'that checks if a given string is a palindrome.', "that takes in a list of integers and returns a new list with only the even numbers from the original list.", 'that checks if a given integer is prime.', "that takes in a list of strings and returns a new list with only the strings that contain the letter 'a'.", 'that sorts a list of integers in ascending order.', 'that takes in a list of integers and returns a new list with the numbers sorted in descending order.', 'that takes in a list of integers and returns the second largest number in the list.', 'that takes in two integers and returns their sum.', 'that calculates the factorial of a given integer.', 'that takes in a list of integers and returns a new list with the numbers sorted in descending order.', 'that takes in a list of integers and returns the second largest number in the list.', 'that takes in a string and returns a new string with all the vowels removed.', 'that checks if two strings are anagrams of each other.', 'that takes in a list of integers and returns the sum of all the even numbers in the list.', 'that takes in a list of integers and returns a new list with only the prime numbers from the original list.', 'that takes in a string and returns the length of the longest word in the string.', 'that takes in a list of strings and returns a new list with the strings sorted in alphabetical order.', 'that takes in a list of integers and returns a new list with the numbers squared.', 'that takes in a list of integers and returns the second smallest number in the list.', 'that takes in a string and returns the reverse of the string.', 'that takes in a list of strings and returns the shortest string in the list.', 'that takes in two strings and returns True if the first string is a substring of the second string.', 'that takes in a list of integers and returns the median of the numbers in the list.', 'that takes in a list of integers and returns the product of all the numbers in the list.', 'that takes in a list of strings and returns a new list with only the strings that have length greater than 5.', 'that takes in a list of integers and returns a new list with only the odd numbers from the original list.', 'that checks if a given string is a valid email address.', 'that takes in a list of strings and returns a new list with only the strings that start with a vowel.', 'that takes in a list of integers and returns the sum of all the numbers in the list.', 'that takes in a string and returns the first non-repeated character in the string.', 'that takes in a list of strings and returns a new list with the strings sorted by length, from shortest to longest.', 'that takes in a list of integers and returns a new list with the numbers rounded to the nearest hundred.', 'that takes in a list of integers and returns the third largest number in the list.', 'that takes in a string and returns True if the string contains only unique characters.', 'that takes in a list of integers and returns a new list with the numbers sorted by absolute value, from smallest to largest.', 'that takes in a list of integers and returns the count of numbers that are divisible by 3.', 'that takes in a list of strings and returns a new list with the strings reversed.', 'that takes in a string and returns the number of words in the string.', 'that takes in a list of integers and returns the average of the numbers in the list, rounded to two decimal places.', 'that takes in a list of integers and returns the smallest number that is greater than zero and not in the list.', 'that takes in a list of integers and returns the maximum sum of any contiguous subsequence.', 'that takes in a string and returns the most common character in the string.', 'that takes in a list of integers and returns the number of distinct values in the list.', 'that takes in a list of integers and returns a new list with the numbers sorted by parity, with all even numbers coming before odd numbers.', 'that takes in a list of strings and returns a new list with the strings that have the same length as the first string in the original list.', 'that takes in a string and returns True if the string is a valid palindrome, ignoring case and non-alphanumeric characters.', 'that takes in a list of integers and returns the largest product of any three numbers in the list.', 'that takes in a list of integers and returns a new list with the numbers in reverse order.', 'that takes in a list of strings and returns a new list with the strings sorted by the number of vowels they contain, from fewest to most.', 'that takes in a list of strings and returns the longest common prefix of the strings.', 'that takes in a list of integers and returns the number of times the largest value appears in the list.', 'that takes in a string and returns True if the string is a valid IPv4 address.', 'that takes in a list of integers and returns the length of the longest increasing subsequence in the list.', 'that takes in a list of integers and returns True if any two numbers in the list add up to a target sum.', 'that takes in a list of integers and returns the kth largest number in the list.', 'that takes in a string and returns the number of times each word appears in the string, as a dictionary with the words as keys and the counts as values.', 'that takes in a list of integers and returns a new list with only the numbers that appear more than once in the original list.', 'that takes in a list of strings and returns True if the strings can be concatenated to form a palindrome.', 'that takes in a list of integers and returns the length of the longest subarray with equal number of 0s and 1s.',],
    
   
}

def generate_prompt(task_key):
    task = tasks[task_key][0]  # Get the primary task description

    # Decide randomly if a modifier should be applied
    apply_modifier = random.choice([True, False])

    if apply_modifier:
        modifier = random.choice(taskmodifiers[task_key])
        # Define a list of words to add before the modifier
        words_before_modifier = ['using', 'in', 'for', 'with']
        word = random.choice(words_before_modifier)
        modifier = f"{word} {modifier}"
    else:
        modifier = ''

    info_to_alter = random.choice(informationtoalter[random.choice(list(informationtoalter.keys()))])

    return f"{task} {modifier} {info_to_alter}".strip() + "."

# Call the function 100,000 times and save the results to a text file

output_file_path = r'C:\Users\XXXXXX\Documents\output.txt'

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for i in range(1000000):
        problem = generate_prompt('Code')
        line = f"{i+1}. {problem}\n"
        print(line.strip())  # Print the problems to the terminal without the newline character
        output_file.write(line)