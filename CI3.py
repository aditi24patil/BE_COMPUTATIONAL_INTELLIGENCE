#Implementation of Clonal selection algorithm using Python.
import random 
def fitness(x):
    return x*x

def create_population(size):
    return[random.uniform(-10,10) for _ in range(size)]

def selection(population):
    return sorted(population,key=fitness,reverse=True)[:3]

def cloning(selected):
    clones=[]
    for i,val in enumerate(selected):
        num_clones=(3-i)*2
        for _ in range(num_clones):
            clones.append(val)
    return clones

def mutation(clones):
    mutated=[]
    for val in clones:
        new_val = val + random.uniform(-1,1)
        mutated.append(new_val)
    return mutated

pop_size = 6
gens = 5

population=create_population(pop_size)

for gen in range(gens):
    print(f'\nGeneration {gen+1} :')
    print('Population :',population)
    selected=selection(population)
    clones=cloning(selected)
    mutated=mutation(clones)
    population = selected + mutated[:pop_size - len(selected)]

for ind in population:
    ind.fitness.values = toolbox.evaluate(ind)

best=max(population,key=fitness)
print('\nBest Solution :',best)
print('Best Fitness :',fitness(best))
