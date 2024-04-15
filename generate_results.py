import math
import numpy
from datetime import datetime
from multiprocessing import Pool
from knapsack.dp import dp
from knapsack.generational_ga import generational_ga as knapsack_generational_ga
from tsp.held_karp import held_karp
from tsp.generational_ga import generational_ga as tsp_generational_ga

def setup_csv_tsp(filename, size):
    # grab vertices from given filename
    with open(filename, "r") as file:
        vertices = []
        for i in range(0, size):
            vertex = [float(i) for i in file.readline().strip().split(",")]
            vertices.append(vertex)

    ## generate graph from the vertices
    graph = []
    for i in range(0, len(vertices)):
        row = []
        for j in range(0, len(vertices)):
            distance = math.sqrt((vertices[i][0] - vertices[j][0]) ** 2 + (vertices[i][1] - vertices[j][1]) ** 2)
            row.append(distance)
        graph.append(row)
    return graph

def setup_tsp(filename, size):
    # grab vertices from given filename
    with open(filename, "r") as file:
        line = file.readline().strip()
        while line != "NODE_COORD_SECTION":
            line = file.readline().strip()

        vertices = []
        for i in range(0, size):
            line = file.readline().strip().split(" ")
            vertex = [float(line[1]), float(line[2])]
            vertices.append(vertex)

    print(vertices)

    ## generate graph from the vertices
    graph = []
    for i in range(0, len(vertices)):
        row = []
        for j in range(0, len(vertices)):
            distance = math.sqrt((vertices[i][0] - vertices[j][0]) ** 2 + (vertices[i][1] - vertices[j][1]) ** 2)
            row.append(distance)
        graph.append(row)
    return graph

def setup_knapsack(folder, _):
    with open("knapsack/" + folder + "/" + folder + "_c.txt", "r") as capacityFile:
        capacity = int(capacityFile.readline().strip())

    with open("knapsack/" + folder + "/" + folder + "_p.txt", "r") as pricesFile:
        prices = [int(i.strip()) for i in pricesFile.read().split("\n")]

    with open("knapsack/" + folder + "/" + folder + "_w.txt", "r") as weightsFile:
        weights = [int(i.strip()) for i in weightsFile.read().split("\n")]

    return [capacity, prices, weights]

def run_algo_once(problem, parameters, algo):
    before = datetime.now()
    solution = algo(problem, parameters)
    after = datetime.now()

    #solution = "Cost: " + str(solution) + "\n"

    print(solution)

    delta = after - before
    time = delta.total_seconds() * 1000
    return solution, time

def run_algo(problem, parameters, algo, runs):
    with Pool(5) as pool:
        result = pool.starmap(run_algo_once, [(problem, parameters, algo) for _ in range(0, runs)])
    return result

def generate_results(setup_problem, parameters, algo, sizes, input_filename, output_filename, runs = 20):
    for size in sizes:
        with open(output_filename, "a") as output_file:
            problem = setup_problem(input_filename, size)
            result = run_algo(problem, parameters, algo, runs)
            total_cost = 0
            total_time = 0
            for run in result:
                total_cost += run[0]
                total_time += run[1]
            output_file.write("\n" + input_filename + "," + str(size) + "," + algo.__name__ + "," + str(parameters) + "," + str(total_cost / runs) + "," + str(total_time / runs))

def tune_parameters(setup_problem, algo, sizes, input_filename, output_filename, runs = 20):

    popsizes = [100, 200, 300]
    maxgens = [100, 200, 300]
    elitisms = [1, 5, 10]
    tournament_sizes = [2, 5, 10]
    p_cs = [0.8, 0.9, 1.0]
    p_ms = [0.01, 0.05, 0.10]

    parameter_combinations = numpy.array(numpy.meshgrid(popsizes, maxgens, elitisms, tournament_sizes, p_cs, p_ms)).T.reshape(-1, 6)
    for parameter_combination in parameter_combinations:
        parameters = {
            "popsize": int(parameter_combination[0]),
            "maxgen": int(parameter_combination[1]),
            "elitism": int(parameter_combination[2]),
            "tournament_size": int(parameter_combination[3]),
            "p_c": parameter_combination[4],
            "p_m": parameter_combination[5],
        }
        generate_results(setup_problem, parameters, algo, sizes, input_filename, output_filename, runs)
    

if __name__ == '__main__':

    tune_parameters(setup_tsp, tsp_generational_ga, [52], "tsp/berlin52.tsp", "results_ga.csv", 5)

    #print(setup_knapsack("p01", 1))

    #generate_results(setup_tsp, tsp_generational_ga, [52], "tsp/berlin52.tsp", "results_ga.csv", 5)

    #generate_results(setup_csv_tsp, held_karp, list(range(10, 20, 10)), "tsp/medium.csv", "results.csv"))
    #generate_results(setup_csv_tsp, tsp_generational_ga, [100], "tsp/medium.csv", "results_ga.csv")
    #generate_results(setup_csv_tsp, tsp_generational_ga, [5, 10, 15, 20, 23], "tsp/medium.csv", "results_ga.csv")

    #generate_results(setup_knapsack, dp, [1], "p01",  "results_dp.csv")
    #generate_results(setup_knapsack, dp, [1], "p02",  "results_dp.csv")
    #generate_results(setup_knapsack, dp, [1], "p03",  "results_dp.csv")
    #generate_results(setup_knapsack, dp, [1], "p04",  "results_dp.csv")
    #generate_results(setup_knapsack, dp, [1], "p05",  "results_dp.csv")
    #generate_results(setup_knapsack, dp, [1], "p06",  "results_dp.csv")
    #generate_results(setup_knapsack, dp, [1], "p07",  "results_dp.csv")
    #generate_results(setup_knapsack, dp, [1], "p08",  "results_dp.csv")

    #generate_results(setup_knapsack, knapsack_generational_ga, [1], "p01", "results_ga.csv")
    #generate_results(setup_knapsack, knapsack_generational_ga, [1], "p02", "results_ga.csv")
    #generate_results(setup_knapsack, knapsack_generational_ga, [1], "p03", "results_ga.csv")
    #generate_results(setup_knapsack, knapsack_generational_ga, [1], "p04", "results_ga.csv")
    #generate_results(setup_knapsack, knapsack_generational_ga, [1], "p05", "results_ga.csv")
    #generate_results(setup_knapsack, knapsack_generational_ga, [1], "p06", "results_ga.csv")
    #generate_results(setup_knapsack, knapsack_generational_ga, [1], "p07", "results_ga.csv")
    #generate_results(setup_knapsack, knapsack_generational_ga, [1], "p08", "results_ga.csv")