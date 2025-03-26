import os
import json
import argparse
import random; random.seed(42)
from tqdm import tqdm

import sort
import comparator

def arange(start, stop, step):
    return [start + i * step for i in range(int((stop - start) / step))]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sweep over a range of values.")
    parser.add_argument("--sort", type=str, required=True, help="The sorting algorithm to use.")
    parser.add_argument("--comparator", type=str, required=True, help="The comparator to use.")
    
    parser.add_argument("--num_trials", type=int, required=True, help="The number of trials to run.")
    parser.add_argument("--num_values", type=int, required=True, help="The number of values to sort.")
    
    parser.add_argument("--sigma_min", type=float, default=0.0, help="The minimum sigma value to sweep.")
    parser.add_argument("--sigma_max", type=float, default=1.0, help="The maximum sigma value to sweep.")
    parser.add_argument("--width_min", type=float, default=0.0, help="The minimum width value to sweep.")
    parser.add_argument("--width_max", type=float, default=1.0, help="The maximum width value to sweep.")
    parser.add_argument("--step_size", type=float, default=0.01, help="The step size for the sweep.")

    parser.add_argument("--output_dir", type=str, default="outputs", help="The output directory to save the results.")
    args = parser.parse_args()

    arrays = [[random.uniform(0, 1) for _ in range(args.num_values)] for _ in range(args.num_trials)]

    outputs = {}
    if args.comparator == 'gaussian':
        for sigma in tqdm(arange(args.sigma_min, args.sigma_max, args.step_size), desc="Sweeping sigma"):
            outputs[sigma] = []
            #import pdb; pdb.set_trace()
            comp = comparator.comparator(args.comparator, sigma=sigma)
            for trial in range(args.num_trials):
                sorted_array = sort.sort(arrays[trial], args.sort, comp)
                outputs[sigma].append(sorted_array)
    elif args.comparator == 'uniform':
        for width in tqdm(arange(args.width_min, args.width_max, args.step_size), desc="Sweeping width"):
            outputs[width] = []
            comp = comparator.comparator(args.comparator, width=width)
            for trial in range(args.num_trials):
                sorted_array = sort.sort(arrays[trial], args.sort, comp)
                outputs[width].append(sorted_array)
    elif args.comparator == 'oracle':
        outputs['0.0'] = []
        outputs['1.0'] = []
        comp = comparator.comparator(args.comparator)
        for trial in range(args.num_trials):
            sorted_array = sort.sort(arrays[trial], args.sort, comp)
            outputs['0.0'].append(sorted_array)
            outputs['1.0'].append(sorted_array)
    else:
        raise ValueError("Invalid comparator")

    output_path = os.path.join(args.output_dir, f"{args.sort}_{args.comparator}.json")
    print(f"Saving outputs to {output_path}")
    with open(output_path, 'w') as f:
        json.dump(outputs, f, indent=1)