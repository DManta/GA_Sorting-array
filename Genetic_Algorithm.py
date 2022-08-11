###############################################################################
#Packages

import numpy as np
import random
import matplotlib.pyplot as plt

###############################################################################
#Functions

#1. Define the initial population..............................................

def initial_pop(ini_elem, pop_size):
    np.random.shuffle(ini_elem) #shuffle elements
    pop = [ini_elem]
    
    for i in range(pop_size-1):
        elem = ini_elem.copy() 
        np.random.shuffle(elem) #shuffle elements
        pop = np.append(pop,[elem], axis=0) #increase the population
    return pop

#2. Define the fitness function................................................
#   Note: I assumed that the elements in the vector are sequential

def fitness(elem):
    max_fit = len(elem)-1 #maximum fitness possible (solution)
    fit = 0
    
    for i in range(0,len(elem)-1):
        if elem[i+1]-elem[i] == 1: #check if the values are ordered
            fit += 1

    return fit/max_fit #normalized

#3. Selection of the parents...................................................

def selection_parents(pop, fitness_pop):
    
    #Picks 2 entries based on the fitness (higher probability of being chosen)
    if max(fitness_pop) == 0: #could happen for a small set
        parent1, parent2 = pop[0], pop[1]
    else: #This function requires at least 1 "fitness_pop" > 0
        parent1, parent2 = random.choices(pop, weights = fitness_pop, k = 2)
        
    return parent1, parent2

#4. Crossover..................................................................
#   Note: I decided to do a 2 point crossover, because with a single point the
#         solution was not very good

def crossover(parent1,parent2):
    #pick 2 random positions
    p =  np.random.randint(len(parent1)) 
    k =  np.random.randint(len(parent1))
    
    #Slice of parent 1 and a slice of parent 2
    if p <= k: #If the value is the same, the array as only 1 entry
        child1 = np.copy(parent1[p:k]) 
        child2 = np.copy(parent2[p:k])
    
    else: #p > k
        child1 = np.copy(parent1[k:p])
        child2 = np.copy(parent2[k:p])

    for i in range(len(parent1)):    #parents have the same length
        if parent2[i] not in child1: #ensure child as only different values
            child1 = np.append(child1,parent2[i])
            
        if parent1[i] not in child2: #ensure child as only different values
            child2 = np.append(child2,parent1[i])
            
    return child1, child2

#5. Mutation...................................................................
#   Get 2 random positions and swap them

def mutation(elem):     
    p = np.random.randint(len(elem))
    k =  np.random.randint(len(elem))
    
    elem[p], elem[k] = elem[k], elem[p] #swap positions
    
    return elem

#6. Generate a new population..................................................

def new_population(pop, fitness_pop, M):
    
    pop_size = len(pop)

    count = 0
    while count < pop_size :
        
        if count == 0:
            count += 2
            
            #To improve the performance, and assure a good convergence, I
            #decided to perform elitism. In this case, the best 2 parents are
            #kept for the next generation.
            
            #1st best solution
            index_max = fitness_pop.index(max(fitness_pop)) 
            best_sol = pop[index_max]
            
            #2nd best sol 
            search_index = [i for i in range(pop_size)]
            search_index.remove(index_max) #remove the 1st best from pop
            pop2 = [pop[i] for i in search_index] #pop without the 1st best
            fitness_pop2 = [fitness(i) for i in pop2]
            index_max2 = fitness_pop2.index(max(fitness_pop2))
            best_sol2 = pop2[index_max2] #2nd best sol 
            
            if np.random.rand() < M: #aply a mutation, to assure diversity
                best_sol = mutation(best_sol)
                best_sol2 = mutation(best_sol2)
                
            new_pop = np.append([best_sol],[best_sol2], axis=0)
                    
        parent1, parent2 = selection_parents(pop, fitness_pop) #select parents
        child1, child2 = crossover(parent1,parent2) #crossover -> childs
        
        if np.random.rand() < M: #aply a mutation, to assure diversity
            child1 = mutation(child1)
            child2 = mutation(child2)
        
                 
        elif count == pop_size-1 and (pop_size % 2) != 0:
            #pop_size is odd, the last child cannot enter
            #choosed child1, but could be 1, 2 or the fittest
            
            count +=1  
            new_pop = np.append(new_pop,[child1], axis=0) 
    
        else: #pop_size is even and new_pop is not complete yet
            count += 2
            new_pop = np.append(new_pop,[child1,child2], axis=0)
            
    return new_pop

#7. Main function..............................................................
#   Receive the inputs and perform the analysis

def GA_sorting(a_size, pop_size, M, gen_max):
    
    #Return some exceptions of the algorithm
    if a_size < 2: 
        return print("Please choose a_size >= 2")
    elif pop_size < 2:
        return print("Please choose pop_size >= 2")
    
    gen = 0
    
    ini_elem = [i for i in range(a_size)] #initial set
    
    pop = initial_pop(ini_elem, pop_size) #Generate the initial population

    fitness_pop = [fitness(i) for i in pop] #Check the fitness of population
    
    print("gen =", gen, "\n", "max_fit =", max(fitness_pop))
    
    plot_gen = [gen]
    plot_fit = [max(fitness_pop)]
    
    #The loop keeps runing until the solution is found or gen_max is achieved
    while max(fitness_pop) != 1 and gen < gen_max:
        gen +=1
        
        #new generation
        pop = new_population(pop, fitness_pop, M)
        
        #chech the fitness of new gen
        fitness_pop = [fitness(i) for i in pop] 
        
        print("gen =", gen, "\n", "max_fit =", max(fitness_pop))
        
        index_max = fitness_pop.index(max(fitness_pop)) 
        best_sol = pop[index_max] #Best solution    
        
        #Trace the evolution of solution
        plot_gen = np.append(plot_gen,gen)
        plot_fit = np.append(plot_fit,max(fitness_pop))
        

    #Solution
    #Check the fitness of the population
    fitness_pop = [fitness(i) for i in pop]
    index_max = fitness_pop.index(max(fitness_pop)) 
    best_sol = pop[index_max] #Best solution
    
    #Print solution
    print("Intial vector= ", ini_elem)
    print("Sorted vector = ", best_sol)

    #Plot the evolution
    plt.plot(plot_gen,plot_fit)
    plt.title("GA sorting: a_size = {0}, pop_size = {1}, M = {2}".format(a_size, pop_size, M))
    plt.xlabel("Generation"), plt.ylabel("Best fitness")
    plt.ylim([0,1])
    plt.show()