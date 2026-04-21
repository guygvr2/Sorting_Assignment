import random
import matplotlib.pyplot as plt
import numpy as np

def generate_data(size, experiment_type):

    arr = list(range(size))     # generate some sorted array of length size

    if experiment_type == 0:    # Random (Part B)
        random.shuffle(arr)

    elif experiment_type == 1:  # 5% Noise (Part C)
        num_swaps = int(size * 0.05)
        for _ in range(num_swaps):
            idx1, idx2 = random.sample(range(size), 2)
            arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

    elif experiment_type == 2:  # 20% Noise (Part C)
        num_swaps = int(size * 0.20)
        for _ in range(num_swaps):
            idx1, idx2 = random.sample(range(size), 2)
            arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

    return arr


def save_plot(results, filename,experiment_type):     # the graphs generator func
    plt.figure(figsize=(10, 6))

    for algo_name, data in results.items():
        sizes = data["sizes"]
        means = np.array(data["means"])
        stds = np.array(data["stds"])

        # mean draw
        plt.plot(sizes, means, label=algo_name, marker='o')

        # deviation draw
        plt.fill_between(sizes, means - stds, means + stds, alpha=0.2)

    plt.xlabel('Array size (n)')
    plt.ylabel('Runtime (seconds)')

    titles = {
        0: "Runtime Comparison (Random Arrays)",
        1: "Runtime Comparison (Nearly Sorted, noise=5%)",
        2: "Runtime Comparison (Nearly Sorted, noise=20%)"
    }

    plt.title(titles.get(experiment_type, "Runtime Comparison"))
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.5)

    # save figures as 1 - without noise , 2- with noise 5%
    plt.savefig(filename)
    print(f"plot saved as {filename}")
    plt.show()
    plt.close()




