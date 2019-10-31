import hash_functions
import argparse
import sys
import random
import os
import time


def reservoir_sampling(new_val, size, V):
    """
    Creates list V for word sampling
    Arguments
    _________
    new_val: new value string to add
    size: maximum size of list V
    V: list to change

    Returns
    _______
    Nothing, but changes V outside of function
    """

    if len(V) < size:
        V.append(new_val)
    else:
        j = random.randint(0, len(V))
        if j < len(V):
            V[j] = new_val


class LinearProbe:
    """Reads in an integer and hash function type and:

        - adds a key and value to array position based
            on hash function chosen
        - handles duplicates by moving to the next empty
            position in the array and adding there
        - searches for and returns value of given key
            by linear search algorithm

    Attributes:
        hash_function: hash function type to use
        N: length of the hash array
        T: array to hold the (key, value) tuples
        M: number of indexes occupied by (key, value)
    """

    def __init__(self, N, hash_function):
        """Initializes hash_function, N, T, and M attributes"""
        self.hash_function = hash_function
        self.N = N
        self.T = [None for i in range(N)]
        self.M = 0

    def add(self, key, value):
        """
        adds (key, value) tuple to index from hash_function
        Arguments
        _________
        key : string to search for
        value : value associated with key
        Returns
        _______
        True: if (key, value) added to empty slot
        False: if no empty slots to add (key, value)
        """

        hash_slot = self.hash_function(key, self.N)

        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            if self.T[test_slot] is None:
                self.T[test_slot] = (key, value)
                self.M += 1
                return True
        return False

    def search(self, key):
        """
        searches for key in array and returns value
        Arguments
        _________
        key : string to search for
        Returns
        _______
        value: if (key, value) located
        None: if key not in array
        """

        hash_slot = self.hash_function(key, self.N)

        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            if self.T[test_slot] is None:
                return None
            if self.T[test_slot][0] == key:
                return self.T[test_slot][1]
        return None


class ChainedHash:
    """Reads in an integer and hash function type and:

        - adds a key and value to array in array  based
            on hash function chosen
        - handles duplicates by appending to the array
            at the position given by the key index
        - searches for and returns value of given key
            by locating the array of interest

    Attributes:
        hash_function: hash function type to use
        N: length of the hash array
        T: 2-D array to hold the (key, value) tuples
        M: number of times (key, value) appended
    """

    def __init__(self, N, hash_method):
        self.hash = hash_method
        self.N = N
        self.T = [[] for i in range(N)]
        self.M = 0

    def add(self, key, value):
        """
        adds (key, value) tuple to index from hash_function
        Arguments
        _________
        key : string to add to array
        value : value associated with key
        Returns
        _______
        True: when (key, value) added to empty slot
        """

        hash_slot = self.hash(key, self.N)
        self.T[hash_slot].append((key, value))
        self.M += 1
        return True

    def search(self, key):
        """
        searches for key in array within array and returns value
        Arguments
        _________
        key : string to search for
        Returns
        _______
        v: if (key, v) located
        None: if key not in array
        """

        hash_slot = self.hash(key, self.N)

        for k, v in self.T[hash_slot]:
            if key == k:
                return v
        return None


if __name__ == '__main__':
    # adding arguments
    parser = argparse.ArgumentParser(
        description='Implement hash tables',
        prog='hash_tables')

    parser.add_argument('--input', type=str,
                        help='Name of the input file', required=True)
    parser.add_argument('--table_size', type=int,
                        help='Size of hash table', required=True)
    parser.add_argument('--hash_method', type=str,
                        help='ascii/weighted/binning/rolling', required=True)
    parser.add_argument('--collision_strategy', type=str,
                        help='linear/chain', required=True)
    parser.add_argument('--keys_to_add', type=int,
                        help='Keys added to table', required=True)
    parser.add_argument('--times_to_search', type=int,
                        help='Times to search table', required=True)

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print('Cannot find input file')
        sys.exit(1)

    ht = None
    valid_collisions = ['linear', 'chain']
    if args.collision_strategy not in valid_collisions:
        print('Hash algorithm not supported at this time')
        sys.exit(1)

    if args.hash_method == 'ascii':
        if args.collision_strategy == 'linear':
            ht = LinearProbe(args.table_size, hash_functions.h_ascii)
        elif args.collision_strategy == 'chain':
            ht = ChainedHash(args.table_size, hash_functions.h_ascii)

    elif args.hash_method == 'weighted':
        if args.collision_strategy == 'linear':
            ht = LinearProbe(args.table_size, hash_functions.h_weighted)
        elif args.collision_strategy == 'chain':
            ht = ChainedHash(args.table_size, hash_functions.h_weighted)

    elif args.hash_method == 'binning':
        if args.collision_strategy == 'linear':
            ht = LinearProbe(args.table_size, hash_functions.h_binning)
        elif args.collision_strategy == 'chain':
            ht = ChainedHash(args.table_size, hash_functions.h_binning)

    elif args.hash_method == 'rolling':
        if args.collision_strategy == 'linear':
            ht = LinearProbe(args.table_size, hash_functions.h_rolling)
        elif args.collision_strategy == 'chain':
            ht = ChainedHash(args.table_size, hash_functions.h_rolling)

    else:
        print('Hash algorithm not supported at this time')
        sys.exit(1)

    V = []

    for line in open(args.input):
        reservoir_sampling(line, args.times_to_search, V)
        t0 = time.time()
        ht.add(line, line)
        t1 = time.time()
        print('add', ht.M/ht.N, t1 - t0)
        if ht.M == args.keys_to_add:
            break

    for value in V:
        t0 = time.time()
        r = ht.search(value)
        t1 = time.time()
        print('search', t1 - t0)

    sys.exit(0)
