#Implement DEAP (Distributed Evolutionary Algorithms) using Python.

import random 
from deap import base , creator , tools , algorithms

creator.create('FitnessMax',base.Fitness,weights=(1.0,))
creator.create('Individual',list,fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register('attr_float',random.uniform,-10,10)
toolbox.register('individual',tools.initRepeat,creator.Individual,toolbox.attr_float,1)
toolbox.register('population',tools.initRepeat,list,toolbox.individual)

def eval_func(individual):
    x=individual[0]
    return (x*x,)
toolbox.register('evaluate',eval_func)

toolbox.register('mate',tools.cxBlend,alpha=0.5)
toolbox.register('mutate',tools.mutGaussian,mu=0,sigma=1,indpb=0.2)
toolbox.register('select',tools.selTournament,tournsize=3)

population = toolbox.population(n=6)
gens=5

for gen in range(gens):
    print(f'\nGeneration {gen+1} :')
    for ind in population :
        ind.fitness.values = toolbox.evaluate(ind)
        print(ind,ind.fitness.values)
    
    offspring = toolbox.select(population,len(population))
    offspring = list(map(toolbox.clone,offspring))
    
    for i in range(0,len(offspring),2):
        if i+1 < len(offspring):
            toolbox.mate(offspring[i],offspring[i+1])
    for ind in offspring:
        toolbox.mutate(ind)
        
    population = offspring
    
best=tools.selBest(population,1)[0]
print('\nBest Solution :',best)
print('Best Fitness :',best.fitness.values)
