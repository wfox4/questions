import random

concepts_multi = {
    'greatest_common_factor': ['GCF', 'greatest common divisor'],
    'least_common_multiple': ['LCM', 'lowest common multiple'],
    'sum': ['sum'],
    'product': ['product'],
}

concepts_single = {
    'prime_factorization': ['prime factors'],
    'square': ['square'],
    'cube': ['cube'],
}

phrases_multi = {
    'greatest_common_factor': ['Find', 'Calculate', 'Determine'],
    'least_common_multiple': ['Find', 'Compute', 'Obtain'],
    'sum': ['Find', 'Calculate', 'Compute'],
    'product': ['Find', 'Calculate', 'Compute'],
}

phrases_single = {
    'prime_factorization': ['Find', 'List', 'Identify'],
    'square': ['Find', 'Calculate', 'Compute'],
    'cube': ['Find', 'Calculate', 'Compute'],
}

def generate_problem_multi(concept_key, min_val, max_val):
    concept = random.choice(concepts_multi[concept_key])
    phrase = random.choice(phrases_multi[concept_key])
    num_count = random.randint(2, 5)
    numbers = [random.randint(min_val, max_val) for _ in range(num_count)]

    return f"{phrase} the {concept} of {', '.join(map(str, numbers))}."

def generate_problem_single(concept_key, min_val, max_val):
    concept = random.choice(concepts_single[concept_key])
    phrase = random.choice(phrases_single[concept_key])
    num = random.randint(min_val, max_val)

    return f"{phrase} the {concept} of {num}."

problems = []

for _ in range(2000):
    concept_key = random.choice(list(concepts_multi.keys()))
    problem = generate_problem_multi(concept_key, 1, 2500)
    problems.append(problem)

for _ in range(2000):
    concept_key = random.choice(list(concepts_single.keys()))
    problem = generate_problem_single(concept_key, 1, 2500)
    problems.append(problem)

random.shuffle(problems)

for i, problem in enumerate(problems):
    print(f"{i+1}. {problem}")
