###############################################################################
#Import the Genetic Algorithm functions
from Genetic_Algorithm import GA_sorting

###############################################################################
#Genetic Algorithm to perform the sorting of a 1-D array of integers
#This algoritm perform the sorting of a vector with integers (randomly picked) 

#Input parameters..............................................................

a_size = 10      #input: Length of the array to sort
pop_size = 5     #input: Population size (dimension of the set of arrays)
M = 0.01         #input: [0,1] = probability of mutations
gen_max = 2000   #input: maximum number of generations (maximum iterations)

#..............................................................................

#run the algorithm and return the results

GA_sorting(a_size, pop_size, M, gen_max)