# GA_Sorting-array

Genetic Algorithm to perform the sorting of a 1-D array of integers.

This algorithm performs the sorting of a vector with integers (randomly picked).

The file `Test_file.py` makes use of the Genetic Algorithm. It is composed by the functions:

1. `initial_pop` - defines the initial population. Picks up a vector and “shuffles” it to generate a random set of vectors.

2. `fitness` - evaluates the fitness of a solutions, i.e., how is the ranking of this solution compared to the right solution. In this case, the fitness function was defined to check if 2 consecutive numbers in an array, with dimension _n_, have a positive difference (ordered in crescent order), if so, an increment of +1 is given. The _exact solution_ is achieved if _n-1_ values were ordered correctly (thus _max fit = n-1_).

3. `selection_parents` - choose two parents from the population. The probability of a vector being chosen is related to his fitness (the higher the fitness, the higher the probability).

4. `crossover` - pick a random slice of parent vectors and mate them. In this case a 2-point crossover was made, in order to increase the convergence of the overall algorithm.

5. `mutation` - given a pre-defined probability, selects 2 random positions in a vector and swap them. This is a great form to introduce more variety in the population but should be used with care, otherwise it can introduce too much entropy in the solution, avoiding it to converge.

6. `new_population` - generates a new population (equivalent to perform a new iteration). The concept of elitism was introduced, which consists of introducing in the new population the 2 best solutions of the previous one. This ensures that a pattern of convergence can be observed, increasing the overall fitness between two consecutive solutions.

7. `GA_sorting` - this is the main function. It calls all the auxiliary functions and run the genetic algorithm. In the end of the overall algorithm a plot of the evolution of the best fitness for each generation is done, to have a better insight of how the algorithm runned.
