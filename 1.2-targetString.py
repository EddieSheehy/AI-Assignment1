import random
import matplotlib.pyplot as plt

population_size = 100
# 'Let the length of the strings be 30'
string_lengths = 30
num_generations = 30
target_string = '110011001100110011001100110011'  # Target string


# 'The initial population should be randomly created.'
population = [''.join(random.choice('01') for _ in range(string_lengths)) for _ in range(population_size)]

# Define the fitness function (number of 1s in the binary string)
def fitness(string):
    return sum(1 for bit1, bit2 in zip(string, target_string) if bit1 == bit2)

# Lists to store average fitness over generations
average_fitness_values = []

# Main for loop
for generation in range(num_generations):
    # Calculate fitness for each string
    fitness_scores = [fitness(string) for string in population]

    # Calculate average fitness
    average_fitness = sum(fitness_scores) / population_size
    average_fitness_values.append(average_fitness)  # Store the average fitness for later

    print(f"Generation {generation}: Average Fitness = {average_fitness:.2f}")

    # Select parents for crossover using 'tournament selection'
    selected_parents = []
    for _ in range(population_size):
        tournament = random.sample(range(population_size), 5)  # Tournament size = 5
        selected_parent = max(tournament, key=lambda i: fitness_scores[i])
        selected_parents.append(population[selected_parent])

    # Perform one-point crossover
    offspring = []
    for i in range(0, population_size, 2):
        parent1 = selected_parents[i]
        parent2 = selected_parents[i + 1]
        crossover_point = random.randint(1, string_lengths - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        offspring.extend([child1, child2])

    # Apply mutation
    for i in range(population_size):
        if random.random() < 0.01:
            mutation_point = random.randint(0, string_lengths - 1)
            population[i] = population[i][:mutation_point] + ('0' if population[i][mutation_point] == '1' else '1') + population[i][mutation_point + 1:]

    # Replace the old population with the new offspring
    population = offspring
    
# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(range(num_generations), average_fitness_values)
plt.xlabel('Generation')
plt.ylabel('Average Fitness')
plt.title('Average Fitness vs. Generations for One-Max Problem')
plt.grid(True)

# Show the plot
plt.show()
