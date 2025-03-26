## Which sorting algorithm is most robust to noisy comparisons?
I was wondering about this and I had some time to spare, so I coded up a simulation that benchmarks some popular sorting algorithms under $Gaussian$ and $Uniform$ noise models. 

Specifically, I sorted 100-sized lists of numbers drawn from $Uniform(0,1)$ using different sorting algorithms, conducting 100 independent trials for each algorithm while simulating noisy comparisons under Gaussian and Uniform noise models (for various values of noise stddev).

### So what did I find?
Nice curves. Some algorithms are **much** more sensitive to noise than others, wow.

<img src="https://github.com/anirudhajith/robust-sorting/blob/main/plots/gaussian/pearson.png" width="400"><img src="https://github.com/anirudhajith/robust-sorting/blob/main/plots/gaussian/pairs.png" width="400">
<img src="https://github.com/anirudhajith/robust-sorting/blob/main/plots/uniform/pearson.png" width="400"><img src="https://github.com/anirudhajith/robust-sorting/blob/main/plots/uniform/pairs.png" width="400">

It appears the ranking of these algorithms from best to worst in terms of their robustness to noise is pretty (cough... cough..) robust to the specific choice of noise model and looks like
1. [Cocktail shaker sort](https://en.wikipedia.org/wiki/Cocktail_shaker_sort)
2. [Shellsort](https://en.wikipedia.org/wiki/Shellsort)
3. [Bubble sort](https://en.wikipedia.org/wiki/Bubble_sort)
4. [Merge sort](https://en.wikipedia.org/wiki/Merge_sort)
5. [Quicksort](https://en.wikipedia.org/wiki/Quicksort)
6. [Heapsort](https://en.wikipedia.org/wiki/Heapsort)
7. [Selection sort](https://en.wikipedia.org/wiki/Selection_sort)
8. [Insertion sort](https://en.wikipedia.org/wiki/Insertion_sort)

### Thoughts
Notice that the list begins with a few $O(n^2)$ algorithms, followed by the $O(n \log{n})$ algorithms, and finally ends with some more $O(n^2)$ algorithms. I wonder if there exists an $O(n \log{n})$ algorithm that's at least as robust as the top-performing $O(n^2)$ ones, or if this increased sensitivity provably persists in any algorithm that runs in $O(n \log{n})$.
