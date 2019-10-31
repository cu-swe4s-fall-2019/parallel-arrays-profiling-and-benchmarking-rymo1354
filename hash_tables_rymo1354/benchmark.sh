# Function calls to generate plots for different hashes from rand_words.txt

python hash_functions.py --input rand_words.txt --hash_method ascii --table_size 100000 | python scatter.py --out_file plots/ascii_random.png --x_label "Hashed word" --y_label "Hashed value"

python hash_functions.py --input rand_words.txt --hash_method rolling --table_size 100000 | python scatter.py --out_file plots/rolling_random.png --x_label "Hashed word" --y_label "Hashed value"

python hash_functions.py --input rand_words.txt --hash_method weighted --table_size 100000 | python scatter.py --out_file plots/weighted_random.png --x_label "Hashed word" --y_label "Hashed value"

python hash_functions.py --input rand_words.txt --hash_method binning --table_size 100000 | python scatter.py --out_file plots/binning_random.png --x_label "Hashed word" --y_label "Hashed value"

# Function calls to generate plots for different hashes from non_rand_words.txt

python hash_functions.py --input non_rand_words.txt --hash_method ascii --table_size 100000 | python scatter.py --out_file plots/ascii_nonrandom.png --x_label "Hashed word" --y_label "Hashed value"

python hash_functions.py --input non_rand_words.txt --hash_method rolling --table_size 100000 | python scatter.py --out_file plots/rolling_nonrandom.png --x_label "Hashed word" --y_label "Hashed value"

python hash_functions.py --input non_rand_words.txt --hash_method weighted --table_size 100000 | python scatter.py --out_file plots/weighted_nonrandom.png --x_label "Hashed word" --y_label "Hashed value"

python hash_functions.py --input non_rand_words.txt --hash_method binning --table_size 100000 | python scatter.py --out_file plots/binning_nonrandom.png --x_label "Hashed word" --y_label "Hashed value"

# Function calls to generate .txt for linear probing and chainedhash from rand_words.txt

for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --input rand_words.txt --table_size 10000 --hash_method ascii --collision_strategy linear --keys_to_add $M --times_to_search 100 >  ascii_linear_rand.$M.txt
    python hash_tables.py --input rand_words.txt --table_size 10000 --hash_method ascii --collision_strategy chain --keys_to_add $M --times_to_search 100 >  ascii_chain_rand.$M.txt

    python hash_tables.py --input rand_words.txt --table_size 10000 --hash_method rolling --collision_strategy linear --keys_to_add $M --times_to_search 100 >  rolling_linear_rand.$M.txt
    python hash_tables.py --input rand_words.txt --table_size 10000 --hash_method rolling --collision_strategy chain --keys_to_add $M --times_to_search 100 >  rolling_chain_rand.$M.txt
    
    python hash_tables.py --input rand_words.txt --table_size 10000 --hash_method weighted --collision_strategy linear --keys_to_add $M --times_to_search 100 >  weighted_linear_rand.$M.txt
    python hash_tables.py --input rand_words.txt --table_size 10000 --hash_method weighted --collision_strategy chain --keys_to_add $M --times_to_search 100 >  weighted_chain_rand.$M.txt
    
    python hash_tables.py --input rand_words.txt --table_size 10000 --hash_method binning --collision_strategy linear --keys_to_add $M --times_to_search 100 >  binning_linear_rand.$M.txt
    python hash_tables.py --input rand_words.txt --table_size 10000 --hash_method binning --collision_strategy chain --keys_to_add $M --times_to_search 100 >  binning_chain_rand.$M.txt
done

# Function calls to generate .txt for linear probing and chainedhash from non_rand_words.txt

for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --input non_rand_words.txt --table_size 10000 --hash_method ascii --collision_strategy linear --keys_to_add $M --times_to_search 100 >  ascii_linear_nonrand.$M.txt
    python hash_tables.py --input non_rand_words.txt --table_size 10000 --hash_method ascii --collision_strategy chain --keys_to_add $M --times_to_search 100 >  ascii_chain_nonrand.$M.txt

    python hash_tables.py --input non_rand_words.txt --table_size 10000 --hash_method rolling --collision_strategy linear --keys_to_add $M --times_to_search 100 >  rolling_linear_nonrand.$M.txt
    python hash_tables.py --input non_rand_words.txt --table_size 10000 --hash_method rolling --collision_strategy chain --keys_to_add $M --times_to_search 100 >  rolling_chain_nonrand.$M.txt
    
    python hash_tables.py --input non_rand_words.txt --table_size 10000 --hash_method weighted --collision_strategy linear --keys_to_add $M --times_to_search 100 >  weighted_linear_nonrand.$M.txt
    python hash_tables.py --input non_rand_words.txt --table_size 10000 --hash_method weighted --collision_strategy chain --keys_to_add $M --times_to_search 100 >  weighted_chain_nonrand.$M.txt
    
    python hash_tables.py --input non_rand_words.txt --table_size 10000 --hash_method binning --collision_strategy linear --keys_to_add $M --times_to_search 100 >  binning_linear_nonrand.$M.txt
    python hash_tables.py --input non_rand_words.txt --table_size 10000 --hash_method binning --collision_strategy chain --keys_to_add $M --times_to_search 100 >  binning_chain_nonrand.$M.txt
done

# Function calls to generate plots for linear probing and chainedhash from rand_words.txt

# Linear Probing from rand_words.txt

grep add ascii_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/ascii_linear_rand_add_time.png --x_label "Load factor" --y_label "Insert time"
grep search ascii_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/ascii_linear_rand_search_time.png --x_label "Load factor" --y_label "Search time"

grep add rolling_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/rolling_linear_rand_add_time.png --x_label "Load factor" --y_label "Insert time"
grep search rolling_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/rolling_linear_rand_search_time.png --x_label "Load factor" --y_label "Search time"

grep add weighted_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/weighted_linear_rand_add_time.png --x_label "Load factor" --y_label "Insert time"
grep search weighted_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/weighted_linear_rand_search_time.png --x_label "Load factor" --y_label "Search time"

grep add binning_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/binning_linear_rand_add_time.png --x_label "Load factor" --y_label "Insert time"
grep search binning_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/binning_linear_rand_search_time.png --x_label "Load factor" --y_label "Search time"

# Chained Hash from rand_words.txt

grep add ascii_chain_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/ascii_chain_rand_add_time.png --x_label "Load factor" --y_label "Insert time"
grep search ascii_chain_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/ascii_chain_rand_search_time.png --x_label "Load factor" --y_label "Search time"

grep add rolling_chain_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/rolling_chain_rand_add_time.png --x_label "Load factor" --y_label "Insert time"
grep search rolling_chain_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/rolling_chain_rand_search_time.png --x_label "Load factor" --y_label "Search time"

grep add weighted_chain_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/weighted_chain_rand_add_time.png --x_label "Load factor" --y_label "Insert time"
grep search weighted_chain_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/weighted_chain_rand_search_time.png --x_label "Load factor" --y_label "Search time"

grep add binning_chain_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/binning_chain_rand_add_time.png --x_label "Load factor" --y_label "Insert time"
grep search binning_chain_rand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/binning_chain_rand_search_time.png --x_label "Load factor" --y_label "Search time"

# Function calls to generate plots for linear probing and chainedhash from non_rand_words.txt

# Linear Probing from non_rand_words.txt

grep add ascii_linear_nonrand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/ascii_linear_nonrand_add_time.png --x_label "Load factor" --y_label "Insert time"
grep search ascii_linear_nonrand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/ascii_linear_nonrand_search_time.png --x_label "Load factor" --y_label "Search time"

grep add rolling_linear_nonrand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/rolling_linear_nonrand_add_time.png --x_label "Load factor" --y_label "Insert time"
grep search rolling_linear_nonrand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/rolling_linear_nonrand_search_time.png --x_label "Load factor" --y_label "Search time"

grep add weighted_linear_nonrand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/weighted_linear_nonrand_add_time.png --x_label "Load factor" --y_label "Insert time"
grep search weighted_linear_nonrand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/weighted_linear_nonrand_search_time.png --x_label "Load factor" --y_label "Search time"

grep add binning_linear_nonrand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/binning_linear_nonrand_add_time.png --x_label "Load factor" --y_label "Insert time"
grep search binning_linear_nonrand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/binning_linear_nonrand_search_time.png --x_label "Load factor" --y_label "Search time"

# Chained Hash from non_rand_words.txt

grep add ascii_chain_nonrand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/ascii_chain_nonrand_add_time.png --x_label "Load factor" --y_label "Insert time"
grep search ascii_chain_nonrand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/ascii_chain_nonrand_search_time.png --x_label "Load factor" --y_label "Search time"

grep add rolling_chain_nonrand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/rolling_chain_nonrand_add_time.png --x_label "Load factor" --y_label "Insert time"
grep search rolling_chain_nonrand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/rolling_chain_nonrand_search_time.png --x_label "Load factor" --y_label "Search time"

grep add weighted_chain_nonrand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/weighted_chain_nonrand_add_time.png --x_label "Load factor" --y_label "Insert time"
grep search weighted_chain_nonrand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/weighted_chain_nonrand_search_time.png --x_label "Load factor" --y_label "Search time"

grep add binning_chain_nonrand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/binning_chain_nonrand_add_time.png --x_label "Load factor" --y_label "Insert time"
grep search binning_chain_nonrand.*.txt | cut -d " " -f2,3 | python scatter.py --out_file plots/binning_chain_nonrand_search_time.png --x_label "Load factor" --y_label "Search time"

rm *000*
