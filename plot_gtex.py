import data_viz
import gzip
import sys
import os
import argparse


# parse arguments
def parse_args():

    parser = argparse.ArgumentParser(
        description='Correctly pass input parameters',
        prog='plot_gtex.py')

    parser.add_argument('--gene_reads',
                        type=str,
                        help='Gene database of interest .gz file',
                        required=True)

    parser.add_argument('--sample_attributes',
                        type=str,
                        help='Meta-data .txt file',
                        required=True)

    parser.add_argument('--gene',
                        type=str,
                        help='Gene of interest, i.e. ACTA2',
                        required=True)

    parser.add_argument('--group_type',
                        type=str,
                        help='The group type. i.e. SMTS',
                        required=True)

    parser.add_argument('--output_file',
                        type=str,
                        help='Saved plot filename',
                        required=True)

    return parser.parse_args()


def linear_search(key, L):

    """
    Linear search for first index in list equivalent to key

    Arguments
    ________
    key: datatype being searched for
    L: list being searched

    Returns
    _______
    i: if key is in the list
    -1: if key is not in the list
    """

    for i in range(len(L)):
        if key == L[i]:
            return i
    return -1


def binary_search(key, L):

    """
    Binary search for first index in list equivalent to key

    Arguments
    ________
    key: datatype being searched for
    L: list being searched

    Returns
    _______
    i: if key is in the list
    -1: if key is not in the list
    """

    lo = 0
    hi = len(L)-1
    while (lo <= hi):
        mid = (hi + lo) // 2

        if key == L[mid][0]:
            return L[mid][1]

        if (key < L[mid][0]):
            hi = mid - 1
        else:
            lo = mid + 1

    return -1


def meta_data(file_group, file):

    """
    Gets certain values for samples and target group from file_group

    Arguments
    ________
    file_group: group in the header of file that is desired
    file: .txt file being explored

    Returns
    _______
    samples: list of info from index of samples
    target_group: list of info for file_group
    """

    header = None
    samples = []
    target_group = []

    for l in open(file):
        samples_info = l.rstrip().split('\t')

        if header is None:
            header = samples_info
            continue

        sample_idx = linear_search('SAMPID', header)
        target_idx = linear_search(file_group, header)

        if (target_idx == -1):
            return [], []

        samples.append(samples_info[sample_idx])
        target_group.append(samples_info[target_idx])

    return samples, target_group


def main():

    args = parse_args()

    if not os.path.exists(args.sample_attributes):
        print('Cannot find file %s' % args.sample_attributes)
        sys.exit(1)
    if not os.path.exists(args.gene_reads):
        print('Cannot find meta file %s' % args.gene_reads)
        sys.exit(1)

    samples, target_group = meta_data(args.group_type,
                                      args.sample_attributes)

    if len(target_group) == 0:
        print('Cannot find group_type %s' % target_group)
        sys.exit(1)

    version = None
    dimension = None
    rna_header = None
    for l in gzip.open(args.gene_reads, 'rt'):

        if version is None:
            version = l
            continue

        if dimension is None:
            dimension = l
            continue

        if rna_header is None:
            rna_header = l.rstrip().split('\t')
            rna_header_plus_index = []
            for i in range(len(rna_header)):
                rna_header_plus_index.append([rna_header[i], i])

            rna_header_plus_index.sort()

            continue

        rna_counts = l.rstrip().split('\t')
        description_idx = linear_search('Description', rna_header)

        if description_idx == -1:
            print('Gene not found in header')
            sys.exit(1)

        if rna_counts[description_idx] == args.gene:
            attrs = list(set(target_group))
            attrs.sort()
            par_array = []
            for attr in attrs:
                attr_idxs = []
                for i in range(len(target_group)):
                    if attr == target_group[i]:
                        attr_idxs.append(i)

                attr_counts = []
                for attr_idx in attr_idxs:
                    # linear search
                    # rna_header_idx = linear_search(samples[attr_idx],
                    #                               rna_header)
                    # binary search
                    rna_header_idx = binary_search(samples[attr_idx],
                                                   rna_header_plus_index)
                    if rna_header_idx == -1:
                        continue
                    count = rna_counts[rna_header_idx]
                    attr_counts.append(int(count))
                par_array.append(attr_counts)
            data_viz.boxplot(par_array, attrs, args.gene,
                             args.group_type, "Gene read counts",
                             args.output_file)
            sys.exit(0)

    sys.exit(0)


if __name__ == '__main__':
    main()
