import math
import numpy
import xml.etree.ElementTree as ET
from datetime import datetime
from multiprocessing import Pool
from knapsack.dp import dp
from knapsack.generational_ga import generational_ga as knapsack_generational_ga
from tsp.held_karp import held_karp
import tsp.generational_ga as ga

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

def setup_xml_tsp(filename):
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Find the graph element
    graph_element = root.find('.//graph')

    # Find the number of vertices
    num_vertices = len(graph_element)

    # Initialize an empty matrix
    distance_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    # Fill the matrix with edge costs
    vertex_count = 0
    for vertex in graph_element:
        edges = vertex.findall('./edge')
        for edge in edges:
            target_vertex_index = int(edge.text)
            cost = edge.get('cost')
            distance_matrix[vertex_count][target_vertex_index] = float(cost)
        vertex_count += 1

    return distance_matrix

def setup_tsp(filename):
    # grab vertices from given filename
    with open(filename, "r") as file:
        line = file.readline().strip()
        while line != "NODE_COORD_SECTION":
            line = file.readline().strip()

        vertices = []
        line = file.readline().strip().split(" ")
        while line[0] != "EOF":
            vertex = [float(line[1]), float(line[2])]
            vertices.append(vertex)
            line = file.readline().strip().split(" ")

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

def run_algo(problem, parameters, algo, input_filename, output_filename, str_parameters):
    before = datetime.now()
    cost = algo(problem, parameters)
    after = datetime.now()
    delta = after - before
    time = delta.total_seconds() * 1000

    with open(output_filename, "a") as output_file:
        # Problem,Size,Algorithm,Parameters,Cost,Time
        output_file.write("\n" + input_filename + "," + str(len(problem)) + "," + algo.__name__ + "," + str_parameters + "," + str(cost) + "," + str(time))

def run_batch(setup_problem, parameters, algo, input_filename, output_filename, runs = 20):
    arr_parameters = []
    for key in parameters.keys():
        if callable(parameters.get(key)):
            arr_parameters.append(key + ": " + str(parameters.get(key).__name__))
        else:  
            arr_parameters.append(key + ": " + str(parameters.get(key)))
    str_parameters = ";".join(arr_parameters)

    problem = setup_problem(input_filename)
    with Pool(5) as pool:
        pool.starmap(run_algo, [(problem, parameters, algo, input_filename, output_filename, str_parameters) for _ in range(0, runs)])

def tune_parameters(setup_problem, algo, input_filename, output_filename, runs = 20):
    popsizes = [100]
    maxgens = [10000]
    elitisms = [1]
    tournament_sizes = [2]
    p_cs = [1]
    p_ms = [0.10]

    parameter_combinations = numpy.array(numpy.meshgrid(popsizes, maxgens, elitisms, tournament_sizes, p_cs, p_ms)).T.reshape(-1, 6)
    for parameter_combination in parameter_combinations:
        parameters = {
            "popsize": int(parameter_combination[0]),
            "maxgen": int(parameter_combination[1]),
            "elitism": int(parameter_combination[2]),
            "tournament_size": int(parameter_combination[3]),
            "p_c": parameter_combination[4],
            "p_m": parameter_combination[5],
            "generate_initial_generation": ga.closest_neighbor_gen,
            "fitness_function": ga.fitness_function,
            "parent_selection": ga.tournament_selection,
            "recombination_operator": ga.edge_recombination_crossover,
            "mutation_operator": ga.simple_inversion_mutation,
        }
        run_batch(setup_problem, parameters, algo, input_filename, output_filename, runs)
    

if __name__ == '__main__':

    #tune_parameters(setup_tsp, tsp_generational_ga, [52], "tsp/berlin52.tsp", "results_ga.csv", 20)
    tune_parameters(setup_xml_tsp, ga.generational_ga, "tsp/brazil.xml", "results_ga.csv", 1)

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