import random
import csv
import matplotlib.pyplot as plt

# Define parameters
population_size = 100
chromosome_length = 30
mutation_rate = 0.01
num_generations = 100

# Initialize the population with random binary strings
population = [''.join(random.choice('01') for _ in range(chromosome_length)) for _ in range(population_size)]

# Define the fitness function for the deceptive landscape
def fitness(chromosome):
    num_ones = sum(int(bit) for bit in chromosome)
    if num_ones == 0:
        return 2 * len(chromosome)  # High fitness if no 1s are present
    else:
        return num_ones

# Lists to store average fitness over generations
average_fitness_values = []

# Main loop
for generation in range(num_generations):
    # Calculate fitness for each chromosome
    fitness_scores = [fitness(chromosome) for chromosome in population]

    # Calculate average fitness
    average_fitness = sum(fitness_scores) / population_size
    average_fitness_values.append(average_fitness)  # Store the average fitness for later

    print(f"Generation {generation}: Average Fitness = {average_fitness:.2f}")

    # Select parents for crossover using tournament selection (you can implement other selection methods)
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
        crossover_point = random.randint(1, chromosome_length - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        offspring.extend([child1, child2])

    # Apply mutation
    for i in range(population_size):
        if random.random() < mutation_rate:
            mutation_point = random.randint(0, chromosome_length - 1)
            population[i] = population[i][:mutation_point] + ('0' if population[i][mutation_point] == '1' else '1') + population[i][mutation_point + 1:]

    # Replace the old population with the new offspring
    population = offspring

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(range(num_generations), average_fitness_values)
plt.xlabel('Generation')
plt.ylabel('Average Fitness')
plt.title('Average Fitness vs. Generations for Deceptive Landscape')
plt.grid(True)

# Show the plot
plt.show()
