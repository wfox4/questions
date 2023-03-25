import os
import random


leader_titles = [
    'the First', 'the Second', 'the Third', 'the Last', 'the Previous', 'the fifth', 'the 1st', 'the 2nd', 'the 3rd', 'the 4th', 'the most recent', 'the most revered', 'the most most impactful',
    ]

major_war_modifiers = {
    'Major_Wars': ['theme of the', 'type of War that was the', 'difference between now and the', 'cause of the',],
}

concepts_history = {
    'Leaders': ['Prime Minister of New Zealand', 'President of Indonesia','President of the United States', 'Chancellor of Germany', 'President of France', 'Prime Minister of Canada', 'Emperor of Japan', 'President of Russia', 'Prime Minister of Australia', 'President of Brazil', 'Prime Minister of India', 'President of South Africa', 'President of Mexico', 'Prime Minister of Italy', 'President of Argentina', 'King of Saudi Arabia', 'President of Turkey', 'Prime Minister of Israel', 'President of South Korea', 'President of Indonesia', 'Prime Minister of New Zealand'],
    'Major_Wars': ['World War I', 'World War II', 'American Civil War', 'Vietnam War', 'Korean War', 'Napoleonic Wars', 'War of 1812', 'Spanish-American War', 'Gulf War', 'Crimean War', 'Falklands War', 'Six-Day War', 'Russo-Japanese War', 'Peloponnesian War', 'Hundred Years War', 'War of the Roses', 'Seven Years War'],
    'Inventions': ['telephone', 'light bulb', 'automobile', 'The internet', 'The airplane', 'The steam engine', 'The printing press', 'The compass', 'The wheel', 'The telescope', 'The microscope', 'The camera', 'The radio'],
    '21st_Century_Political_Events': ['Brexit', 'Arab Spring', 'COVID-19 pandemic','Election of Barack Obama','Occupy Wall Street movement','Russian annexation of Crimea','The rise of ISIS','Hong Kong protests','US-China trade war','Impeachment of Donald Trump',"India's Citizenship Amendment Act protests",],
    'Tech_Companies': ['Apple', 'Google', 'Amazon','Microsoft','Facebook','Tesla','Netflix','Alibaba','TikTok','Uber','Airbnb'],
    'Environmental_Issues': ['climate change', 'deforestation', 'plastic pollution','Ocean acidification','Loss of biodiversity','Air pollution','Ozone layer depletion','Overfishing','Desertification','Water scarcity','Melting polar ice caps', 'Invasive species', 'Soil erosion and degradation', 'Urban sprawl', 'Waste disposal and management', 'Resource depletion (e.g., deforestation, mining, over-extraction of water)', 'Chemical pollution (e.g., pesticides, fertilizers, toxic waste)', 'Noise pollution', 'Light pollution', 'Loss of coral reefs', 'industrial agriculture', 'Habitat destruction', 'Mountaintop removal mining', 'Endangered species', 'Genetically modified organisms (GMOs) and their environmental impact', 'Marine debris and plastic pollution'],
}

concepts_science = {
    'Physics_Laws': ["Newton's first law", "Newton's second law", "Newton's third law","Ohm's law", "Boyle's law", "Charles' law", "Watt's law", "Faraday's law of induction", "Gauss' law", "Lorentz force law", "Hooke's law", "Archimedes' principle", "Pascal's law", "Maxwell's equations", "Einstein's theory of relativity", "Schrödinger's equation", "Heisenberg uncertainty principle", "Planck\'s law of black-body radiation", "Bohr's atomic model", "Rutherford scattering", "Compton effect", 'Quantum entanglement', 'Cosmological principle'],
    'Chemistry_Elements': ['hydrogen', 'helium', 'carbon'],
    'Biology_Cells': ['prokaryotic', 'eukaryotic', 'plant''animal', 'bacterial', 'fungal', 'protist', 'ciliated', 'flagellated', 'neuron', 'muscle', 'gamete', 'stem', 'white blood', 'red blood', 'nerve', 'bone', 'liver', 'pancreas', 'kidney', 'thyroid', 'ovum', 'sperm'],
    'Space_Exploration': ['Mars Rover', 'SpaceX', 'James Webb Space Telescope', 'Voyager missions', 'Hubble Space Telescope', 'Curiosity Rover', 'New Horizons mission'],
    'Renewable_Energy': ['solar power', 'wind power', 'hydro power', 'geothermal power', 'tidal power', 'biomass energy'],
    'Artificial_Intelligence': ['machine learning', 'deep learning', 'neural networks', 'natural language processing', 'computer vision', 'reinforcement learning', 'Generative Adversarial Networks (GANs)', '4-bit quantization inference.', '4-bit quantization fine-tuning.', '4-bit quantization tuning.', 'GPT Models.',],
}

concepts_literature = {
    
    'Famous_Authors': ['William Shakespeare', 'Jane Austen', 'Charles Dickens', 'Mark Twain', 'Ernest Hemingway', 'F. Scott Fitzgerald', 'Virginia Woolf', 'James Joyce', 'Herman Melville', 'Leo Tolstoy', 'Fyodor Dostoevsky', 'Edgar Allan Poe', 'Nathaniel Hawthorne', 'Emily Dickinson', 'Walt Whitman', 'Toni Morrison', 'Gabriel Garcia Marquez', 'Jorge Luis Borges', 'Isabel Allende', 'Paulo Coelho', 'J.K. Rowling', 'Stephen King', 'Dan Brown', 'George R.R. Martin', 'J.R.R. Tolkien', 'C.S. Lewis', 'Agatha Christie', 'Ernest Cline', 'Margaret Atwood', 'John Steinbeck', 'Harper Lee', 'Salman Rushdie', 'Chimamanda Ngozi Adichie', 'David Foster Wallace', 'William Faulkner', 'Toni Morrison', 'Maya Angelou', 'Gabriel Garcia Marquez', 'Vladimir Nabokov', 'Milan Kundera',],
    
    'Literary_Genres': ['poetry', 'drama novels', 'fiction novels', 'fables around the world', 'epic fantasy', 'gothic inspiration in writing', 'dark fantasy', 'crime thrillers', 'romance novels', 'biographies', 'horror storytelling', 'mystery storytelling', 'adventure storylines', 'tragedy stories', 'satire media', 'young adult genres', 'science fiction',],
    
    'Classic_Novels': ['Pride and Prejudice', 'To Kill a Mockingbird', '1984'],
    'Public_Artworks': ['Cloud Gate', 'The Kelpies', 'The Bean', 'The Gates', 'LOVE Sculpture', 'Charging Bull', 'Angel of the North', 'Fearless Girl', 'Sky Mirror', 'Fountain of Wealth', 'Magic Fountain of Montjuïc', 'The Spire', 'The Monument'],
    
    'Music_Artists': ['Billie Eilish', 'Ariana Grande', 'Ed Sheeran', 'Banksy', 'Yayoi Kusama', 'Ai Weiwei', 'Kehinde Wiley', 'JR', 'Kara Walker', 'Zhang Huan', 'Cindy Sherman', 'Julie Mehretu', 'Yinka Shonibare', 'Mickalene Thomas', 'Takashi Murakami', 'Marina Abramović'],
    
    'TV_Shows': ['Game of Thrones', 'Stranger Things', 'The Mandalorian','The Crown', "The Queen's Gambit", 'The Office', 'Breaking Bad', 'Friends', 'The Sopranos', 'House of Cards', "The Handmaid's Tale", 'Westworld', 'The Boys', 'Avengers: Endgame', 'Black Panther', 'Parasite'],
    
    'Leaders': ['Who was the', 'Identify the', 'Name the', 'Explain the', 'Write a description of', 'Describe the impact of the', 'Design a article for the', 'Construct a timeline for the', 'Design logo for the', 'Generate a list of achievements about', 'Create a story using', 'Generate a rap song about', 'Generate a tweet about', 'Identify the subject for',],
}


phrases = {
    'Compare': ['Compare and contrast', 'Explain the differences between', 'Write a detailed description contrasting', 'Create a list comparing', 'Generate a article discussing', 'Constuct a detailed timeline of', 'Construct a brief list of events for', 'Summarize the differences between', 'Design an algorithm for predicting the effects between'],
    
    'Leaders': ['Who was the', 'Identify the', 'Name the', 'Explain the', 'Write a description of', 'Describe the impact of the', 'Design a article for the', 'Construct a timeline for the', 'Design logo for the', 'Generate a list of achievements about', 'Create a story using', 'Generate a rap song about', 'Generate a tweet about', 'Identify the subject for',],
    
    'Figures': ['Who was the', 'Identify the', 'Name the', 'Explain the', 'Write a description of', 'Describe the impact of the', 'Design a article for the', 'Construct a timeline for the', 'Design logo for the', 'Generate a list of achievements about', 'Create a story using', 'Generate a rap song about', 'Generate a tweet about', 'Identify the subject for',],
    
    'Major_Wars': ['Identify the cause of', 'What was ', 'Which countries were involved in', 'Explain the', 'Write a description of', 'Summarize the impact of', 'What was the impact of the', 'In which year was the', 'Design a article for the', 'Construct a timeline for the', 'Design logo for the', 'Suggest an idea for the cause of', 'Make a prediction about a world without', 'Identify the subject for', 'Describe the difference in history without the following', 'Provide an example of'],
    
    'Inventions': ['Who invented the', 'In which year was the following invented', 'What was the impact of the', 'Explain the purpose behind', 'Write a description of', 'Write a tweet about', 'Generate a tweet about','Summarize the impact of', 'Label the category for the following', 'Describe the benefits of', 'Design a article for the', 'Design logo for the', 'Suggest a new idea using', 'Construct a timeline for', 'Identify the difference made when using', 'Generate an article about', 'Identify the subject for', 'Provide an example of'],
    
    'Physics_Laws': ['Explain the meaning of', 'Find the word that best describes', 'Describe the meaning of', 'Explain a function of', 'Write a description of', 'Write a tweet about', 'Design a article for the', 'Design logo for the', 'Generate an article about', 'Suggest a new idea using', 'Construct a timeline for', 'Identify the subject for', 'Provide an example of'],
    
    '21st_Century_Political_Events': ['Explain the concept of', 'State', 'Describe the concept of', 'Write a description of', 'Construct a timeline for the', 'Design logo for the', 'Identify the subject for', 'Explain the meaning of', 'Describe the difference in history without the following', 'Provide an example of'],
    
    'Environmental_Issues': ['Explain the concept of', 'State', 'Describe the concept of', 'Explain', 
    'Write a description of', 'Construct a timeline for the', 'Design a logo for the', 'Provide five solutions for', 'Provide solution for', 'Provide an example of', 'Provide a detailed summary of', 'Provide a brief summary of', 'Provide an ordered summary of', 'Classify the word', 'Describe the impact of', 'Name the type of issue for the following', 'Write detailed summary of', 'Describe the process of', 'Give an example of', 'Give a list for damage caused by', 'Generate a question about', 'Make a prediction if the following continues,', 'Suggest a strategy for dealing with', 'Suggest an idea for resolving', 'Design an experiment to test a solution for', 'Make a suggestion for fixing', 'Make a list of solutions for', 'Generate a tweet about', ],
    'Chemistry_Elements': ['What is the atomic number of', 'What is the symbol for', 'What is a common use for', 'Explain the', 'Write a description of', 'Design a logo for the', 'Provide an ordered summary of', 'Provide an example of', 'Provide a detailed summary of', 'Write detailed summary of', 'Generate an article about', 'Design an algorithm for measuring the effects of'],
    
    'Biology_Cells': ['Describe the structure of', 'What is the main difference between', 'What is a unique feature of', 'Explain the', 'Write a description of', 'Design logo for the', 'Generate an article about', "Convert the following word to it's scientific name,", 'Construct an agruement against', 'Suggest a way to alter the following for a benefit', 'Provide an example of'],
    
    'Music_Artists': ['Write a Song in style of', 'What was the singing style of', 'What is a famous quote by', 'Write a Poem in the style of', 'Write a description of', 'Design a logo for', 'Generate a list of achievements about', 'Provide an example of'],
    
    'Famous_Authors': ['Which book was written by', 'Generate a story in the style of', 'Generate a poem in the style of','What is a famous quote by', 'Explain the', 'Write a description of', 'Rewrite in the style of', 'Generate a list of achievements about', 'Provide an example of'],
    
    'Literary_Genres': ['Give an example of', 'What are the main characteristics of', 'What is the origin of', 'Explain the purpose of', 'Write a description of', 'Summarize the point of', 'Provide an example of'],
    
    'Public_Artworks': ['Give an example of', 'What are the main characteristics of', 'What is the origin of', 'Explain the purpose of', 'Write a description of', 'Explain the concept of',],
    
    'Renewable_Energy': ['Give an example of', 'What are the main characteristics of', 'What is the origin of', 'Explain the purpose of','Describe the process of', 'Write a description of', 'Design logo for', 'Provide an example of'],
    
    'Space_Exploration': ['Give an example of', 'What are the main characteristics of', 'What is the origin of', 'Explain the concept of', 'Write a description of', 'Design a logo for the following,', 'Generate a story for', 'Generate a list of achievements about', 'Describe the benefits of', 'Provide an example of'],
    
    'Artificial_Intelligence': ['Give an example of', 'What are the main characteristics of', 'What is the origin of', 'Explain the concept of', 'Write a description of', 'Design a logo for', 'Construct a timeline for', 'Design an algorithm in Python for the following', 'Design an algorithm for a website about the following', 'Design a creative game about', 'Describe the benefits of', 'Provide an example of'],
    
    'Tech_Companies': ['Give an example of', 'What are the main characteristics of', 'What is the origin of', 'Explain the', 'Write a description of', 'Design logo for', 'Provide an example of'],
    
    'Classic_Novels': ['Who is the protagonist in', 'What is the main theme of', 'What is the setting of', 'Explain the concept of', 'Write a description of', 'Provide an example of'],
    
    'TV_Shows': ['Who is the protagonist in', 'What is the main theme of', 'What is the setting of', 'Explain the concept of', 'Write a description of', 'Design logo for', 'Construct a timeline for', 'Provide an example of'],
}


concept_dicts = [concepts_history, concepts_science, concepts_literature]
concept_dict = random.choice(concept_dicts)




def generate_problem(concept_key, concept_dicts, leader_titles=None, major_war_modifiers=None):
    phrase = random.choice(phrases[concept_key])

    if concept_key == 'Compare':
        concept_dict = random.choice(concept_dicts)
        random_key = random.choice(list(concept_dict.keys()))
        concept1, concept2 = random.sample(concept_dict[random_key], 2)
        question = f"{phrase} {concept1} and {concept2}?"
    elif concept_key == 'Leaders':
        concept = random.choice(concept_dicts[0][concept_key])  # Assuming concepts_history is the first element in concept_dicts
        title = random.choice(leader_titles)
        question = f"{phrase} {title} {concept}?"
    elif concept_key == 'Major_Wars':
        concept = random.choice(concept_dicts[0][concept_key])  # Assuming concepts_history is the first element in concept_dicts
        question = f"{phrase} {concept}?"
    else:
        concept_dict = random.choice(concept_dicts)
        concept = random.choice(concept_dict[concept_key])
        question = f"{phrase} {concept}?"

    print(question)
    return question


def generate_problems_for_concept(concept_key, concept_dicts, n_problems, leader_titles=None, major_war_modifiers=None):
    problems = []
    for _ in range(n_problems):
        problem = generate_problem(concept_key, concept_dicts, leader_titles, major_war_modifiers)
        problems.append(problem)
    return problems

# Your existing code to define concepts_history, concepts_science, concepts_literature, leader_titles, and major_war_modifiers

problems = []
concept_dicts = [concepts_history, concepts_science, concepts_literature]

# Generate problems for history concepts
problems.extend(generate_problems_for_concept('Compare', concept_dicts, 200000))
problems.extend(generate_problems_for_concept('Leaders', concept_dicts, 100000, leader_titles=leader_titles))
problems.extend(generate_problems_for_concept('Major_Wars', concept_dicts, 100000, major_war_modifiers=major_war_modifiers))

# Generate problems for science concepts
problems.extend(generate_problems_for_concept('Compare', concept_dicts, 200000))
# Add other science-related keys and their respective n_problems here, if any

# Generate problems for literature concepts
problems.extend(generate_problems_for_concept('Compare', concept_dicts, 200000))
# Add other literature-related keys and their respective n_problems here, if any

random.shuffle(problems)

output_file_path = r'C:\Users\XXXXXX\Documents\output.txt'

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for i, problem in enumerate(problems):
        line = f"{i+1}. {problem}\n"
        print(line.strip())  # Print the problems to the terminal without the newline character
        output_file.write(line)