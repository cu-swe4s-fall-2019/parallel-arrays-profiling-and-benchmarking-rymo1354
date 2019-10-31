# Hash tables
Testing different hash functions and search methods. 
Note: random and non-random strings used for hashing. 

## Travis Status
![](https://travis-ci.com/cu-swe4s-fall-2019/hash-tables-rymo1354.svg?branch=master)

## Installation
To use this package, you should have [Python3](https://www.python.org/download/releases/3.6/) in your environment. You should also have matplotlib installed.

## Utilized Packages
* pycodestyle
* matplotlib

## Usage
`scatter.py` is the main program used to generate plots from the hash function and search method distributions. It uses `hash_functions.py` and `hash_methods.py` to generate these plots. Examples of plots are shown in the `plots` folder.

All plots are generated using the following command:
`bash benchmark.sh`
This generates the plots in the `plots` folder. 

Note: `binning` and `weighted` hash functions were plotted for EXTRA CREDIT.

### Hash Function Plots
Arguments include:
* input: name of input file, i.e. rand_words.txt, non_rand_words.txt (INPUT)
* hash_method: the method of hashing, i.e. ascii, rolling, etc. (HASH_METHOD)
* table_size: size of hash table (TABLE_SIZE)
* out_file: name of plot, i.e. output file (OUT_FILE)

Format is:
```
python hash_functions.py --input INPUT --hash_method HASH_METHOD --table_size TABLE_SIZE | python scatter.py --out_file 'OUT_FILE' --x_label "Hashed Word" --y_label "Hashed Value"
```
#### INPUT = rand_words.txt, HASH_METHOD = ascii
![](plots/ascii_random.png)

#### INPUT = rand_words.txt, HASH_METHOD = rolling
![](plots/rolling_random.png)   

#### INPUT = rand_words.txt, HASH_METHOD = binning
![](plots/binning_random.png)   

#### INPUT = rand_words.txt, HASH_METHOD = weighted
![](plots/weighted_random.png)

#### INPUT = non_rand_words.txt, HASH_METHOD = ascii
![](plots/ascii_nonrandom.png)             
 
#### INPUT = non_rand_words.txt, HASH_METHOD = rolling
![](plots/rolling_nonrandom.png) 
 
#### INPUT = non_rand_words.txt, HASH_METHOD = binning
![](plots/binning_nonrandom.png) 
 
#### INPUT = non_rand_words.txt, HASH_METHOD = weighted
![](plots/weighted_nonrandom.png)    

### Results

As you can see, the rolling hash is the best performing hash across both random and nonrandom words. While the binning hash performs decently well for random words, it performs quite poorly for nonrandom words. The ascii and weighted hashes both perform poorly for random and nonrandom words. 

### Chained Hash and Linear Probing
These files are generated using `benchmark.sh`. The exact syntax for the generation of these plots can be found in `benchmark.sh` under "Linear probing from rand_words.txt", "Linear probing from non_rand_words.txt", "Chain hash from rand_words.txt", and "Chain hash from non_rand_words.txt". A select few plots are shown below: 

### ASCII HASH

#### INPUT = rand_words.txt, HASH_METHOD = ascii, COLLISION_METHOD = linear
![](plots/ascii_linear_rand_add_time.png)
![](plots/ascii_linear_rand_search_time.png)

#### INPUT = rand_words.txt, HASH_METHOD = ascii, COLLISION_METHOD = chain
![](plots/ascii_chain_rand_add_time.png)
![](plots/ascii_chain_rand_search_time.png)

#### INPUT = non_rand_words.txt, HASH_METHOD = ascii, COLLISION_METHOD = linear
![](plots/ascii_linear_nonrand_add_time.png)
![](plots/ascii_linear_nonrand_search_time.png)

#### INPUT = non_rand_words.txt, HASH_METHOD = ascii, COLLISION_METHOD = chain
![](plots/ascii_chain_nonrand_add_time.png)
![](plots/ascii_chain_nonrand_search_time.png)

### ROLLING HASH

#### INPUT = rand_words.txt, HASH_METHOD = rolling, COLLISION_METHOD = linear
![](plots/rolling_linear_rand_add_time.png)
![](plots/rolling_linear_rand_search_time.png)

#### INPUT = rand_words.txt, HASH_METHOD = rolling, COLLISION_METHOD = chain
![](plots/rolling_chain_rand_add_time.png)
![](plots/rolling_chain_rand_search_time.png)

#### INPUT = non_rand_words.txt, HASH_METHOD = rolling, COLLISION_METHOD = linear
![](plots/rolling_linear_nonrand_add_time.png)
![](plots/rolling_linear_nonrand_search_time.png)

#### INPUT = non_rand_words.txt, HASH_METHOD = rolling, COLLISION_METHOD = chain
![](plots/rolling_chain_nonrand_add_time.png)
![](plots/rolling_chain_nonrand_search_time.png)
