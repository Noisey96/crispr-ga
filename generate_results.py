import math
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

def run_algo_once(problem, algo):
    before = datetime.now()
    solution = algo(problem)
    after = datetime.now()

    #solution = "Cost: " + str(solution) + "\n"

    print(solution)

    delta = after - before
    time = delta.total_seconds() * 1000
    return solution, time

def run_algo(problem, algo, runs):
    with Pool(5) as pool:
        result = pool.starmap(run_algo_once, [(problem, algo) for _ in range(0, runs)])
    return result

def generate_results(setup_problem, algo, sizes, input_filename, output_filename, runs = 20):
    for size in sizes:
        with open(output_filename, "a") as output_file:
            problem = setup_problem(input_filename, size)
            result = run_algo(problem, algo, runs)
            total_cost = 0
            total_time = 0
            for run in result:
                total_cost += run[0]
                total_time += run[1]
            output_file.write("Cost: " + str(total_cost / runs) + "\n")
            output_file.write("Time: " + str(total_time / runs) + "\n")
    with open(output_filename, "a") as output_file:
        output_file.write("----" + algo.__name__ + " over " + input_filename + "----" + "\n")

if __name__ == '__main__':
    #print(setup_knapsack("p01", 1))

    generate_results(setup_tsp, tsp_generational_ga, [657], "tsp/d657.tsp", "results_ga.txt", 5)

    #generate_results(setup_csv_tsp, held_karp, list(range(10, 20, 10)), "tsp/medium.csv", "results.txt"))
    #generate_results(setup_csv_tsp, tsp_generational_ga, [100], "tsp/medium.csv", "results_ga.txt")
    #generate_results(setup_csv_tsp, tsp_generational_ga, [5, 10, 15, 20, 23], "tsp/medium.csv", "results_ga.txt")

    #generate_results(setup_knapsack, dp, [1], "p01",  "results_dp.txt")
    #generate_results(setup_knapsack, dp, [1], "p02",  "results_dp.txt")
    #generate_results(setup_knapsack, dp, [1], "p03",  "results_dp.txt")
    #generate_results(setup_knapsack, dp, [1], "p04",  "results_dp.txt")
    #generate_results(setup_knapsack, dp, [1], "p05",  "results_dp.txt")
    #generate_results(setup_knapsack, dp, [1], "p06",  "results_dp.txt")
    #generate_results(setup_knapsack, dp, [1], "p07",  "results_dp.txt")
    #generate_results(setup_knapsack, dp, [1], "p08",  "results_dp.txt")

    #generate_results(setup_knapsack, knapsack_generational_ga, [1], "p01", "results_ga.txt")
    #generate_results(setup_knapsack, knapsack_generational_ga, [1], "p02", "results_ga.txt")
    #generate_results(setup_knapsack, knapsack_generational_ga, [1], "p03", "results_ga.txt")
    #generate_results(setup_knapsack, knapsack_generational_ga, [1], "p04", "results_ga.txt")
    #generate_results(setup_knapsack, knapsack_generational_ga, [1], "p05", "results_ga.txt")
    #generate_results(setup_knapsack, knapsack_generational_ga, [1], "p06", "results_ga.txt")
    #generate_results(setup_knapsack, knapsack_generational_ga, [1], "p07", "results_ga.txt")
    #generate_results(setup_knapsack, knapsack_generational_ga, [1], "p08", "results_ga.txt")