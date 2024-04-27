import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import StrMethodFormatter
import scipy

def graphs():
    datasets = ("PR76", "PR107", "PR124", "PR136", "PR144", "PR152", "PR226", "PR264", "PR439", "PR1002", "PR2392")
    means = {
        '0.01': (411071.1741,	392950.2197,	513776.9937,	627214.996,	613359.3379,	816187.1239,	1360449.944,	865255.4789,	1653641.511,	5897989.332,	14427447.9),
        '0.05': (430121.2978,	418645.2865,	543364.26,	656714.5656,	654121.523,	841006.9861,	1425377.994,	917335.3893,	1689209.148,	6000825.896,	14570476.43),
        '0.10': (447633.7958,	426495.3842,	558572.3584,	671952.6662,	673518.0005,	871416.8573,	1451640.263,	931916.1306,	1721963.082,	6025242.17,	14615843.58),
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
    ax.yaxis.set_major_formatter(StrMethodFormatter('{x: 7.0f}'))
    ax.set_ylabel("Average Solution Cost")
    plt.show()

    datasets = ("PR76", "PR107", "PR124", "PR136", "PR144", "PR152", "PR226", "PR264", "PR439", "PR1002", "PR2392")
    means = {
        '0.01': (378402.6317,	367076.1787,	491170.4548,	607877.8173,	600323.8577,	777633.3116,	1335476.167,	875725.1361,	1635955.625,	5892733.247,	14358293.33),
        '0.05': (401016.4652,	394682.1482,	518687.9163,	647315.8159,	628472.9498,	825428.4957,	1383070.28,	906069.8257,	1675566.341,	5986156.845,	14514826.83),
        '0.10': (423956.1871,	408197.5226,	538964.2646,	661037.729,	649439.7552,	849097.2785,	1430768.503,	922859.526,	1701935.834,	6027744.199,	14624633.47),
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
    ax.yaxis.set_major_formatter(StrMethodFormatter('{x: 7.0f}'))
    ax.set_ylabel("Average Solution Cost")
    plt.show()

    datasets = ("PR76", "PR107", "PR124", "PR136", "PR144", "PR152", "PR226", "PR264", "PR439", "PR1002", "PR2392")
    means = {
        'Normal GA': (3.800619219,	8.869607469,	8.703659049,	6.481368536,	10.4781478,	11.07715757,	16.92754599,	17.6097584,	15.4233145,	22.76820372,	38.16462072),
        'CRISPR GA': (3.498577388,	8.285582888,	8.320692102,	6.281546493,	10.25545993,	10.55391156,	16.61680707,	17.82283782,	15.25836038,	22.74791348,	37.98168762),
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
    ga_times = [8639.732267,	11252.12748,	12643.75951,	13652.79563,	15018.83461,	15816.24763,	23497.89341,	28964.37576,	53769.04042,	132772.7484,	395361.016]
    crispr_times = [8915.333566,	11630.33307,	12843.29008,	14339.10381,	15605.12473,	16361.12943,	24299.09447,	30261.93442,	54563.00853,	133482.458,	393254.6753]

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

    pr76_ga_costs = [
411264.2723
, 413046.6522
, 422586.6901
, 416572.3015
, 408365.1415
, 414529.777
, 410885.2296
, 418286.6904
, 390817.707
, 404357.2796
    ]
    pr76_crispr_costs = [
362552.4555
, 379214.9908
, 357717.4737
, 376686.8716
, 385795.3522
, 388858.7524
, 390633.0269
, 391182.6142
, 370237.7607
, 381147.0188
    ]

    print("GA Median")
    print(np.median(pr76_ga_costs))

    print("CRISPR Median")
    print(np.median(pr76_crispr_costs))

    print("GA vs CRISPR")
    print("%.10f (%.10f)" % scipy.stats.kruskal(pr76_ga_costs, pr76_crispr_costs))

    print("\nPR107")

    pr107_ga_costs = [
397583.4186
, 388746.1267
, 394234.8544
, 361033.046
, 415113.3018
, 394726.7852
, 401760.4359
, 411854.9132
, 368509.6699
, 395939.6451
    ]
    pr107_crispr_costs = [
393516.9784
, 349766.0831
, 384296.0446
, 328476.6479
, 349420.3021
, 383323.1973
, 347301.6127
, 385999.553
, 387723.2894
, 360938.0782
    ]

    print("GA Median")
    print(np.median(pr107_ga_costs))

    print("CRISPR Median")
    print(np.median(pr107_crispr_costs))

    print("GA vs CRISPR")
    print("%.10f (%.10f)" % scipy.stats.kruskal(pr107_ga_costs, pr107_crispr_costs))

    print("\nPR124")

    pr124_ga_costs = [
512040.5206
, 483189.1167
, 515625.6721
, 525612.5692
, 513935.6214
, 503213.8599
, 502586.6923
, 529650.5276
, 530021.5317
, 521893.8252
    ]
    pr124_crispr_costs = [
443879.3355
, 482764.5527
, 521624.822
, 490536.6806
, 489328.5771
, 501653.3224
, 466862.1504
, 492315.6586
, 493385.1962
, 529354.2523
    ]

    print("GA Median")
    print(np.median(pr124_ga_costs))

    print("CRISPR Median")
    print(np.median(pr124_crispr_costs))

    print("GA vs CRISPR")
    print("%.10f (%.10f)" % scipy.stats.kruskal(pr124_ga_costs, pr124_crispr_costs))

    print("\nPR136")

    pr136_ga_costs = [
650648.2328
, 584371.7725
, 644574.9562
, 616505.1307
, 644616.1233
, 623338.4635
, 634345.0281
, 629079.4245
, 638370.4067
, 606300.4212
    ]
    pr136_crispr_costs = [
600479.3102
, 634472.2053
, 609678.4515
, 615525.2783
, 590460.5884
, 598827.8036
, 601396.6761
, 619455.0234
, 606802.5752
, 601680.2605
    ]

    print("GA Median")
    print(np.median(pr136_ga_costs))

    print("CRISPR Median")
    print(np.median(pr136_crispr_costs))

    print("GA vs CRISPR")
    print("%.10f (%.10f)" % scipy.stats.kruskal(pr136_ga_costs, pr136_crispr_costs))

    print("\nPR144")

    pr144_ga_costs = [
623490.8715
, 615071.2066
, 589837.6277
, 589430.6046
, 624155.7805
, 598664.1247
, 617098.881
, 622597.6905
, 627179.2659
, 626067.326
    ]
    pr144_crispr_costs = [
574514.7685
, 593482.7092
, 609095.2335
, 595982.8996
, 563037.909
, 626649.6468
, 599436.3443
, 611334.3577
, 629785.3789
, 599919.3294
    ]

    print("GA Median")
    print(np.median(pr144_ga_costs))

    print("CRISPR Median")
    print(np.median(pr144_crispr_costs))

    print("GA vs CRISPR")
    print("%.10f (%.10f)" % scipy.stats.kruskal(pr144_ga_costs, pr144_crispr_costs))

    print("\nPR152")

    pr152_ga_costs = [
820163.0305
, 835469.3192
, 816299.6333
, 807367.1512
, 824465.0862
, 815021.2827
, 824550.9622
, 812207.1021
, 796256.0491
, 810071.6228
    ]
    pr152_crispr_costs = [
799643.8749
, 777982.6098
, 768882.3436
, 747431.6145
, 786180.702
, 805555.7767
, 773870.1002
, 792608.9829
, 761644.3324
, 762532.7795
    ]

    print("GA Median")
    print(np.median(pr152_ga_costs))

    print("CRISPR Median")
    print(np.median(pr152_crispr_costs))

    print("GA vs CRISPR")
    print("%.10f (%.10f)" % scipy.stats.kruskal(pr152_ga_costs, pr152_crispr_costs))

    print("\nPR226")

    pr226_ga_costs = [
1384100.141
, 1379603.778
, 1364157.299
, 1379053.867
, 1362313.76
, 1369636.234
, 1380115.487
, 1357152.038
, 1319428.708
, 1308938.124
    ]
    pr226_crispr_costs = [
1373796.955
, 1349099.566
, 1314039.862
, 1357868.334
, 1345274.611
, 1316632.993
, 1356854.214
, 1316605.944
, 1319921.915
, 1304667.28
    ]

    print("GA Median")
    print(np.median(pr226_ga_costs))

    print("CRISPR Median")
    print(np.median(pr226_crispr_costs))

    print("GA vs CRISPR")
    print("%.10f (%.10f)" % scipy.stats.kruskal(pr226_ga_costs, pr226_crispr_costs))

    print("\nPR264")

    pr264_ga_costs = [
834129.3427
, 850470.7616
, 847366.146
, 865768.5516
, 880995.7062
, 867920.8269
, 901569.6401
, 866770.9548
, 881569.6747
, 855993.184
    ]
    pr264_crispr_costs = [
860358.9559
, 900686.1812
, 895462.2894
, 878176.834
, 896829.7045
, 875448.8315
, 889303.3426
, 828905.4888
, 879516.0409
, 852563.6918
    ]

    print("GA Median")
    print(np.median(pr264_ga_costs))

    print("CRISPR Median")
    print(np.median(pr264_crispr_costs))

    print("GA vs CRISPR")
    print("%.10f (%.10f)" % scipy.stats.kruskal(pr264_ga_costs, pr264_crispr_costs))

    print("\nPR439")

    pr439_ga_costs = [
1692514.527
, 1657198.875
, 1657960.483
, 1657959.418
, 1656244.838
, 1645058.425
, 1651601.507
, 1626410.928
, 1625510.05
, 1665956.061
    ]
    pr439_crispr_costs = [
1611020.115
, 1647768.371
, 1641187.54
, 1659333.274
, 1632068.034
, 1652367.576
, 1623015.33
, 1635701.922
, 1639506.469
, 1617587.622
    ]

    print("GA Median")
    print(np.median(pr439_ga_costs))

    print("CRISPR Median")
    print(np.median(pr439_crispr_costs))

    print("GA vs CRISPR")
    print("%.10f (%.10f)" % scipy.stats.kruskal(pr439_ga_costs, pr439_crispr_costs))

    print("\nPR1002")

    pr1002_ga_costs = [
5938253.797
, 5981924.062
, 5856216.877
, 5948259.393
, 5883201.049
, 5821798.964
, 5877596.363
, 5898590.381
, 5881096.544
, 5892955.896
    ]
    pr1002_crispr_costs = [
6007850.953
, 5899140.151
, 5922317.123
, 5795766.972
, 5834218.961
, 5863743.321
, 5852742.869
, 5949260.974
, 5874450.937
, 5927840.205
    ]

    print("GA Median")
    print(np.median(pr1002_ga_costs))

    print("CRISPR Median")
    print(np.median(pr1002_crispr_costs))

    print("GA vs CRISPR")
    print("%.10f (%.10f)" % scipy.stats.kruskal(pr1002_ga_costs, pr1002_crispr_costs))

    print("\nPR2392")

    pr2392_ga_costs = [
14446161.03
, 14477410.96
, 14315506.74
, 14536279.59
, 14429376.57
, 14461853.91
, 14458162
, 14408449.42
, 14323602.95
, 14417675.82
    ]
    pr2392_crispr_costs = [
14408599.75
, 14392869.2
, 14377773.18
, 14471099.06
, 14339758.45
, 14380725.72
, 14378820.02
, 14265816.86
, 14317212.65
, 14250258.44
    ]

    print("GA Median")
    print(np.median(pr2392_ga_costs))

    print("CRISPR Median")
    print(np.median(pr2392_crispr_costs))

    print("GA vs CRISPR")
    print("%.10f (%.10f)" % scipy.stats.kruskal(pr2392_ga_costs, pr2392_crispr_costs))


if __name__ == '__main__':
    graphs()
    stats()