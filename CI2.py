#Optimization of genetic algorithm parameter in hybrid genetic algorithm-neural network modelling: Application to spray drying of coconut milk.
#use iris dataset

import numpy as np
import pandas as pd
import random
import warnings 
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

warnings.filterwarnings('ignore')

data = pd.read_csv(r"C:\Users\Public\Iris.csv")
if 'Id' in data.columns:
    data=data.drop('Id',axis=1)
    
x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

le=LabelEncoder()
y=le.fit_transform(y)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

pop_size=6
gens=5
mutation_rate=0.1

def create_chromosomes():
    return[random.randint(5,20),random.uniform(0.001,0.1)]

def fitness(chromosome):
    hidden_size=chromosome[0]
    lr=chromosome[1]
    
    model=MLPClassifier(
        hidden_layer_sizes=(hidden_size,),
        learning_rate_init=lr,
        max_iter=200
    )
    
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    
    return accuracy_score(y_test,y_pred)

def selection(population):
    population=sorted(population,key=lambda x:fitness(x),reverse=True)
    return population[:2]

def crossover(p1,p2):
    return [p1[0],p2[1]]

def mutation(chromosome):
    if random.random() < mutation_rate :
        chromosome[0] = random.randint(5,20)
    if random.random() < mutation_rate :
        chromosome[1] = random.uniform(0.001,0.1)
    return chromosome

population = [create_chromosomes() for _ in range (pop_size)]

for gen in range(gens):
    print(f'\nGeneration {gen+1} :')
    for chrom in population :
        print('Chromosome :',chrom,'Accuracy :',fitness(chrom))
    parents=selection(population)
    new_population = parents.copy()
    while len(new_population) < pop_size :
        child=crossover(parents[0],parents[1])
        child=mutation(child)
        new_population.append(child)
    population=new_population
    
best=selection(population)[0]
print('\nBest Parameters Found :')
print('Hidden Layers Size :',best[0])
print('Learning Rate :',best[1])
print('Accuracy :',fitness(best))
