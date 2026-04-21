import argparse
import utils
from sorting import ALGO_MAP
import time
import numpy as np




def run_experiment(algo_ids, sizes, experiment_type, repetitions):
    results = {}

    for algo_id in algo_ids:
        algo_name, algo_func = ALGO_MAP[algo_id]
        results[algo_name] = {"sizes": [], "means": [], "stds": []}

        for size in sizes:
            times = []
            for _ in range(repetitions):
                # generate different data for every size
                data = utils.generate_data(size, experiment_type)

                # calculate running times
                start_time = time.perf_counter()
                algo_func(data)
                end_time = time.perf_counter()

                times.append(end_time - start_time)

            # Statistics analysis
            results[algo_name]["sizes"].append(size)
            results[algo_name]["means"].append(np.mean(times))
            results[algo_name]["stds"].append(np.std(times))    #standard deviation

            print(f"Finished {algo_name} for size {size}")

    return results




def main():
    parser = argparse.ArgumentParser(description="Sorting Algorithms Experiment")

    # arguments settings
    parser.add_argument("-a", nargs="+", type=int, help="Algorithm IDs (1-5)")
    parser.add_argument("-s", nargs="+", type=int, help="Array sizes")
    parser.add_argument("-e", type=int, help="Experiment type: 1 (5%% noise), 2 (20%% noise), etc.")
    parser.add_argument("-r", type=int, default=10, help="Number of repetitions")

    args = parser.parse_args()

    # check user selection
    if args.a and args.s:
        # experiment type 0 - random arrays , 1 - nearly sorted arrays (5% noise) , 2 - nearly sorted arrays (20% noise)
        exp_type = args.e if args.e is not None else 0
        experiment_results = run_experiment(args.a, args.s, exp_type, args.r)
        if exp_type == 0:
            filename = "result1.png"
        else:
            filename = "result2.png"
        utils.save_plot(experiment_results, filename, exp_type)


if __name__ == '__main__':
    main()