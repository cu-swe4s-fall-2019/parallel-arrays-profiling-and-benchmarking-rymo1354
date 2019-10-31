#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_style pycodestyle hash_functions.py
assert_no_stdout
run test_style pycodestyle hash_tables.py
assert_no_stdout
run test_style pycodestyle scatter.py
assert_no_stdout
run test_style pycodestyle test_hash_functions.py
assert_no_stdout
run test_style pycodestyle test_hash_tables.py
assert_no_stdout
run test_style pycodestyle test_scatter.py
assert_no_stdout

run test_hash_functions python hash_functions.py --input rand_words.txt --hash_method ascii --table_size 10000
assert_exit_code 0
run test_hash_functions python hash_functions.py --input non_rand_words.txt --hash_method ascii --table_size 10000
assert_exit_code 0
run test_hash_functions python hash_functions.py --input rand_words.txt --hash_method rolling --table_size 10000
assert_exit_code 0
run test_hash_functions python hash_functions.py --input non_rand_words.txt --hash_method rolling --table_size 10000
assert_exit_code 0
run test_hash_functions python hash_functions.py --input rand_words.txt --hash_method weighted --table_size 10000
assert_exit_code 0
run test_hash_functions python hash_functions.py --input non_rand_words.txt --hash_method weighted --table_size 10000
assert_exit_code 0
run test_hash_functions python hash_functions.py --input rand_words.txt --hash_method binning --table_size 10000
assert_exit_code 0
run test_hash_functions python hash_functions.py --input non_rand_words.txt --hash_method binning --table_size 10000
assert_exit_code 0

run bad_input python hash_functions.py --input no_words.txt --hash_method ascii --table_size 10000
assert_exit_code 1
assert_stdout
run bad_input python hash_functions.py --input rand_words.txt --hash_method _ascii --table_size 10000
assert_exit_code 1
assert_stdout
run bad_input python hash_functions.py --input rand_words.txt --hash_method ascii --table_size -1
assert_exit_code 1
assert_stdout

run test_hash_tables python hash_tables.py --input non_rand_words.txt --table_size 10000 --hash_method ascii --collision_strategy linear --keys_to_add 10 --times_to_search 10
assert_exit_code 0
run test_hash_tables python hash_tables.py --input rand_words.txt --table_size 10000 --hash_method binning --collision_strategy chain --keys_to_add 10 --times_to_search 10
assert_exit_code 0
run test_hash_tables python hash_tables.py --input rand_words.txt --table_size 10000 --hash_method weighted --collision_strategy linear --keys_to_add 10 --times_to_search 10
assert_exit_code 0
run test_hash_tables python hash_tables.py --input non_rand_words.txt --table_size 10000 --hash_method rolling --collision_strategy chain --keys_to_add 10 --times_to_search 10
assert_exit_code 0

run bad_input python hash_tables.py --input no_words.txt --table_size 10000 --hash_method ascii --collision_strategy linear --keys_to_add 10 --times_to_search 10
assert_exit_code 1
assert_stdout
run bad_hash python hash_tables.py --input rand_words.txt --table_size 10000 --hash_method bad --collision_strategy linear --keys_to_add 10 --times_to_search 10
assert_exit_code 1
assert_stdout
run bad_collision python hash_tables.py --input rand_words.txt --table_size 10000 --hash_method ascii --collision_strategy bad --keys_to_add 10 --times_to_search 10
assert_exit_code 1
assert_stdout




