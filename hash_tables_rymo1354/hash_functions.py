import sys
import os
import argparse
import collections.abc


def check_hashable(key):
    """
    Determines if passed key is hashable type
    Arguments
    _________
    key: hashable type to convert to string

    Returns
    _______
    True : if type is hashable
        Otherwise, returns False
    """

    if isinstance(key, collections.Hashable) is True:
        return True

    else:
        return False


def check_integer(N):
    """
    Determines if passed value can be integer
    Arguments
    _________
    N: type to convert to integer

    Returns
    _______
    True : if type is positive integer
        Otherwise, returns False
    """

    try:
        N = int(N)
        if N <= 0:
            raise ValueError
        else:
            return True
    except ValueError:
        print("Unhashable type as N")
        return False


def h_ascii(key, N):
    """
    Gets ascii hash of key
    Arguments
    _________
    key: string to be hashed
    N: length of hash table

    Returns
    _______
    s % N : Position of key in hash table
    """

    s = 0
    for i in range(len(key)):
        s += ord(key[i])
    return s % N


def h_rolling(key, N, p=53, m=2**64):
    """
    Gets rolling hash of key
    Arguments
    _________
    key: string to be hashed
    N: length of hash table

    Returns
    _______
    s % N : Position of key in hash table
    """
    s = 0
    for i in range(len(key)):
        s += ord(key[i]) * p**i
    s = s % m
    return s % N


def h_weighted(key, N):
    """
    Gets ascii hash of key weighted by position
    Arguments
    _________
    key: string to be hashed
    N: length of hash table

    Returns
    _______
    s % N : Position of key in hash table
    """
    s = 0
    for i in range(len(key)):
        s += i * ord(key[i])
    return s % N


def h_binning(key, N):
    """
    Gets binned hash of key (max 2 per bin)
    Arguments
    _________
    key: string to be hashed
    N: length of hash table

    Returns
    _______
    s % N : Position of key in hash table
    """
    ascii_nums = []
    for letter in key:
        ascii_nums.append(ord(letter))

    paired = []
    for i in range(len(ascii_nums)):
        first = i*2
        second = i*2+1
        if first < len(ascii_nums) and second < len(ascii_nums):
            val = int(str(ascii_nums[first])+str(ascii_nums[second]))
            paired.append(val)
        elif first < len(ascii_nums) and second >= len(ascii_nums):
            paired.append(ascii_nums[first])
        else:
            continue

    s = 0
    for i in range(len(paired)):
        s += paired[i]
    return s % N


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Hash Function Implementation',
        prog='hash_functions')

    parser.add_argument('--input', type=str,
                        help='Name of the input file', required=True)
    parser.add_argument('--hash_method', type=str,
                        help='ascii/weighted/binning/rolling', required=True)
    parser.add_argument('--table_size', type=int,
                        help='Size of hash table', required=True)

    args = parser.parse_args()

    if check_integer(args.table_size) is not True:
        print('Invalid integer')
        sys.exit(1)

    if (os.path.exists(args.input)):
        for line in open(args.input):
            if check_hashable(line) is True:
                if (args.hash_method == 'ascii'):
                    print(h_ascii(line, args.table_size))
                elif (args.hash_method == 'rolling'):
                    print(h_rolling(line, args.table_size))
                elif (args.hash_method == 'binning'):
                    print(h_binning(line, args.table_size))
                elif (args.hash_method == 'weighted'):
                    print(h_weighted(line, args.table_size))
                else:
                    print('Hash method not supported')
                    sys.exit(1)
            else:
                sys.exit(1)
        sys.exit(0)
    else:
        print('Input file does not exist')
        sys.exit(1)
