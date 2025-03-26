import os
import json
import argparse
import scipy.stats
import numpy as np
import matplotlib.pyplot as plt

def pearson(arr):
    sorted_arr = sorted(arr)
    return scipy.stats.pearsonr(arr, sorted_arr)[0]

def spearman(arr):
    return scipy.stats.spearmanr(arr, range(len(arr)))[0]

def kendall(arr):
    ranks = scipy.stats.rankdata(arr)
    sorted_ranks = sorted(ranks)
    return scipy.stats.kendalltau(ranks, sorted_ranks)[0]

def pairs(arr):
    inversion_count = 0
    total_count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversion_count += 1
            total_count += 1
    return 1 - (inversion_count / total_count)

def bootstrap_std(arr, num_samples=1000):
    means = []
    for _ in range(num_samples):
        sample = np.random.choice(arr, len(arr), replace=True)
        means.append(np.mean(sample))
    return np.std(means)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create plot for Gaussian comparator.")
    parser.add_argument("--input_dir", type=str, default="outputs", help="The input directory to load the results.")
    parser.add_argument("--comparator", type=str, required=True, help="The comparator to use.")
    parser.add_argument("--metrics", type=str, nargs="+", default=["pearson", "spearman", "kendall", "pairs"], help="The metrics to evaluate.")
    parser.add_argument("--output_dir", type=str, default="plots", help="The output directory to save the plots.")
    args = parser.parse_args()

    results = {}
    for filename in sorted(os.listdir(args.input_dir)):
        sort, comparator = filename.split('.')[0].split('_')
        if comparator == args.comparator:
            with open(os.path.join(args.input_dir, filename), 'r') as f:
                results[sort] = json.load(f)
    
    for metric in args.metrics:
        plt.figure(figsize=(12, 8))
        for sort, sweep_results in results.items():
            x, y, y_err = [], [], []
            for sigma, values in sweep_results.items():
                x.append(float(sigma))
                trial_outputs = [globals()[metric](trial_output) for trial_output in values]
                y.append(np.mean(trial_outputs))
                y_err.append(bootstrap_std(trial_outputs))
            x = np.array(x)
            y = np.array(y)
            y_err = np.array(y_err)
            plt.plot(x, y, label=sort)
            plt.fill_between(x, y - 2*y_err, y + 2*y_err, alpha=0.2)
        plt.title(f"{args.comparator.capitalize()} Noise Model: {metric.capitalize()}", fontsize=20)

        if comparator == "gaussian":
            plt.xlabel("Sigma", fontsize=16)
        elif comparator == "uniform":
            plt.xlabel("Width/2", fontsize=16)

        plt.ylabel(metric.capitalize(), fontsize=16)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.grid(axis='y')
        plt.legend(fontsize=14)

        output_path = os.path.join(args.output_dir, args.comparator, f"{metric}.png")
        print(f"Saving plot to {output_path}")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        plt.savefig(os.path.join(args.output_dir, args.comparator, f"{metric}.png"), bbox_inches='tight', dpi=300)
