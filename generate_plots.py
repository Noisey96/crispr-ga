import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter
import math
import scipy

def graphs():
    datasets = ("PR76", "PR107", "PR124", "PR136", "PR144", "PR152", "PR226", "PR264", "PR439", "PR1002", "PR2392")
    means = {
        '0.01': (1,	0.996078431,	1,	1,	1,	1,	1,	0.995420867, 1, 1, 1),
        '0.05': (1,	1,	1,	1,	1,	1,	1,	1, 1, 1, 1),
        '0.10': (1,	0.996078431,	1,	1,	1,	1,	1,	0.995420867, 1, 1, 1),
    }

    x = np.arange(len(datasets))
    width = 0.25
    multiplier = 0

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    for attribute, measurement in means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, tick_label="test", label=attribute)
        multiplier += 1
    ax.set_title("Normal GA With Different Mutation Rates")
    ax.legend(loc="lower right")
    ax.set_xticks(x + width, datasets)
    ax.set_ylabel("Average Solution Cost")
    plt.show()

    datasets = ("PR76", "PR107", "PR124", "PR136", "PR144", "PR152", "PR226", "PR264", "PR439", "PR1002", "PR2392")
    means = {
        '0.01': (1,	0.996078431,	1,	1,	1,	1,	1,	0.995420867),
        '0.05': (1,	1,	1,	1,	1,	1,	1,	1),
        '0.10': (1,	0.996078431,	1,	1,	1,	1,	1,	0.995420867),
    }

    x = np.arange(len(datasets))
    width = 0.25
    multiplier = 0

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    for attribute, measurement in means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, tick_label="test", label=attribute)
        multiplier += 1
    ax.set_title("CRISPR GA With Different Mutation Rates")
    ax.legend(loc="lower right")
    ax.set_xticks(x + width, datasets)
    ax.set_ylabel("Average Solution Cost")
    plt.show()

    datasets = ("PR76", "PR107", "PR124", "PR136", "PR144", "PR152", "PR226", "PR264", "PR439", "PR1002", "PR2392")
    means = {
        'Normal GA': (1,	0.996078431,	1,	1,	1,	1,	1,	0.995420867),
        'CRISPR GA': (1,	1,	1,	1,	1,	1,	1,	1),
    }

    x = np.arange(len(datasets))
    width = 0.25
    multiplier = 0

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    for attribute, measurement in means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, tick_label="test", label=attribute)
        multiplier += 1
    ax.set_title("Normal GA vs CRISPR GA")
    ax.legend(loc="lower right")
    ax.set_xticks(x + width, datasets)
    ax.set_ylabel("Average Solution Cost / Optimal Cost")
    plt.show()


    cities = [76, 107, 124, 136, 144, 152, 226, 264, 439, 1002, 2392]
    ga_times = [76, 107, 124, 136, 144, 152, 226, 264, 439, 1002, 2392]
    crispr_times = [76, 107, 124, 136, 144, 152, 226, 264, 439, 1002, 2392]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(cities, ga_times, color='tab:blue', label='Normal GA')
    ax.plot(cities, crispr_times, color='tab:red', label='CRISPR GA')
    ax.set_title("Normal GA vs CRISPR GA")
    ax.legend()
    ax.ticklabel_format(style="plain")
    ax.set_xlabel("# of Cities")
    ax.set_ylabel("Average Runtime in Milliseconds")
    plt.show()

def stats():

    print("PR76")

    pr76_ga_costs = [309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309]
    pr76_crispr_costs = [309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309]

    print("GA Median")
    print(np.var(pr76_ga_costs))

    print("CRISPR Median")
    print(np.var(pr76_crispr_costs))

    print("GA vs CRISPR")
    print("%.10f (%.10f)" % scipy.stats.kruskal(pr76_ga_costs, pr76_crispr_costs))

    print("\nPR107")

    pr107_ga_costs = [309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309]
    pr107_crispr_costs = [309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309]

    print("GA Median")
    print(np.var(pr107_ga_costs))

    print("CRISPR Median")
    print(np.var(pr107_crispr_costs))

    print("GA vs CRISPR")
    print("%.10f (%.10f)" % scipy.stats.kruskal(pr107_ga_costs, pr107_crispr_costs))

    print("\nPR124")

    pr124_ga_costs = [309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309]
    pr124_crispr_costs = [309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309]

    print("GA Median")
    print(np.var(pr124_ga_costs))

    print("CRISPR Median")
    print(np.var(pr124_crispr_costs))

    print("GA vs CRISPR")
    print("%.10f (%.10f)" % scipy.stats.kruskal(pr124_ga_costs, pr124_crispr_costs))

    print("\nPR136")

    pr136_ga_costs = [309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309]
    pr136_crispr_costs = [309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309]

    print("GA Median")
    print(np.var(pr136_ga_costs))

    print("CRISPR Median")
    print(np.var(pr136_crispr_costs))

    print("GA vs CRISPR")
    print("%.10f (%.10f)" % scipy.stats.kruskal(pr136_ga_costs, pr136_crispr_costs))

    print("\nPR144")

    pr144_ga_costs = [309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309]
    pr144_crispr_costs = [309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309]

    print("GA Median")
    print(np.var(pr144_ga_costs))

    print("CRISPR Median")
    print(np.var(pr144_crispr_costs))

    print("GA vs CRISPR")
    print("%.10f (%.10f)" % scipy.stats.kruskal(pr144_ga_costs, pr144_crispr_costs))

    print("\nPR152")

    pr152_ga_costs = [309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309]
    pr152_crispr_costs = [309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309]

    print("GA Median")
    print(np.var(pr152_ga_costs))

    print("CRISPR Median")
    print(np.var(pr152_crispr_costs))

    print("GA vs CRISPR")
    print("%.10f (%.10f)" % scipy.stats.kruskal(pr152_ga_costs, pr152_crispr_costs))

    print("\nPR226")

    pr226_ga_costs = [309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309]
    pr226_crispr_costs = [309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309]

    print("GA Median")
    print(np.var(pr226_ga_costs))

    print("CRISPR Median")
    print(np.var(pr226_crispr_costs))

    print("GA vs CRISPR")
    print("%.10f (%.10f)" % scipy.stats.kruskal(pr226_ga_costs, pr226_crispr_costs))

    print("\nPR264")

    pr264_ga_costs = [309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309]
    pr264_crispr_costs = [309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309]

    print("GA Median")
    print(np.var(pr264_ga_costs))

    print("CRISPR Median")
    print(np.var(pr264_crispr_costs))

    print("GA vs CRISPR")
    print("%.10f (%.10f)" % scipy.stats.kruskal(pr264_ga_costs, pr264_crispr_costs))

    print("\nPR439")

    pr439_ga_costs = [309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309]
    pr439_crispr_costs = [309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309]

    print("GA Median")
    print(np.var(pr439_ga_costs))

    print("CRISPR Median")
    print(np.var(pr439_crispr_costs))

    print("GA vs CRISPR")
    print("%.10f (%.10f)" % scipy.stats.kruskal(pr439_ga_costs, pr439_crispr_costs))

    print("\nPR1002")

    pr1002_ga_costs = [309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309]
    pr1002_crispr_costs = [309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309]

    print("GA Median")
    print(np.var(pr1002_ga_costs))

    print("CRISPR Median")
    print(np.var(pr1002_crispr_costs))

    print("GA vs CRISPR")
    print("%.10f (%.10f)" % scipy.stats.kruskal(pr1002_ga_costs, pr1002_crispr_costs))

    print("\nPR2392")

    pr2392_ga_costs = [309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309]
    pr2392_crispr_costs = [309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309, 309]

    print("GA Median")
    print(np.var(pr2392_ga_costs))

    print("CRISPR Median")
    print(np.var(pr2392_crispr_costs))

    print("GA vs CRISPR")
    print("%.10f (%.10f)" % scipy.stats.kruskal(pr2392_ga_costs, pr2392_crispr_costs))


if __name__ == '__main__':
    graphs()
    stats()