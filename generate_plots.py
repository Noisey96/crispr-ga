import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

if __name__ == '__main__':
    number_of_items = [5, 6, 7, 7, 8, 10, 15, 24]
    average_accuracy = [1 - ((51.0 - 51.0) / 51.0), 1 - ((150.0 - 150.0) / 150.0), 1 - ((107.0 - 107.0) / 107.0), 1 - ((1735.0 - 1735.0) / 1735.0), 1 - ((900.0 - 900.0) / 900.0), 1 - ((309.0 - 309.0) / 309.0), 1 - ((1458.0 - 1457.9) / 1458.0), 1 - ((13549094.0 - 13535570.8) / 13549094.0)]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(number_of_items, average_accuracy, color='tab:blue')
    ax.set_title("Knapsack")
    ax.ticklabel_format(style="plain")
    ax.set_xticks(number_of_items)
    ax.set_xlabel("# of Items")
    ax.yaxis.set_major_formatter(PercentFormatter(1))
    ax.set_ylabel("Average Accuracy")
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(number_of_items, average_accuracy, color='tab:blue')
    ax.set_title("Knapsack")
    ax.ticklabel_format(style="plain")
    ax.set_xticks(number_of_items)
    ax.set_xlabel("# of Items")
    ax.set_ybound(0, 1.1)
    ax.yaxis.set_major_formatter(PercentFormatter(1))
    ax.set_ylabel("Average Accuracy")
    plt.show()

    sizes = [5, 10, 15, 20, 23]
    dp_times = [0.049850000000000005, 5.977449999999999, 497.2015, 35524.901600000005, 430728.2624]
    ga_times = [2972.34775, 4886.674499999999, 6870.810650000001, 8826.12165, 10029.394900000001]
    dp_costs = [2.0379680084182166, 2.74116754204749, 3.064577470394665, 3.619913176312962, 3.9900946485758024]
    ga_costs = [2.0379680084182175, 2.7411675420474904, 3.0645774703946653, 3.619913176312962, 3.990094648575804]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(sizes, ga_times, color='tab:blue', label='GA')
    ax.plot(sizes, dp_times, color='tab:red', label='Held-Karp')
    ax.set_title("TSP")
    ax.legend()
    ax.ticklabel_format(style="plain")
    ax.set_xticks(sizes)
    ax.set_xlabel("# of Cities")
    ax.set_ylabel("Runtime in milliseconds")
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(sizes, ga_costs, color='tab:blue', label='GA')
    ax.plot(sizes, dp_costs, color='tab:red', label='Held-Karp')
    ax.set_title("TSP")
    ax.legend()
    ax.ticklabel_format(style="plain")
    ax.set_xticks(sizes)
    ax.set_xlabel("# of Cities")
    ax.set_ylabel("Solution Cost")
    plt.show()

    sizes = list(range(10, 110, 10))
    times = [4839.832450000001, 8751.881149999997, 12653.628550000001, 16474.67735, 20277.3613, 24367.35055, 28365.61965, 32403.979049999994, 36405.860349999995, 41303.83255]
    costs = [2.7411675420474904, 3.619913176312962, 4.710520377882223, 5.046832865615033, 5.600194513914297, 6.015611021694051, 6.535803406737341, 6.777443402026033, 7.3791734380163945, 8.102403661169118]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(sizes, times, color='tab:blue')
    ax.set_title("TSP with GA")
    ax.ticklabel_format(style="plain")
    ax.set_xticks(sizes)
    ax.set_xlabel("# of Cities")
    ax.set_ylabel("Runtime in milliseconds")
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(sizes, costs, color='tab:blue')
    ax.set_title("TSP with GA")
    ax.ticklabel_format(style="plain")
    ax.set_xticks(sizes)
    ax.set_xlabel("# of Cities")
    ax.set_ylabel("Solution Cost")
    plt.show()