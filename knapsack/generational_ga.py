import random
import math

def penalty_function(problem, generation):
    [capacity, prices, weights] = problem

    fitnesses = []
    for gene in generation:
        total_weight = 0
        total_price = 0
        for j in range(len(gene)):
            if gene[j]:
                total_weight += weights[j]
                total_price += prices[j]
        if total_weight > capacity:
            fitness = 0
        else:
            fitness = total_price
        fitnesses.append(fitness)
    return fitnesses

def tournament_selection(fitnesses, tournament_size):
    parent_indices = set()
    while len(parent_indices) < 2:
        tournament = []
        for _ in range(tournament_size):
            tournament.append(math.floor(random.uniform(0, len(fitnesses))))
        
        max_fitness = float("-inf")
        for participant in tournament:
            if max_fitness < fitnesses[participant]:
                parent_index = participant
                max_fitness = fitnesses[participant]
        parent_indices.add(parent_index)
    
    return list(parent_indices)
            
def uniform_crossover(parent_1, parent_2):
    child_1 = []
    child_2 = []
    for i in range(len(parent_1)):
        if random.uniform(0, 1) < 0.5:
            child_1.append(parent_2[i])
            child_2.append(parent_1[i])
        else:
            child_1.append(parent_1[i])
            child_2.append(parent_2[i])
    return child_1, child_2

def bit_flip(gene, p_m):
    for i in range(len(gene)):
        if random.uniform(0, 1) < p_m:
            if gene[i] == 1:
                gene[i] = 0
            else:
                gene[i] = 1
    return gene

def generate_initial_generation(popsize, genesize):
    initial_generation = []

    for _ in range(popsize):
        gene = []
        for _ in range(genesize):
            if random.uniform(0, 1) < 0.5:
                gene.append(1)
            else:
                gene.append(0)
        initial_generation.append(gene)
    return initial_generation

def determine_n_best(list, n):
    local_list = list.copy()

    indices = []
    for _ in range(n):
        max_element = float("-inf")
        for i in range(len(local_list)):
            if local_list[i] > max_element:
                index = i
                max_element = local_list[i]
        local_list[index] = float("-inf")
        indices.append(index)
    return indices

def generational_ga(problem):
    [_, prices, _] = problem

    parameters = {
        "popsize": 100,
        "maxgen": 1000,
        "fitness_function": penalty_function,
        "elitism": 10,
        "parent_selection": tournament_selection,
        "tournament_size": 10,
        "recombination_operator": uniform_crossover,
        "mutation_operator": bit_flip,
        "p_m": 0.10,
    }

    current_generation = generate_initial_generation(parameters["popsize"], len(prices))
    for i in range(parameters["maxgen"]):
        fitnesses = parameters["fitness_function"](problem, current_generation)

        next_generation = []
        elites = determine_n_best(fitnesses, parameters["elitism"])
        for elite in elites:
            next_generation.append(current_generation[elite])

        while len(next_generation) < len(current_generation):
            [parent_1_index, parent_2_index] = parameters["parent_selection"](fitnesses, parameters["tournament_size"])   
            child_1, child_2 = parameters["recombination_operator"](current_generation[parent_1_index], current_generation[parent_2_index])
            child_1 = parameters["mutation_operator"](child_1, parameters["p_m"])
            child_2 = parameters["mutation_operator"](child_2, parameters["p_m"])
            next_generation.extend([child_1, child_2])
        current_generation = next_generation
        
    fitnesses = parameters["fitness_function"](problem, current_generation)

    solution_index = determine_n_best(fitnesses, 1)[0]

    total_price = 0
    for i in range(len(current_generation[solution_index])):
        if current_generation[solution_index][i]:
            total_price += prices[i]
    return total_price
    
            
if __name__ == '__main__':
    problem = [6404180, [825594, 1677009, 1676628, 1523970, 943972, 97426, 69666, 1296457, 1679693, 1902996, 1844992, 1049289, 1252836, 1319836, 953277, 2067538, 675367, 853655, 1826027, 65731, 901489, 577243, 466257, 369261], [382745, 799601, 909247, 729069, 467902, 44328, 34610, 698150, 823460, 903959, 853665, 551830, 610856, 670702, 488960, 951111, 323046, 446298, 931161, 31385, 496951, 264724, 224916, 169684]]
    solution = generational_ga(problem)
    print(solution)
