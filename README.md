# AI-Assignment1
For all three problems, we represent solutions as binary strings of a fixed length (30 in this case). Each bit in the string represents a decision or a feature.
## 1.1 One-Max Problem
For the One-Max Problem, the fitness function calculates the fitness of a solution by counting the number of '1's in the binary string. The fitness is directly proportional to the number of '1's present in the string.
## 1.2 Evolving to a Target String
For the Evolving to a Target String problem, we define a target binary string. The fitness function calculates the fitness of a solution by counting the number of matching bits between the current binary string and the target string. The more matching bits, the higher the fitness.
## 1.3 Deceptive Landscape
For the Deceptive Landscape problem, the fitness function is modified. It counts the number of '1's in the string, but if there are no '1's present, the fitness is set to be 2 times the length of the solution. This modification creates a deceptive landscape, making it challenging for the genetic algorithm to find the optimal solution.
## Selection
We use tournament selection for selecting parents for crossover. In each generation, we randomly select a subset of individuals (tournament size = 5) and choose the fittest individual from that subset as a parent.
## Crossover
We perform one-point crossover, where two parents are selected, and a random crossover point is chosen. The children are created by swapping the bits of the parents before and after the crossover point.
## Mutation
Mutation is applied with a low probability (mutation rate = 0.01) for each bit in an individual's binary string. If mutation occurs for a bit, it is flipped (from '0' to '1' or from '1' to '0').

# Plots of Performance
## 1.1 One-Max Plotting
![Alt](https://github.com/EddieSheehy/AI-Assignment1/blob/main/partaPhotos/1.1_photo.png)

## 1.2 Evolving to a Target String Plotting
![Alt](https://github.com/EddieSheehy/AI-Assignment1/blob/main/partaPhotos/1.2_photo.png)

## 1.3 Deceptive Landscape Plotting
![Alt](https://github.com/EddieSheehy/AI-Assignment1/blob/main/partaPhotos/1.3_photo.png)

# Description of Results

## 1.1 One-Max Problem
The genetic algorithm quickly converges to the optimal solution, which is a binary string with all '1's. The average fitness increases steadily over generations, demonstrating the algorithm's effectiveness in a simple search landscape.

## 1.2 Evolving to a Target String
The algorithm successfully evolves the population to match the target binary string. The average fitness increases over generations as the algorithm finds better solutions, demonstrating its ability to search for specific patterns.

## 1.3 Deceptive Landscape
The Deceptive Landscape poses a significant challenge to the genetic algorithm. The fitness landscape is deceptive, with the optimal solution not containing any '1's. The algorithm struggles to find the optimal solution, and the average fitness remains high throughout the generations.

In summary, the genetic algorithm successfully addresses the three different optimization problems, showcasing its adaptability to different fitness landscapes. It performs well in simple problems but faces challenges in deceptive landscapes where the optimal solution is not straightforward.

# Part B
# Representation of Solutions
In the provided genetic algorithm, solutions (individuals in the population) are represented as lists of integers. Each integer in the list corresponds to a bin ID, indicating exactly which bin a particular item is placed in. For example, if there are three items and a solution is [2, 1, 2], this would mean the first and third items are placed in bin 2, while the second item is placed in bin 1.

This encoding allows for a straightforward enough representation which makes it easy to manipulate solutions during crossover and mutation. However, it requires additional processing to calculate the fitness, as the algorithm must map these bin IDs back to actual bins and also sum their contents.

# Fitness Function and Operators
The fitness function in the provided code evaluates how well a solution pairs to the constraints of the bin packing problem. It counts the number of unique bin IDs used while encouraging fewer bins used and adds penalties for any bins that exceed the maximum capacity discouraging overfilling. The fitness function is defined as:

## Selection:
The algorithm uses a tournament selection process where three individuals are randomly chosen, and the one with the best fitness is selected as a parent. This process is repeated to select another parent.

## Crossover:
With a certain probability (CROSSOVER_PROBABILITY), a single-point crossover is performed between two parents to produce two children. The crossover point is randomly chosen, and the segments of the parent solutions are swapped to create offspring.

## Mutation:
Each gene or bin ID in an offspring can be mutated with a certain probability (MUTATION_PROBABILITY). Mutation is performed by assigning a new random bin ID to an item, allowing the algorithm to explore new areas of the solution space.

# Insights into the Problem Landscape
The bin packing problem is NP-hard, meaning that it's computationally too expensive to find an optimal solution for large instances using a brute-force search. Genetic algorithms are well-suited for these types of problems as they can provide good solutions within a reasonable time frame by simulating the evolutionary process of natural selection being less expensive than brute-force search.

The fitness landscape of the bin packing problem can have many local optima because small changes to a solution can lead to significant changes in the number of bins used or the way items are distributed among bins. The genetic algorithm navigates this landscape by combining exploration (through mutation and crossover) with exploitation (by selecting the fittest individuals). This balance helps in avoiding local optima and moving towards more optimal solutions over successive generations.

However, the algorithm's performance heavily depends on its parameters, such as population size, mutation rate, and crossover probability, as well as the specific characteristics of the problem instances, like the number of items and their weights relative to the bin capacity. Fine-tuning these parameters and potentially collecting problem-specific knowledge into the operators can significantly affect the quality and convergence speed of the solutions generated by the genetic algorithm.

# Output Of Part B
![AI_Assignment_PartII_Pic](https://github.com/EddieSheehy/AI-Assignment1/assets/94063005/8fbc2eec-9c5c-40d7-a68d-bf2b0ab5bd0d)

